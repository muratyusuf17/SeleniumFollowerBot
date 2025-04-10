import time
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import random
import re
import pyperclip
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC

sendname=input("Enter target instagram account:")
username_list=["manipulasyonkulubu","gunes.gibi.biri17"]
chromedriver_autoinstaller.install()
tarayici=webdriver.Chrome()
def insta(username,password,sendname,atomic_origin_mail,atomic_origin_password):
    tarayici.get("https://www.instagram.com/")
    insta_mail = tarayici.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[1]/div/label/input')
    insta_mail.send_keys(username)
    insta_sifre=tarayici.find_element(By.XPATH,'//*[@id="loginForm"]/div[1]/div[2]/div/label/input')
    insta_sifre.send_keys(password)
    tarayici.find_element(By.XPATH,'//*[@id="loginForm"]/div[1]/div[3]').click()
    time.sleep(10)


    try:
        # URL'nin belirli kısmının içerip içermediğini kontrol et
        current_url = tarayici.current_url
        if "auth_platform/codeentry" in current_url:
            print("URL'nin gerekli kısmı bulundu. Yeni sekme açılıyor...")
            tarayici.execute_script("window.open('https://atomicmail.io/app/auth/sign-in', '_blank');")



            # Yeni sekmeye geçiş yapma
            tarayici.switch_to.window(tarayici.window_handles[1])


            # Yeni sekmede işlem yapma
            time.sleep(2)
            atomic_email=tarayici.find_element(By.NAME,"username")
            atomic_email.send_keys(atomic_origin_mail)
            time.sleep(3)
            tarayici.find_element(By.XPATH,'/html/body/main/div/div[2]/div/div[2]/div/div[2]/form/div/div[2]/button').click()
            atomic_password=tarayici.find_element(By.NAME,"password")
            atomic_password.send_keys(atomic_origin_password)
            time.sleep(3)
            tarayici.find_element(By.XPATH,'/html/body/main/div/div[2]/div/div[2]/div/div[2]/form/div/div[2]/button[2]').click()
            time.sleep(7)
            tarayici.get("https://atomicmail.io/app/mailbox")
            time.sleep(random.uniform(10,25))
            son_mail = tarayici.find_element(By.XPATH,'//*[@id="listItem-0"]/li[1]/div/div[2]/a/div/div[1]/div/p')
            son_mail.click()
            time.sleep(5)
            body_element = tarayici.find_element(By.TAG_NAME, "body")
            body_text = body_element.text
            # 6 haneli sayıyı bul
            for word in body_text.split():
                if len(word) == 6 and word.isdigit():
                    pyperclip.copy(word)  # Kodu kopyalar
                    print("Kod kopyalandı:", word)
                    break
            else:
                print("Kod bulunamadı.")




            time.sleep(5)

            # Sekmeyi kapatma
            tarayici.close()

            # Ana sekmeye geri dönme
            tarayici.switch_to.window(tarayici.window_handles[0])

            # Ana sekmede işlem yapma
            time.sleep(10)
            body_uc = tarayici.find_element('tag name', 'body')  # Sayfanın body elementini buluyoruz
            body_uc.send_keys(Keys.TAB * 4 + pyperclip.paste()+ Keys.ENTER)  # Tab tuşuna 3 kez basıyoruz
        else:
            print("URL beklenen formatta değil.")

    except Exception as e:
        print(f"Bir hata oluştu: {e}")


    time.sleep(random.uniform(10,15))
    tarayici.get("https://www.instagram.com/"+sendname +"/")
    try:
        # URL'nin belirli kısmının içerip içermediğini kontrol et
        current_url2 = tarayici.current_url
        if "https://www.instagram.com/consent/" in current_url2:
            print("cookie sekmesi bulundu")
            body4 = tarayici.find_element('tag name', 'body')  # Sayfanın body elementini buluyoruz
            body4.send_keys(Keys.TAB * 22 + Keys.ENTER)  # Tab tuşuna 3 kez basıyoruz
            time.sleep(10)
            tarayici.get("https://www.instagram.com/" + sendname + "/")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")
    time.sleep(random.uniform(3,15))
    body = tarayici.find_element('tag name', 'body')  # Sayfanın body elementini buluyoruz
    body.send_keys(Keys.TAB * 3 + Keys.ENTER)  # Tab tuşuna 3 kez basıyoruz
    time.sleep(random.randint(5,8))
    tarayici.get("https://www.instagram.com/accounts/logout")

#insta(username_list[0],"enterinstagram password",sendname,"atomic mail","atomic mail password")
#usernamelist.append("nickname")
#insta(username_list[1],"enterinstapassword",sendname,"atomic mail","atomic mail password")
time.sleep(3)
tarayici.quit()