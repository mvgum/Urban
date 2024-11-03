# Домашнее задание по теме "Клавиатура кнопок".
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


kb = ReplyKeyboardMarkup(resize_keyboard=True)
button_info = KeyboardButton(text='Информация')
button_calc = KeyboardButton(text='Рассчитать')
kb.add(button_info)
kb.add(button_calc)


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью', reply_markup=kb)


@dp.message_handler(text='Информация')
async def set_age(message):
    await message.answer('Бот расчитывает дневную норму калорий по упрощенной формуле Миффлина - Сан Жеора.')


@dp.message_handler(text='Рассчитать')
async def set_age(message):
    await message.answer('Введите свой возраст (лет):')
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
