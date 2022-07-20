from urllib import response
from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/news')
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, 'html.parser')
article_tag = soup.find(name="a", class_="titlelink")
article_text = article_tag.getText()
article_link = article_tag.get("href")
article_upvote = soup.find(name='span', class_='score').getText()

print(article_text)
print(article_link)
print(article_upvote)











# with open('Day_1-Web-Scraping/website.html', encoding="utf8") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, 'html.parser')

# # print(soup.title.h1)

# # anchor_tags = soup.find_all(name='a')

# # print(anchor_tags)

# # for tag in anchor_tags:
# #     print(tag.getText())

# heading = soup.find(name='h1', id='name')
# # print(heading)

# section_heading = soup.find(name='h3', class_='heading')
# print(section_heading)

# # Seleting HTML Ids
# name = soup.select_one(selector='#name')
# print(name)

# #Seleting HTML Classes
# c = soup.select(".heading")
# print(c)