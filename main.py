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


def smartfinal():
    url = 'https://dam.flippenterprise.net/flyerkit/publication/6234203/products?display_type=all&source=hosted2&locale=en&access_token=0a290a2b3668a85e2d28efd6efd77383'

    headers = {
        'authority': 'dam.flippenterprise.net',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'if-none-match': 'W/"7d4a1a3643c6fce6f84f6fceee2e6013"',
        'origin': 'https://www.smartandfinal.com',
        'referer': 'https://www.smartandfinal.com/',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    }

    response = requests.get(url, headers=headers)
    data = response.json()
    for i in data:
        if i['price_text']!="":
            print(i['name']," ",i['price_text']," ",i['description'])
            print()
def raleys():
    driver.get("https://www.raleys.com/weekly-ad")
    sleep(15)
    # input_element = driver.find_element("xpath",'/html/body/div[4]/div/div[1]/header/nav/div/div[1]/div[2]/div[3]/div/div/div/div[2]/div[1]/p')
    # input_element.click()
    # sleep(10)
    # iframe = driver.find_element('xpath',"//iframe[contains(@id,'sp_message_iframe')]")
    # driver.switch_to().frame(iframe)

    # input_element = driver.find_element("xpath",'//*[@id=":r6:"]/div/div/div[2]/button[3]')
    # input_element.click()
    # sleep(2)
    # input_element = driver.find_element("xpath",'/html/body/div[4]/div/div[1]/header/div[2]/div/div/div[2]/div[1]/div/div/input')
    # input_element.send_keys("Merced")
    html = driver.page_source 
    soup = BeautifulSoup(html, "html.parser") 
    # print(soup.prettify())
    product_grid=soup.find('div', {'class': 'desktop:grid-cols-5'})
    srchProducts = soup.find_all('div', {'class' : 'flex flex-col gap-4 pb-16'}) + soup.find_all('div', {'class' : 'flex flex-col items-start gap-4 pb-16'})
    products=[]
    print(len(srchProducts))
    for n in range(len(srchProducts)):
        product={}
        if srchProducts[n].find('p', {'class' : 'desktop:h7'}) is not None:
            # print(srchProducts[n])
            product['name'] = srchProducts[n].find('p', {'class' : 'desktop:h7'}).text
            product['price'] = srchProducts[n].find('h6', {'class': 'desktop:h6'}).text
            # print(srchProducts[n].find('div', {'class': 'p6'}).text)
            if srchProducts[n].find('div', {'class': 'desktop:p6 p6 text-neutral-600'}) is not None:
                product['unitPrice'] = srchProducts[n].find('div', {'class': 'desktop:p6 p6 text-neutral-600'}).text
            products.append(product)

    print(products)
    print(len(products))

raleys()
# foodmaxx()
# smartfinal()
