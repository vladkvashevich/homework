from time import sleep

class User:
    def __init__ (self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return f"User: {self.nickname}, Password: {self.password}, Age: {self.age}"

class Video:
    def __init__ (self, title, duration, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

class UrTube:

    def __init__ (self):
        self.users_list = []
        self.videos_list = []
        self.current_user = None

    def register (self, nickname, password, age):
        for user in self.users_list:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        self.users_list.append(User(nickname, hash(password), age))
        self.log_in(nickname, password)

    def log_in (self, login, password):
        if self.current_user is None:
            for user in self.users_list:
                if user.nickname == login and user.password == hash(password):
                    self.current_user = user
                    return
            print("Неверный логин или пароль")
            return
        print("Вы уже вошли в аккаунт")

    def log_out (self):
        if self.current_user is None:
            print("Вы не входили в аккаунт")
            return
        self.current_user = None

    def add(self, *video_list):
        for video in video_list:
            if video.title not in [v.title for v in self.videos_list]:
                self.videos_list.append(video)

    def get_videos (self, search_word):
        result = []
        for video in self.videos_list:
            if search_word.lower() in video.title.lower():
                result.append(video.title)
        return result

    def watch_video (self, title):
        if self.current_user is None:
            print("Войдите в аккаунт чтобы смотреть видео")
            return
        for video in self.videos_list:
            if video.title == title:
                if self.current_user.age < 18 and video.adult_mode:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return
                print("Воспроизведение: ", end=" ")
                for second in range(video.duration):
                    sleep(1)
                    video.time_now += 1
                    print(second + 1, end=" ")
                return print("Конец видео")
            video.time_now = 0
        print("Видео не найдено")

ur = UrTube()

v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

ur.add(v1, v2)

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