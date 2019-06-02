import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import os
import shutil
import time
import random
import json
from requests import get


# target url 
url = "https://cybernepal.com/forums/contest-giveaways.4/"
# start driver
print('################################################################')
print('SYSTEM STARTED')
print('################################################################')
print('################################################################')
print('STARTING DRIVER')
print('################################################################') 
driver = webdriver.Firefox(executable_path='browserdrivers/geckodriver.exe')
# html = get(url)
print('################################################################')
print('DRIVER STARTED WITHOUT ERROR')
print('################################################################') 
print('################################################################')
print('OPENING URL =', url)
print('################################################################')  
driver.get(url)
# delay
print('################################################################')
print('SLEEP MODE ON FOR 60 SEC (LOGIN MODE ON)')
print('################################################################')
time.sleep(60)
driver.execute_script("window.scrollTo(0, (document.body.scrollHeight)/5);")
time.sleep(int(random.uniform(1, 5)))
driver.execute_script("window.scrollTo(0, (document.body.scrollHeight)/4);")
time.sleep(int(random.uniform(1, 5)))
driver.execute_script("window.scrollTo(0, (document.body.scrollHeight)/3);")
time.sleep(int(random.uniform(1, 5)))  
##########################
# get html source from dom
html = driver.execute_script("return document.documentElement.outerHTML")
# parse html
soup = BeautifulSoup(html, 'html.parser') 
posturls = []
mainpostdivs = soup.findAll(
    "div", {"class": "structItem--thread"})
loopcount = 0
for singlediv in mainpostdivs:
    loopcount = loopcount + 1
    print('################################################################')
    print('SN =', str(loopcount))
    print('################################################################') 
    time.sleep(int(random.uniform(1, 5)))
    urldiv = singlediv.find(
        "div", {"class": "structItem-title"})
    urlas = urldiv.findAll('a') 
    print('################################################################')
    print('RETRIVING URL FOR THE THREAD')
    print('################################################################') 
    
    if len(urlas) == 2: 
        threadlink = "https://cybernepal.com"+urlas[1]['href']
        print('################################################################')
        print('THREAD URL ',threadlink)
        print('################################################################') 
        # add to list
        posturls.append(threadlink)
    elif len(urlas) == 1: 
        threadlink = "https://cybernepal.com"+urlas[0]['href']
        print('################################################################')
        print('THREAD URL ',threadlink)
        print('################################################################') 
        # add to list
        posturls.append(threadlink)
 
print('################################################################')
print('THREAD COUNT = ', str(len(posturls)))
print('################################################################')

loopcounter = 0
while loopcounter < len(posturls):
    selectedposturl = posturls[loopcounter]
    print('################################################################')
    print('OPENING THREAD NO = ', str(loopcounter))
    print('THREAD URL = ', str(selectedposturl))
    print('################################################################')
    driver.get(selectedposturl)
    driver.execute_script(
        "window.scrollTo(0, (document.body.scrollHeight)/5);")
    time.sleep(int(random.uniform(1, 5)))
    driver.execute_script(
        "window.scrollTo(0, (document.body.scrollHeight)/5);")
    time.sleep(int(random.uniform(1, 5)))
    driver.execute_script(
        "window.scrollTo(0, (document.body.scrollHeight)/5);")
    time.sleep(int(random.uniform(1, 5)))


    html3 = driver.execute_script(
        "return document.documentElement.outerHTML")
    soup3 = BeautifulSoup(html3, 'html.parser')

    print('################################################################')
    print('SLEEP MODE ON FOR 104 SEC')
    print('################################################################')
    time.sleep(104)

    textbox = driver.find_element_by_xpath(
        ".//div[@class='fr-element fr-view']/p[1]")
    driver.execute_script(
        "arguments[0].textContent = arguments[1];", textbox, "Hip Hip Hurray !! I love CyberNepal :-* ")
    time.sleep(int(random.uniform(1, 5)))
    driver.execute_script(
        "window.scrollTo(0, (document.body.scrollHeight)/5);")
    time.sleep(int(random.uniform(1, 5)))
    driver.execute_script(
        "window.scrollTo(0, (document.body.scrollHeight)/5);")
    # send comment
    print('################################################################')
    print('SLEEP MODE ON FOR 149 SEC')
    print('################################################################')
    time.sleep(149)
    # click send btn
    # use the drive to confirm
    # TODO: button click didnt worked
    driver.find_element_by_css_selector(
        '.button--icon--reply').click()
    print('################################################################')
    print('SLEEP MODE ON FOR 1800 SEC (30MIN)')
    print('################################################################')
    time.sleep(1800) 
    loopcounter = loopcounter +1


print('################################################################')
print('PROGRAM TEMINATED WITHOUT ERROR')
print('################################################################')
