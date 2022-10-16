import time
import string
from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from functools import reduce
driver = webdriver.Chrome(ChromeDriverManager().install())


def remove(string):
    return reduce(lambda x, y: (x + y) if (y != " ") else x, string, "")


f = open('problem_urls.txt', 'r')
f = open('problem_titles.txt', 'r')
urls = []
titles = []
with open('problem_titles.txt', 'r') as gt:
    titles = gt.readlines()
for title in titles:
    title = title.encode("utf-8")
    title = str(title)
    title = remove(title)

with open('problem_urls.txt') as ft:

    urls = ft.readlines()

    cnt = 251
    for url in urls:
        driver.get(url)
        cnt += 1
        time.sleep(5)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        problem_text = soup.find('div', {"class": "content__u3I1 question-content__JfgR"}).get_text()
        # print(problem_text)
        # problem_text = problem_text.encode("utf-8")
        # problem_text = str(problem_text)

        with open("problem_text_" + str(cnt) + ".txt", "w+", encoding="utf-8") as f:
            f.write(problem_text)
# # #


