from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from pathlib import Path
from threading import Thread, Lock, currentThread
import time



class Bot:
    stop_flag = False
    current_thread = Thread()
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features")
    driver = webdriver.Chrome(
        Path(r"chromedriver\chromedriver.exe"),
        options=options)

    # Открытие ссылки в окне браузера

    def __init__(self):
        self.lock = Lock()
        self.stop = False

    def goto(self, url):
        if not self.checkBrowserOpen(url):
            self.testgoto(url)

    def testgoto(self, url):
        self.driver.get(self.checkUrl(url))

    # Проверка открыто ли окно браузера

    def checkBrowserOpen(self, url):
        try:
            self.driver.get(self.checkUrl(url))
            return True
        except Exception as ex:
            print("Browser is closed: ", ex)
            return False

    # Проверка ссылки на корректный вид
    # Селениум воспринимает только ссылки с началом https

    def checkUrl(self, url):
        if "https://" in url:
            return url
        else:
            return "https://" + url

    # Проверка конкретной кнопки на появление
    # В случае если кнопка найдена, она нажимается
    # autoplay-video-allow-btn
    def test_shit(self):
        click_btns = self.driver.find_elements(By.TAG_NAME, "button")
        for click_btn in click_btns:
            if click_btn.get_property("className") == "btn btn_success btn_material":
                click_btn.click()
                print("Отметился")
        time.sleep(2)
        closebtn1 = self.driver.find_elements(By.TAG_NAME, "button")
        class_for_close = "btn-link AttentionControlModal__cancel___bcfZW btn-link_success btn-link_upper btn-link_bold"
        for close in closebtn1:
            if close.get_property("className") == class_for_close:
                close.click()
                print("Закрыл отмечалку")
        time.sleep(0.3)


    # Проверка разных элементов страницы на их появление
    # Первый элемент удачный
    # Остальные нужны если первый не сработает

    def check(self):
        print("скрипт работает")
        while (not self.stop):
            # / html / body / div[3] / div / div / div[3] / button
            # / html / body / div[3] / div / div / div[3] / button / span
            # /html/body/div[5]/div/div/div[3]/button
            self.lock.acquire()
            if self.stop is True:
                break
            self.lock.release()
            time.sleep(5)
            try:  # Сработало
                self.test_shit()
            except Exception as ex:
                pass
            "btn btn_success btn_material"
            time.sleep(15)

