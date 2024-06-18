from time import sleep

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


class Video:
    def __init__(self, title, duration, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = 0

class UrTube:
    def __init__(self):
        self.users = {}
        self.videos = []
        self.current_user = None


    def log_in(self, login, password):
        if login not in self.users:
            if hash(password) not in self.users.values():
                self.current_user = login

    def register(self, nickname, password, age):
        self.age = age
        if nickname not in self.users:
            self.users[nickname] = password
            self.current_user = nickname
        else:
            print(f"Пользователь {nickname} уже существует")

    def log_out(self):
        return self.current_user == None

    def add(self, *ved):
        list_ved=[*ved]
        for i in list_ved:
            if i not in self.videos:
                self.videos.append(i)
        return self.videos

    def get_videos(self, word):
        list_video = []
        for i in self.videos:
            if word.lower() in i.title.lower():
                list_video.append(i.title)
        return list_video

    def watch_video(self, word_video):
        if self.current_user:
            if self.age > 18:
                for video in self.videos:
                    if word_video in video.title:
                        for i in range(video.duration):
                            counter = ''
                            video.time_now += 1
                            counter += str(video.time_now)
                            print(counter, end=' ')
                            sleep(1)
                        print('Конец воиспроизведения')
                        video.time_now -= video.duration

            else:
                print("Вам нет 18 лет, пожалуйста покиньте страницу")
        else:
            print("Войдите в аккаунт чтобы смотреть видео")




ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)


ur.add(v1, v2)


print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))


ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')


ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)


ur.watch_video('Лучший язык программирования 2024 года!')
