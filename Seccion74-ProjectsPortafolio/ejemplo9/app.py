import time
import mss
import pyautogui
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://elgoog.im/t-rex/')
driver.maximize_window()
time.sleep(2)
pyautogui.press('space')
count = 0
while True:
    with mss.mss() as sct:
        width = 30

        if width < 200:
            width += 0.05 * count
        gameover_img = sct.grab({'top': 300, 'left': 800, 'width': 50, 'height': 50})
        count += 1
        img2 = sct.grab({'top': 355, 'left': 665 , 'width': width, 'height': 50})
        mss.tools.to_png(gameover_img.rgb, gameover_img.size, output='gameover.png')
        mss.tools.to_png(img2.rgb, img2.size, output='dummy2.png')
        values = (83, 83, 83)
        im = Image.open('dummy2.png')
        gm = Image.open('gameover.png').convert('RGB')
        rgb_im = im.convert('RGB')
        gameover_pixels = [i for i in gm.getdata()]
        pixels2 = [i for i in rgb_im.getdata()]

        if values in pixels2 and values not in gameover_pixels:
            pyautogui.press('space')
        elif values in gameover_pixels:
            count = 0
            time.sleep(2)
            pyautogui.press('space')