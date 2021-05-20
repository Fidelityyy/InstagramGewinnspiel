import random
import time
from selenium import webdriver
from random import randint

pcBenutzername = "R11111111111"
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:/Users/" + pcBenutzername + "/AppData/Local/Google/Chrome/User Data")
browser = webdriver.Chrome(executable_path="D:/chromedriver_win32/chromedriver.exe", options=options)
followerNamen = []
kommentarNamen = []
anzahlKommentareLaden = 100

instaSeite = 'https://www.instagram.com/ink.busters/'
instaFollowSeite = 'https://www.instagram.com/ink.busters/followers/'
instaFollowSeiteKurz = '/ink.busters/followers/'
instaBildSeite = 'https://www.instagram.com/p/CO2zfbAFuc3/'
benutzername = ""  # input("Benutzername: ")
passwort = ""  # input("Passwort: ")

browser.get(instaFollowSeite)
# alleAnnehmenKnopf = browser.find_element_by_class_name('bIiDR')
# alleAnnehmenKnopf.click()
# time.sleep(5)
# print('Benutzerdaten abschicken...')
# emailFeld = browser.find_element_by_name('username')
# emailFeld.send_keys(benutzername)
# passwortFeld = browser.find_element_by_name('password')
# passwortFeld.send_keys(passwort)
# anmeldeButton = browser.find_element_by_class_name('_4EzTm')
# anmeldeButton.click()
# time.sleep(10)
print('Instagram Seite besuchen...')
# browser.get(instaSeite)
time.sleep(5)
followerAnzahl = int((browser.find_element_by_xpath(
    "/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span").get_attribute("title")).replace('.', ''))
followerKnopf = browser.find_element_by_xpath('//a[@href="' + instaFollowSeiteKurz + '"]')
time.sleep(5)
followerKnopf.click()
time.sleep(5)
# Scrollen von Follower
print("Follower abholen...")
followerPath = browser.find_element_by_xpath("/html/body/div[5]/div/div/div[2]")
css_selector = "body > div.RnEpo.Yx5HN > div > div > div.isgrP"
SCROLL_PAUSE_TIME = 2
last_height = browser.execute_script("return document.querySelector('" + css_selector + "').scrollHeight")
while True:
    browser.execute_script(
        "document.querySelector('" + css_selector + "').scrollTo(0, document.querySelector('" + css_selector +
        "').scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)
    new_height = browser.execute_script("return document.querySelector('" + css_selector + "').scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height


def restzeug():
    print(str(len(followerNamen)))
    for x in range(100):
        print("I N K B U S T E R S - - - G E W I N N S P I E L")
    print("Storyposter abholen...")
    print("Kommentare abholen...")
    browser.get(instaBildSeite)
    time.sleep(5)
    try:
        load_more_comment = browser.find_element_by_css_selector('.NUiEW > button:nth-child(1)')
        # print("Found {}".format(str(load_more_comment)))
        i = 0
        while load_more_comment.is_displayed() and i < int(anzahlKommentareLaden):
            load_more_comment.click()
            time.sleep(1.5)
            load_more_comment = browser.find_element_by_css_selector('.NUiEW > button:nth-child(1)')
            # print("Found {}".format(str(load_more_comment)))
            i += 1
    except Exception as e:
        print(e)
        pass

    user_names = []
    user_comments = []
    comment = browser.find_elements_by_class_name('gElp9 ')
    for c in comment:
        container = c.find_element_by_class_name('C4VMK')
        name = container.find_element_by_class_name('_6lAjh').text
        content = container.find_element_by_tag_name('span').text
        content = content.replace('\n', ' ').strip().rstrip()
        user_names.append(name)
        user_comments.append(content)
    user_names.pop(0)
    user_comments.pop(0)
    user_names = list(dict.fromkeys(user_names))
    gewinnspielliste = []
    followerkurz = []
    for follower in followerNamen:
        followerkurz.append(follower.replace('https://www.instagram.com/', '').replace('/', ''))
    for username in user_names:
        if username in followerkurz:
            gewinnspielliste.append(username)
    # print(user_names)
    gewinner = random.choice(gewinnspielliste)
    print("I N K B U S T E R S - - - G E W I N N S P I E L")
    go = False
    while not go:
        goprompt = input("go um zu starten ")
        if goprompt == 'go':
            go = True
    print("Gewinner ermitteln...")
    time.sleep(randint(5, 10))
    print(gewinner)
    while True:
        nochmalprompt = input("nochmal? ja / nein ")
        if nochmalprompt == 'ja':
            gewinner = random.choice(gewinnspielliste)
            print("Gewinner ermitteln...")
            time.sleep(randint(5, 10))
            print(gewinner)
        else:
            exit(0)


try:
    for x in range(1, followerAnzahl):
        followerNamen.append((browser.find_element_by_xpath(
            "/html/body/div[5]/div/div/div[2]/ul/div/li[" + str(x) + "]/div/div[1]/div[2]/div[1]/span/a"))
                             .get_attribute("href"))
    restzeug()
except:
    restzeug()
