
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())

# driver.get("https://www.codechef.com/tags/problems/dynamic-programming")
#
# time.sleep(5)
# #
# html = driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
# all_ques_div = soup.findAll("div", {"class": "problem-tagbox-inner"})
# print(len(all_ques_div))
#
# all_ques = []
#
# for ques in all_ques_div:
#     all_ques.append(ques.findAll("div")[0].find("a"))
#
# # print(all_ques[10])
# urls = []
# titles = []
# for ques in all_ques:
#     urls.append("https://www.codechef.com"+ques['href'])
#     titles.append(ques.text)
#
# with open("problem_urls.txt", "w+") as f:
#     f.write('\n'.join(urls))
#
# with open("problem_titles.txt", "w+") as f:
#     f.write('\n'.join(titles))

# driver.get("https://www.codechef.com/problems/XYSTR")
# time.sleep(5)
# html = driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
#
# problem_text = soup.find('div', {"id": "problem-statement"}).text
# print(problem_text)



f = open('problem_urls.txt', 'r')
# f = open('problem_titles.txt', 'r')
urls = []
# titles = []
# with open('problem_titles.txt', 'r') as gt:
#     titles = gt.readlines()



with open('problem_urls.txt') as ft:

    urls = ft.readlines()

    cnt = 584
    for url in urls:
        driver.get(url)
        cnt += 1
        time.sleep(6)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        problem_text = soup.find('div', {"id": "problem-statement"}).get_text()
        # print(problem_text)
        problem_text = problem_text.encode("utf-8")
        problem_text = str(problem_text)

        with open("problem_codechef_dp" + str(cnt) + ".txt", "w+") as f:
            f.write(problem_text)

# urls = ["https://www.codechef.com/problems/XYSTR",
#         "https://www.codechef.com/problems/SUBINC"]
# cnt = 0
# for url in urls:
#     driver.get(url)
#     cnt += 1
#     time.sleep(5)
#     html = driver.page_source
#     soup = BeautifulSoup(html, 'html.parser')
#     problem_text = soup.find('div', {"id": "problem-statement"}).get_text()
#     # print(problem_text)
#     problem_text = problem_text.encode("utf-8")
#     problem_text = str(problem_text)
#
#     with open("problem" + str(cnt) + ".txt", "w+") as f:
#         f.write(problem_text)
