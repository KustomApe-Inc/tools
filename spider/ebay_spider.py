import urllib.request
from bs4 import BeautifulSoup as bs
import csv

base_url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw='
request = str(input('キーワードを入力してください：'))
url_separator = '&_sacat=0&_pgn='
page_num = '1'
url = base_url + request + url_separator + page_num
html = urllib.request.urlopen(url).read()
soup = bs(html, 'html.parser')
num = 1

for i in range(1):
    url = base_url + request + url_separator + page_num
    for post in soup.findAll('li', {'class': 's-item'}):
        h = post.findAll('a', {'class': 's-item__link'})[0]
        imgH = post.findAll('img', {'class': 's-item__image-img'})[0]
        priceH = post.findAll('span', {'class': 's-item__price'})[0]
        title = h.text
        link = h['href']
        price = priceH.text
        image = imgH['src']
        print(title)
        print(link)
        print(price)
        print(image)
    if 'jpg' in image:
        image = image
    continue
    num += 1
    page_num = str(num)
    url = base_url + request + url_separator + page_num
    html = urllib.request.urlopen(url).read()
    soup = bs(html, 'html.parser')
    print('we are at page' + page_num)
print('finish scraping')
