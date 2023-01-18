# 네이버 블로그 아이디 크롤링 - 개정, 웹사이트 ver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import csv
import pandas as pd
# 네이버 아이디 복붙용
import pyperclip

drive = webdriver.Chrome('chromedriver.exe')

# 블로그 아이디 링크를 저장하기 위한 빈 리스트
id_url_list = []
# 지정 키워드와 반복 페이지 숫자 - 원하는 키워드로 변경할 것
keyword = '후쿠오카'
repeatPages = 50

for i in range(1, repeatPages):
    # 페이지 이동
    web_url = f"https://section.blog.naver.com/Search/Post.naver?pageNo={i}&rangeType=ALL&orderBy=sim&keyword={keyword}"
    drive.get(web_url)

    id_url = drive.find_elements_by_class_name('thumbnail_post')
    for i in id_url:
        id_url_list.append(i.get_attribute('post-url'))
        drive.implicitly_wait(10)
    # time.sleep(1)
    drive.implicitly_wait(10)

data = pd.DataFrame(id_url_list)
# mode = a 를 추가해 기존에 있던 csv를 append, 즉 overwrite형식으로 변경
data.to_csv('naver.csv', mode='w', header=False, index=False)