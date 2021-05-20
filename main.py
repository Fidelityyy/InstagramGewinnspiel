import time
from selenium import webdriver

pcBenutzername = "R11111111111"
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:/Users/" + pcBenutzername + "/AppData/Local/Google/Chrome/User Data")
browser = webdriver.Chrome(executable_path="D:/chromedriver_win32/chromedriver.exe", options=options)
followerNamen = []
kommentarNamen = []

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
    print("Followerarraylänge: " + str(len(followerNamen)))
    print("Liker abholen...")
    browser.get(instaBildSeite)
    kommentarleute = []
    print("Kommentararray erstellt!")
    kommentareladenknopf = browser.find_element_by_css_selector('.dCJp8.afkep')
    for x in range(15):
        kommentareladenknopf.click()
        time.sleep(1)
    print(browser.find_element_by_xpath(
        "tml/body/div[1]/section/main/div/div[1]/article/div[3]/div[1]/ul/ul[1]/div/li/div/div[1]/div[2]/span"))
    for x in range(1, 100):
        kommentarleute[x - 1] = browser.find_element_by_xpath(
            "tml/body/div[1]/section/main/div/div[1]/article/div[3]/div[1]/ul/ul[" + str(
                x) + "]/div/li/div/div[1]/div[2]/span")
    print("I N K B U S T E R S - - - G E W I N N S P I E L")
    go = False
    while not go:
        goprompt = input("go um zu starten ")
        if goprompt == 'go':
            go = True
    for follower in followerNamen:
        print(follower.replace('https://www.instagram.com/', '').replace('/', ''))


try:
    for x in range(1, followerAnzahl):
        followerNamen.append((browser.find_element_by_xpath(
            "/html/body/div[5]/div/div/div[2]/ul/div/li[" + str(x) + "]/div/div[1]/div[2]/div[1]/span/a"))
                             .get_attribute("href"))
    restzeug()
except:
    restzeug()
