import time
from selenium import webdriver
import getpass

browser = webdriver.Chrome('D:/chromedriver_win32/chromedriver.exe')
browser.minimize_window()
benutzername = input("Benutzername: ")
passwort = input("Passwort: ")
for x in range(100):
    print("I N K B U S T E R S - - - G E W I N N S P I E L")
go = False
while not go:
    goPrompt = input("go um zu starten ")
    if goPrompt == 'go':
        go = True
browser.get('https://www.instagram.com/ink.busters/followers/')
browser.maximize_window()
fertig = False
while not fertig:
    try:
        alleAnnehmenKnopf = browser.find_element_by_class_name('bIiDR')
        alleAnnehmenKnopf.click()
        time.sleep(5)
        emailFeld = browser.find_element_by_name('username')
        emailFeld.send_keys(benutzername)
        passwortFeld = browser.find_element_by_name('password')
        passwortFeld.send_keys(passwort)
        anmeldeButton = browser.find_element_by_class_name('_4EzTm')
        anmeldeButton.click()
        time.sleep(10)
        browser.get('https://www.instagram.com/ink.busters/')
        time.sleep(10)
        followerKnopf = browser.find_element_by_xpath('//a[@href="' + '/ink.busters/followers/' + '"]')
        time.sleep(5)
        followerKnopf.click()
    except:
        #browser.close()
        time.sleep(1)