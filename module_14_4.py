# Домашнее задание по теме "План написания админ панели.".

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup , InlineKeyboardButton
from crud_functions import *


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb_r = ReplyKeyboardMarkup(resize_keyboard=True)
button_info = KeyboardButton(text='Информация')
button_calc = KeyboardButton(text='Рассчитать')
button_buy = KeyboardButton(text='Купить')
kb_r.add(button_info)
kb_r.add(button_calc)
kb_r.add(button_buy)

kb_i = InlineKeyboardMarkup(resize_keyboard=True)
button_prod_1 = InlineKeyboardButton(text='Витамин А', callback_data='product_buying')
button_prod_2 = InlineKeyboardButton(text='Витамин B', callback_data='product_buying')
button_prod_3 = InlineKeyboardButton(text='Витамин С', callback_data='product_buying')
button_prod_4 = InlineKeyboardButton(text='Витамин D', callback_data='product_buying')
kb_i.add(button_prod_1)
kb_i.add(button_prod_2)
kb_i.add(button_prod_3)
kb_i.add(button_prod_4)


def get_all_products():
    connection = sqlite3.connect('not_telegram.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Products')
    prod = cursor.fetchall()
    connection.commit()
    connection.close()
    return prod


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью', reply_markup=kb_r)


@dp.message_handler(text='Информация')
async def set_age(message):
    await message.answer('Бот расчитывает дневную норму калорий по упрощенной формуле Миффлина - Сан Жеора.')


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:',  reply_markup=kb_i)


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    products = get_all_products()
    for prod in products:
        with open('./vitamin-c.jpg', 'rb') as img:
            await message.answer_photo(img, f'Название: {prod[1]} | Описание: {prod[2]} | Цена: {prod[3]}')
    await message.answer('Выберите продукт для покупки:', reply_markup=kb_i)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('формулы:\n'
                             'для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5;\n'
                             'для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161.')
    await call.answer()


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст (лет):')
    await call.answer()
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(first=message.text)
    await message.answer('Введите свой рост (см):')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(second=message.text)
    await message.answer('Введите свой вес (кг):')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(third=message.text)
    data = await state.get_data()
    calories = 10 * int(data['third']) + 625 * int(data['second']) / 100 - 5 * int(data['first'])
    men = calories - 5
    wom = calories - 161
    await message.answer(f'Дневная норма калорий для вас, если вы мужчина - {men}, если женщина - {wom}')
    await state.finish()


@dp.message_handler()
async def all_massages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

