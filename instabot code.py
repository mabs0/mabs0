from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium .webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path="C:/Users/Elève/Desktop/projet/ytb tuto code/video/tuto instabot fr/chromedriver.exe")
action = ActionChains(driver)

Username = "latar72337@lenfly.com"
Password = "Jules_290"


def Start():
    try:
        driver.get("https://www.instagram.com")
        print("driver ouvert")

    except:
        print("driver non ouvert")


def Cookies():
    try:
        driver.find_element(By.CLASS_NAME, "bIiDR").click()
        print("cookies acceptés")

    except:
        print("cookies non acceptés")


def Login(username, password):
    try:
        cookies = False
        while cookies == False:
            try:
                if driver.find_element(By.NAME, "username"):
                    driver.find_element(By.NAME, "username").send_keys(username)
                    driver.find_element(By.NAME, "password").send_keys(password)
                    cookies = True

                    driver.find_elements(By.CLASS_NAME, "IwRSH")[1].click()
                    connect = False
                    while connect == False:
                        try:
                            if driver.find_element(By.CLASS_NAME, "XrOey"):
                                print("connecté")
                                connect = True

                        except:
                            pass

            except:
                pass

    except:
        print("non connecté")


def Follow(url):
    driver.get(url)

    try:
        button = False
        while button == False:
            try:
                if driver.find_elements(By.CLASS_NAME, "_aaco"):
                    driver.find_elements(By.CLASS_NAME, "_aaco")[1].click()

                    follow = False
                    while follow == False:
                        try:
                            if driver.find_element(By.CLASS_NAME, "_ab9p"):
                                print("follow executé")
                                follow = True
                                button = True

                        except:
                            pass

                elif driver.find_element(By.CLASS_NAME, "_ab9p"):
                    print("follow déja executé")
                    button = True

            except:
                pass

    except:
        print("une erreur est survenue dans le follow")


def Like(url, postsIndex):
    driver.get(url)

    posts = False
    while posts == False:
        if driver.find_elements(By.CLASS_NAME, "_aabd"):
            posts = driver.find_elements(By.CLASS_NAME, "_aabd")

            for i in postsIndex:
                posts[i].click()
                like = False
                while like == False:
                    try:
                        if driver.find_elements(By.CLASS_NAME, "_abl_")[0]:
                            driver.find_elements(By.CLASS_NAME, "_abl_")[0].click()
                            print("post liké")
                            like = True
                            driver.find_element(By.CLASS_NAME, "futnfnd5").click()


                    except:
                        pass



Start()
Cookies()
Login(Username, Password)
Follow("https://www.instagram.com/instagram")
Like("https://www.instagram.com/instagram", [0, 3])
driver.close()
