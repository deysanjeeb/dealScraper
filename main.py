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


service = Service(executable_path=r'/usr/bin/chromedriver')
options = webdriver.ChromeOptions()
service = Service(executable_path=r'/usr/bin/chromedriver')
# options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=service, options=options)


def foodmaxx():
    driver.get("https://foodmaxx.com/stores")
    sleep(10)
    input_element = driver.find_element("xpath",'//*[@id="place-search"]')
    input_element.send_keys('Merced')
    sleep(3)
    input_element.send_keys(Keys.DOWN)
    input_element.send_keys(Keys.RETURN)
    sleep(10)
    input_element = driver.find_element("xpath",'/html/body/div[1]/div[2]/div/main/section/div/div/div/div[2]/div[1]/div/div[1]/div/div/div[2]/button')
    input_element.click()
    sleep(5)
    driver.get("https://foodmaxx.com/flyers/")
    sleep(15)
    # html = driver.page_source 
    # soup = BeautifulSoup(html, "html.parser") 
    # /html/body/flipp-router/flipp-publication-page/div/div[2]/flipp-sfml-component/sfml-storefront/div/sfml-linear-layout/sfml-flyer-image/div

foodmaxx()
