import time
from selenium import webdriver
import winsound

browser = webdriver.Chrome('D:/chromedriver_win32/chromedriver.exe')

browser.get('https://www.alternate.de/Grafikkarten/AMD-Grafikkarten')
browser.maximize_window()