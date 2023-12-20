import requests as rq
import pandas as pd
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from lxml import etree
import time

# get player name
def get_player_name():
    player_list = []
    player = sp.find_all(class_ = 'full-3fV3c9pF')
    for i in range(0, len(player), 2):
        player_list.append(player[i].text + ' ' + player[i+1].text)
    return player_list

# get player's position
def get_player_position():
    position_list = []
    position = sp.find_all(class_ = 'position-28TbwVOg')
    for i in position:
        position_list.append(i.text)
    return position_list

def get_column_name():
    click_standard_button()
    sp = soup(driver.page_source, 'lxml')
    
    data_column_name = ['PLAYER', 'POSITION', 'TEAM']
    temp = sp.find_all(class_ = 'bui-text cellheader bui-text')
    for i in range(4, len(temp), 2):
        data_column_name.append(temp[i].text)
    temp = sp.find_all(class_ = 'bui-text cellheader selected-1vxxHvFg bui-text')
    for i in range(0, len(temp), 2):
        data_column_name.append(temp[i].text)

    click_expanded_button()
    sp = soup(driver.page_source, 'lxml')
    temp = sp.find_all(class_ = 'bui-text cellheader bui-text')
    for i in range(4, len(temp), 2):
        data_column_name.append(temp[i].text)
        
    return data_column_name

# click standard button
def click_standard_button():
    time.sleep(3)
    driver.find_element('xpath', '//*[@id="stats-app-root"]/section/section/div[1]/div[2]/div/div[1]/div/div[1]/button').click()
    driver.find_element('xpath', '//*[@id="stats-app-root"]/section/section/div[1]/div[2]/div/div[1]/div/div[1]/button').click()
    time.sleep(3)
    sp = soup(driver.page_source, 'lxml')

# click expanded button
def click_expanded_button():
    time.sleep(3)
    driver.find_element('xpath', '//*[@id="stats-app-root"]/section/section/div[1]/div[2]/div/div[1]/div/div[2]/button').click()
    driver.find_element('xpath', '//*[@id="stats-app-root"]/section/section/div[1]/div[2]/div/div[1]/div/div[2]/button').click()
    time.sleep(3)

# click next page button
def click_next_page_button():
    time.sleep(3)
    driver.find_element('xpath', '//*[@id="stats-app-root"]/section/section/div[3]/div[2]/div/div/div[2]/button').click()
    time.sleep(3)
    sp = soup(driver.page_source, 'lxml')

# get standard data
def get_data():
    data = []
    
    click_standard_button()
    sp = soup(driver.page_source, 'lxml')
    standard_data = []
    tt = sp.select('#stats-app-root tr td')
    for i in tt:
        standard_data.append(i.text)
    
    click_expanded_button()
    sp = soup(driver.page_source, 'lxml')
    expanded_data = []
    tt = sp.select('#stats-app-root tr td')
    for i in tt:
        expanded_data.append(i.text)

    for i in range(len(standard_data)//17):
        data.extend(standard_data[i*17:i*17+17])
        data.extend(expanded_data[i*16+1:i*16+16])

    return data

def run(link, year):
    try:
        df_list = []
        while True:
            sp = soup(driver.page_source, 'lxml')
            print('page start')
            time.sleep(2)
            name = get_player_name()
            time.sleep(2)
            position = get_player_position()
            time.sleep(2)
            current_data = get_data()
            time.sleep(2)
            for i in range(len(name)):
                row = []
                row.append(name[i])
                row.append(position[i])
                row.extend(current_data[i*32:i*32+32])
                df_list.append(row)
            click_next_page_button()
    except:
        df = pd.DataFrame(df_list, columns=get_column_name())
        df.to_csv(f'mlb_stats/{link[26:-1]}_{year}.csv', index=False, encoding='utf-8')
        print('This is the last page :)')

urls = pd.read_csv('mlb_stats_urls.csv', encoding='utf-8')

for year in range(2013, 2024):
    for link in urls['link']:
        url = link + str(year) + '?playerPool=ALL'
        driver = webdriver.Chrome('/programing/swiftx/chromedriver-win64/chromedriver.exe')
        html = driver.get(url)
        sp = soup(driver.page_source, 'lxml')

        run(link, year)

driver.quit()