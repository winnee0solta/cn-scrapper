'''
Author : Winnee Creztha
Desc   : scrapper for auto reaction 

CN Auto React random posts replies
uses account.json for login  
'''
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

#get account data
print("#############################################################################################")
print("#########################################account############################")
print("#############################################################################################")
 
account = {
    "email": "winneecreztha@gmail.com",
    "password": "9860988117",
    "username": "winnee"
}

loginurl = "https://cybernepal.com/login/"
# start driver
print('################################################################')
print('SYSTEM STARTED')
print('################################################################')
print('################################################################')
print('STARTING DRIVER')
print('################################################################')
which_browser = int(random.uniform(1, 3)) 
driver = webdriver.Chrome(
    executable_path='browserdrivers/chromedriver.exe')  
print('################################################################')
print('DRIVER STARTED WITHOUT ERROR')
print('################################################################')
print('################################################################')
print('OPENING URL =', loginurl)
print('################################################################')
driver.get(loginurl)
# delay
time.sleep(int(random.uniform(1, 5)))
driver.execute_script("window.scrollTo(0, (document.body.scrollHeight)/5);")
time.sleep(int(random.uniform(1, 5)))
driver.execute_script("window.scrollTo(0, (document.body.scrollHeight)/4);")
time.sleep(int(random.uniform(1, 5)))
driver.execute_script("window.scrollTo(0, (document.body.scrollHeight)/3);")
time.sleep(int(random.uniform(1, 5)))
# get html source from dom
html = driver.execute_script("return document.documentElement.outerHTML")
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


# target url
# use gaming discussion for now
url = "https://cybernepal.com/forums/gaming-discussion.33/"
print('################################################################')
print('OPENING URL =', url)
print('################################################################')


driver.get(url)
# get html source from dom
html = driver.execute_script("return document.documentElement.outerHTML")
# parse html
soup = BeautifulSoup(html, 'html.parser')
# for pagination
paginationdiv = soup.find("ul", {"class": "pageNav-main"})
lastpageindex = 0
tempcount = 0
for li in paginationdiv.findAll('li'):
    tempcount = tempcount + 1
    # print(li.a.get_text())
    if tempcount == 5:
        lastpageindex = int(li.a.get_text())
        pass

# last page index
while 1:
    posturls = []

    # get the each page posts urls
    index1 = 0
    while index1 < lastpageindex+1:
        # while index1 < 1:
        index1 = index1 + 1
        pageurl = 'https://cybernepal.com/forums/gaming-discussion.33/page-' + \
            str(index1)
        print('################################################################')
        print("#Opening url : ", pageurl,
              "#######################################")
        print('################################################################')

        #   open page
        driver.get(pageurl)
        html2 = driver.execute_script(
            "return document.documentElement.outerHTML")
        soup2 = BeautifulSoup(html2, 'html.parser')
        # time.sleep(10)
        # get all the posts urls
        mainpostdivs = soup2.findAll(
            "div", {"class": "structItem--thread"})
        loopcount = 0
        for singlediv in mainpostdivs:
            loopcount = loopcount + 1
            print(
                "#############################################################################################")
            print('loop no ', str(loopcount))
            print(
                "#############################################################################################")
            print('################################################################')
            print('SLEEP MODE ON FOR .300')
            print('################################################################')
            time.sleep(.300)
            # print(singlediv)
            # continue
            # get url if replies != 0
            # repliediv = singlediv.find(
            #     "div", {"class": "structItem-cell--meta"})
            # repliescount = int(repliediv.find(
            #     "dd").get_text())  # replies counter

            # if repliescount == 0 :
            #     continue
            # # print(repliediv.find("dd").get_text())
            # thread url
            urldiv = singlediv.find(
                "div", {"class": "structItem-title"})
            urlas = urldiv.findAll('a')
            # urla = urlas.next_sibling("a")

            if len(urlas) == 2:
                threadlink = "https://cybernepal.com"+urlas[1]['href']
                # add to list
                posturls.append(threadlink)
            elif len(urlas) == 1:
                # print(urlas[0]['href'])
                threadlink = "https://cybernepal.com"+urlas[0]['href']
                # add to list
                posturls.append(threadlink)

    #
    # Use the post links to react in random post
    # take random post each time
    # reach one reply then repeat
    #
    while 1:
        # loop 28 time then wait 3hr
        moneycounter = 0
        while moneycounter < 29:
            moneycounter = moneycounter + 1
            #
            # REACT
            #
            # select random post
            selectedposturl = random.choice(posturls)
            emo_val = [1, 4]
            emotoselect = random.choice(emo_val)
            # go to the url
            #   open page
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

            mainreplydivs = soup3.findAll(
                "article", {"class": "message--post"})
            print(
                "#############################################################################################")
            print('length of mainreplydivs', len(mainreplydivs))
            print(
                "#############################################################################################")

            indexcollection = []
            counter122 = 0
            while counter122 < len(mainreplydivs):
                indexcollection.append(counter122)
                counter122 = counter122 + 1

            chooser12 = random.choice(indexcollection)
            singlereplydiv = mainreplydivs[chooser12]
            #check if user is not winnee
            usernameh4 = singlereplydiv.find(
                "h4", {"class": "message-name"})
            print(
                "#############################################################################################")
            print("#########################################USERNAME CHECK#########################################")
            print(
                "#############################################################################################")
            username = usernameh4.a.text
            if username != account["username"]:
                #get reply url
                spanwithid = singlereplydiv.find(
                    "span", {"class": "u-anchorTarget"})
                idtoreact = spanwithid['id']
                temp_id = idtoreact.split('-')
                postid = int(temp_id[1])

                print('################################################################')
                print('SLEEP MODE ON FOR Random  SEC ')
                print('################################################################')
                time.sleep(int(random.uniform(10, 80)))
                # react page
                reactpageurl = 'https://cybernepal.com/posts/' + \
                    str(postid)+'/react?reaction_id='+str(emotoselect)
                driver.get(reactpageurl)
                time.sleep(int(random.uniform(1, 5)))
                driver.execute_script(
                    "window.scrollTo(0, (document.body.scrollHeight)/5);")
                time.sleep(int(random.uniform(1, 5)))
                driver.execute_script(
                    "window.scrollTo(0, (document.body.scrollHeight)/5);")
                time.sleep(int(random.uniform(1, 5)))

                html4 = driver.execute_script(
                    "return document.documentElement.outerHTML")
                soup4 = BeautifulSoup(html4, 'html.parser')
                # use the drive to confirm
                driver.find_element_by_css_selector(
                    '.button--icon--confirm').click()
                driver.get('https://cybernepal.com')
                #
                # maybe some delay
                #
                print(
                    "#############################################################################################")
                print(
                    "######################################### 29 sec Delay #########################################")
                print(
                    "#############################################################################################")
                time.sleep(int(random.uniform(10, 29)))
            #if ends for username

        # 15min delay
        print("#############################################################################################")
        print("#########################################random 100s delay#########################################")
        print("#############################################################################################")
        time.sleep(int(random.uniform(100, 329)))

# page url
