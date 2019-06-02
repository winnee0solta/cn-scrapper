import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import os
import shutil
import time
import random
import json
from requests import get

print('################################################################')
print('PROGRAM STARTED')
print('################################################################')

while 1:
    #get account data
    print("#############################################################################################")
    print("#########################################LOADING accounts.json############################")
    print("#############################################################################################")
    # with open('accounts.json') as f:
    #     data = json.load(f)
    data = {"accounts": [{"email": "shresthaalu@gmail.com",  "password": "9860988117"}]}
    for account in data['accounts']:
        # print(account['email'])
        # print(account['password'])
        # target url
        loginurl = "https://cybernepal.com/login/"
        # start driver
        print('################################################################')
        print('SYSTEM STARTED')
        print('################################################################')
        print('################################################################')
        print('STARTING DRIVER')
        print('################################################################')
        driver = webdriver.Firefox(
            executable_path='browserdrivers/geckodriver.exe')
        print('################################################################')
        print('DRIVER STARTED WITHOUT ERROR')
        print('################################################################')
        print('################################################################')
        print('OPENING URL =', loginurl)
        print('################################################################')
        driver.get(loginurl)
        # delay
        time.sleep(int(random.uniform(1, 5)))
        driver.execute_script(
            "window.scrollTo(0, (document.body.scrollHeight)/5);")
        time.sleep(int(random.uniform(1, 5)))
        driver.execute_script(
            "window.scrollTo(0, (document.body.scrollHeight)/4);")
        time.sleep(int(random.uniform(1, 5)))
        driver.execute_script(
            "window.scrollTo(0, (document.body.scrollHeight)/3);")
        time.sleep(int(random.uniform(1, 5)))
        # get html source from dom
        html = driver.execute_script(
            "return document.documentElement.outerHTML")
        # parse html
        soup = BeautifulSoup(html, 'html.parser')
        print('################################################################')
        print('LOGGING IN')
        print('################################################################')
        username_text_area = driver.find_element_by_name('login')
        username_text_area.send_keys(account['email'])
        print('################################################################')
        print('EMAIL', str(account['email']))
        print('################################################################')
        username_text_area = driver.find_element_by_name('password')
        username_text_area.send_keys(account['password'])
        print('################################################################')
        print('PASSWORD', str(account['password']))
        print('################################################################')
        driver.find_element_by_css_selector(
            '.button--icon--login').click()
        print('################################################################')
        print('OPENING WINNEE KO ACCOUNT')
        print('################################################################')
        winnee_account_url = 'https://cybernepal.com/members/winnee.3342/#latest-activity'
        # TODO:    Testing in someone else
        # winnee_account_url = 'https://cybernepal.com/members/sumison360.341/#latest-activity'
        print('################################################################')
        print('OPENING URL =', winnee_account_url)
        print('################################################################')
        driver.get(winnee_account_url)
        print('################################################################')
        print('LOADING PAGE')
        print('################################################################')
        time.sleep(int(random.uniform(4, 10)))
        #click button untill full history loaded (pagination)
        #check if button is present

        show_older_item = 1
        temp_counter = 1
        while show_older_item:
            try:
                time.sleep(4)
                # Scroll down to bottom
                driver.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight);")
                driver.find_element_by_link_text(
                    'Show older items').click()
                time.sleep(5)
                # Scroll down to bottom
                driver.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(3)
                show_older_item = 1
                print('################################################################')
                print(temp_counter)
                print('################################################################')
            except NoSuchElementException:
                show_older_item = 0
            temp_counter = temp_counter + 1
        #show_older_item while ends

        print('################################################################')
        print('All OLD POST LOADED')
        print('################################################################')
        # get html source from dom
        html = driver.execute_script(
            "return document.documentElement.outerHTML")
        # parse html
        soup = BeautifulSoup(html, 'html.parser')
        main_activity_rows = soup.findAll(
            "li", {"class": "block-row--separated"})
        print("#############################################################################################")
        print('TOTAL ACTIVITIES', len(main_activity_rows))
        print("#############################################################################################")
        loopcount = 0
        random.shuffle(main_activity_rows)
        random.shuffle(main_activity_rows)
        random.shuffle(main_activity_rows)
        for single_activity_row in main_activity_rows:
            loopcount = loopcount + 1
            print('################################################################')
            print('Row No =', str(loopcount))
            print('################################################################')
            #check if activity is for replied
            activity_row_title = single_activity_row.find(
                "div", {"class": "contentRow-title"}).text
            if "replied" in activity_row_title:
                urldiv = single_activity_row.find(
                    "div", {"class": "contentRow-title"})
                urlas = urldiv.findAll('a')
                #get thread post id
                temp_thread_url = urlas[1]['href']
                temp_id = temp_thread_url.split('/')
                thread_id = int(temp_id[2])
                thread_url = 'https://cybernepal.com'+urlas[1]['href']
                #go to post
                print(
                    "#############################################################################################")
                print(
                    "#########################################SLEEP (300, 600) sec #########################################")
                print(
                    "#############################################################################################")
                time.sleep(int(random.uniform(300, 600)))
                print('################################################################')
                print('OPENING URL =', thread_url)
                print('################################################################')
                driver.get(thread_url)
                time.sleep(int(random.uniform(4, 10)))
                # Scroll down to bottom
                driver.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(int(random.uniform(4, 10)))
                #react using id
                emo_val = [1, 3, 4, 5]
                emotoselect = random.choice(emo_val)
                react_page_url = 'https://cybernepal.com/posts/' + \
                    str(thread_id)+'/react?reaction_id='+str(emotoselect)
                print(
                    "#############################################################################################")
                print(
                    "#########################################SLEEP (300, 600) sec #########################################")
                print(
                    "#############################################################################################")
                time.sleep(int(random.uniform(300, 600)))
                print('################################################################')
                print('OPENING URL =', react_page_url)
                print('################################################################')
                driver.get(react_page_url)
                time.sleep(int(random.uniform(4, 10)))
                # Scroll down to bottom
                driver.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight);")
                # use the driver to confirm
                driver.find_element_by_class_name(
                    'button--icon--confirm').click()
                time.sleep(int(random.uniform(2, 5)))
                driver.get('https://cybernepal.com')
                time.sleep(int(random.uniform(4, 10)))
            #if "replied" in activity_row_title: ENDS
        #for loop single_activity_row ends
    #go to home
    time.sleep(int(random.uniform(2, 5)))
    driver.get('https://cybernepal.com')
    time.sleep(int(random.uniform(100, 180)))
    #logout
    driver.find_element_by_link_text(
        'Log out').click()
    print("#############################################################################################")
    print(
        "#########################################SLEEP 30-60min #########################################")
    print(
        "#############################################################################################")
    time.sleep(int(random.uniform(1800, 3600)))
    #for loop for single login (for account in data['accounts'])

#first while ends
