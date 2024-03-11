# Dinosaur Game Bot

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import base64
import time
import pyautogui
from PIL import Image
import numpy as np


chrome_driver_path = "C:\Development\chromedriver.exe"
URL = "https://elgoog.im/dinosaur-game/"
ser = Service(chrome_driver_path)
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)  # Create a new driver from the new module chromedriver
driver.get(URL)
driver.maximize_window()


screenWidth, screenHeight = pyautogui.size()  # Get the size of the primary monitor.


#
def space():
    pyautogui.press(['space'])


def _up():
    pyautogui.press(['up'])


def _down():
    pyautogui.keyDown('down')
    time.sleep(0.3)
    pyautogui.press('down')


def get_image():
    road = driver.find_element(By.CSS_SELECTOR, 'div.runner-container:nth-child(6) > canvas:nth-child(1)')

    # get the canvas as a PNG base64 string
    road_base64 = driver.execute_script("return arguments[0].toDataURL('image/jpg').substring(21);", road)

    # decode
    road_png = base64.b64decode(road_base64)

    # save to a file
    with open(r"road.png", 'wb') as f:
        f.write(road_png)


# # # # # # # # # # # # # # # # # Start Game # # # # # # # # # # # # # # # # # # # # # # # # #

time.sleep(10)
space()

while True:
    get_image()

    file_name = 'road.png'
    my_array = np.array(Image.open(file_name))
    if_up = np.mean(my_array[90:150, 80:150, :])
    if_down = np.mean(my_array[70:100, 90:150, :])

    if if_up > 3:
        _up()
    elif if_down > 12:
        _down()
    else:
        pass
