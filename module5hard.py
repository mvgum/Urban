# Дополнительное практическое задание по модулю: "Классы и объекты."
import time


class User:

    def __init__(self, nickname, password, age):
        self.name = nickname
        self.password = hash(password)
        self.age = age


class Video:

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:

    def __init__(self):
        self.current_user = None
        self.videos = {}
        self.users = {}

    def log_in(self, nickname, password):
        flag = False
        for key, value in self.users.items():
            if key == nickname:
                flag = True
                break
        return flag

    def register(self, nickname, password, age):
        if self.log_in(nickname, password):
            print(f"Пользователь {nickname} уже существует")
        else:
            self.users[nickname] = [password, age]
            self.current_user = nickname

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for elem in args:
            if elem not in self.videos.keys():
                self.videos[elem.title] = [elem.duration, elem.time_now, elem.adult_mode]

    def get_videos(self, word):
        video_list = []
        for title, other in self.videos.items():
            for elem in title.split():
                if word.lower() in elem.lower():
                    video_list.append(title)
                    break
        return video_list

    def watch_video(self, title):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео!")
        else:
            for key, values in self.videos.items():
                if title == key:
                    if self.videos[title][2]:
                        if self.users[self.current_user][1] < 18:
                            print("Вам нет 18 лет, пожалуйста покиньте страницу")
                        else:
                            time_now = values[1]
                            duration = values[0]
                            for i in range(time_now, duration):
                                print(i, end=" ")
                                time.sleep(0.3)
                            print("Конец видео")

    def info(self):
        for el, values in self.videos.items():
            print(el, values)

    def check_user(self):
        flag = True
        if self.current_user == "urban_pythonist":
            flag = False
            print("Войдите в аккаунт, чтобы смотреть видео!")
        else:
            if self.users[self.current_user][1] >= 18:
                print("YYY")


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
