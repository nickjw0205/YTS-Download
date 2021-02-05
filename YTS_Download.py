from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import youtube_dl
import os

# video title and link list
titles = []
links = []

# basic links for code
basic_link = 'https://www.youtube.com'
basic_search_link = 'https://www.youtube.com/results?search_query='

# input sequence
def search_word():
    input_word = input("search word: ")
    word = input_word.replace(" ", "+")
    search_link = basic_search_link+word

    return search_link

# open chrome tab and scroll it to load videos
def search_youtube(search):
    # location of chrome driver
    path = 'path'
    driver = webdriver.Chrome(executable_path=path)
    delay = 3
    driver.implicitly_wait(delay)
    driver.get(search)
    body = driver.find_element_by_tag_name('body')
    num_of_pagedowns = 10
    while num_of_pagedowns >= 0:
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        num_of_pagedowns -= 1
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    driver.close()

    return soup

# add video title and link to list
def search_titles(soup):
    for a in soup.find_all('a','yt-simple-endpoint style-scope ytd-video-renderer'):
        titles.append(a['title'])
        links.append(basic_link+a['href'])
    return titles, links

# print number of downloaded video
def print_list(titles, links):
    i = 0
    for title, link in zip(titles, links):
        print(title + ": " + link)
        i += 1
        print()
    print()
    print("-----------------------------")
    print("{0} videos will be downloaded".format(i))
    print("-----------------------------")
    print()

# download video
def download_videos(titles, links):
    output_dir = os.path.join('/videos', '%(title)s.%(ext)s')

    ydl_opt = {
        'outtmpl': output_dir,
        'format': 'bestvideo/best',
    }
    # dwonload video and print title
    for title, link in zip(titles,links):
        with youtube_dl.YoutubeDL(ydl_opt) as ydl:
            print(title)
            print(link)
            ydl.download([link])
    print('end sequence')

titles, links = search_titles(search_youtube(search_word()))
print_list(titles, links)
download_videos(titles, links)
