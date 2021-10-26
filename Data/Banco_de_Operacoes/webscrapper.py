import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import json
import re



def click_datapage(driver, i):
    try:
        driver.find_element_by_xpath(f"//main[@id='main-2']//section[@class='container']//div[@class='w-100 justify-center']//ul[@class='pagination mb-0']//li[@data-page='{i}']//a").click()
        time.sleep(1)
        print(f"\tClickando {i}")
    except:
        try:
            driver.find_element_by_xpath("//html//body[@class='main-nav-small']//div[@class='popup-fixed']//div[@class='container']//div[@class='advertising ad-846fdba2a96c4169a12391131693a3d8 mb-1']//div[@class='text-right']//button[@type='button']").click()  # //i[@class='material-icons']
            print("Anúncio Aberto")
            print("Anúncio Fechado")
            try:
                print("Outro Anúncio Aberto")
                driver.find_element_by_xpath(f"/html/body/div[1]/div[2]").click()
            except:
                print("Outro Anúncio Fechado")
            try:
                driver.find_element_by_xpath(
                    f"//main[@id='main-2']//section[@class='container']//div[@class='w-100 justify-center']//ul[@class='pagination mb-0']//li[@data-page='{i}']//a").click()
            except:
                return False
        except:
            try:
                print("Outro Anúncio Aberto")
                driver.find_element_by_xpath(f"/html/body/div[1]/div[2]").click()
            except:
                print("Outro Anúncio Fechado")
            try:
                driver.find_element_by_xpath(
                    f"//main[@id='main-2']//section[@class='container']//div[@class='w-100 justify-center']//ul[@class='pagination mb-0']//li[@data-page='{i}']//a").click()
            except:
                return False



def get_code(driver, codes):
    try:
        html_content = driver.find_element_by_xpath(f"/html/body/main/section[3]/div[2]")
        html_content = html_content.get_attribute("outerHTML")

        doc = BeautifulSoup(html_content, "html.parser")
        hrfs_finded = doc.find_all("a", class_="company card mt-0 mb-3 ml-1 mr-1 d-flex flex-column waves-effect")
        print(len(hrfs_finded)) # teste
        for i in hrfs_finded:  # para testes
            codes.append(i["href"][7:])
    except:
        return False



url = "https://statusinvest.com.br/acoes"
#https://statusinvest.com.br/acoes

option = Options()

option.headless = True
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get(url)

codes = []
print(codes)


for i in range(1, 26):
    # click_datapage(driver, i)
    # get_code(driver, codes)
    # time.sleep(1)
    valido_get_code = True
    valido_click_datapage = True

    valido_click_datapage = False if click_datapage(driver, i) == False else True
    valido_get_code = False if get_code(driver, codes) == False else True
    time.sleep(1)

    while valido_get_code == False or valido_click_datapage == False:
        valido_click_datapage = False if click_datapage(driver, i) == False else True
        valido_get_code = False if get_code(driver, codes) == False else True
        time.sleep(1)


print(codes)




# //main[@role="main", @d="main-2"]
#/html/body/main/section[3]/div[3]/ul/li[3]/a
# li.waves-effect.active
# a[@role="button"]





