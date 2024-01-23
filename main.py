from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

from time import sleep
from bs4 import BeautifulSoup 
import csv
# import config
# from telegram import Bot
import requests
import re
from lxml import etree



service = Service(executable_path=r'/usr/bin/chromedriver')
options = webdriver.ChromeOptions()
service = Service(executable_path=r'/usr/bin/chromedriver')
# options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=service, options=options)


def foodmaxx():
    # driver.get("https://foodmaxx.com/stores")
    # sleep(10)
    # input_element = driver.find_element("xpath",'//*[@id="place-search"]')
    # input_element.send_keys('Merced')
    # sleep(3)
    # input_element.send_keys(Keys.DOWN)
    # input_element.send_keys(Keys.RETURN)
    # sleep(10)
    # input_element = driver.find_element("xpath",'/html/body/div[1]/div[2]/div/main/section/div/div/div/div[2]/div[1]/div/div[1]/div/div/div[2]/button')
    # input_element.click()
    # sleep(5)
    # driver.get("https://foodmaxx.com/flyers/")
    # sleep(15)
    # html = driver.execute_script("return document.body.innerHTML")
    # print(html)
    # soup = BeautifulSoup(html, 'lxml')
    # dom = etree.HTML(str(soup))
    # print(dom.xpath('/html/body/flipp-router/flipp-publication-page/div/div[2]/flipp-sfml-component/sfml-storefront/div/sfml-linear-layout/sfml-flyer-image/div'))
    # # print(deals)
    headers = {
    'authority': 'dam.flippenterprise.net',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'if-none-match': 'W/"8d8d5d58f00b41f55f2222c480448f54"',
    'origin': 'https://foodmaxx.com',
    'referer': 'https://foodmaxx.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
}

    response = requests.get('https://dam.flippenterprise.net/flyerkit/publication/6227599/products?display_type=all&source=hosted2&locale=en&access_token=6253e7db4156b0fcf78ceaf133d4aab6', headers=headers)
    data = (response.json())
    for i in data:
        print(i['name']," ",i['price_text']," ",i['description']," ",i['post_price_text'])
            
foodmaxx()
