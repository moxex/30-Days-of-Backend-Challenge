from bs4 import BeautifulSoup

with open('Day_1-Web-Scraping/website.html', encoding="utf8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')

print(soup.title.string)