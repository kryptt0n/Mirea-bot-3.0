import bot_class
from threading import Thread, Lock
import os
import time

def main():
    bot = bot_class.Bot()
    bot.goto("https://events.webinar.ru/21390906/11012455/7f86c85da0547ef5b1086875cd9771d5")
    thread = Thread(target=bot.check)
    thread.start()
    time.sleep(2)
    if input("ВВедите exit") == "exit":
        bot.lock.acquire()
        bot.stop = True
        bot.lock.release()
    # print("end")
    # urls = list(map(str.rstrip, get_urls()))
    # print(urls)
    pass

# Удаление \n переноса строки в конце строки
def remove_n(text):
    if r"\n" in text:
        return text[:-2]
    else:
        return text

# Получение ссылок из текстового файла
def get_urls():
    urls = []
    if os.path.exists("urls.txt"):
        with open("urls.txt") as file:
            lines = file.readlines()
            for line in lines:
                urls.append(line)
    else:
        with open("urls.txt", 'w'):
            pass

    return urls

if __name__ == '__main__':
    main()

