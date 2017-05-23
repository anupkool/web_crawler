import requests
from bs4 import BeautifulSoup
import _json
def search_spider(url):
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html5lib")

        for link in soup.find_all('div', {'class': 'product-desc-rating'}):
            href = link.find('a').get('href')
            #print(link)
            fetchname(href)
            print(href)
            fetchcost(href)
            fetchrate(href)
            fetchdesc(href)

def fetchname(url):
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html5lib")
    links = soup.find('span', {'class': 'active-bread'})
    print('Product Name:', links.string)

def fetchcost(url):
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html5lib")
    links = soup.find('span', {'class': 'pdp-final-price'})
    print(links.text)

def fetchrate(url):
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html5lib")
    links = soup.find('span', {'class': 'avrg-rating'}) or soup.find('div', {'class': 'pdp-e-i-ratings'})
    print(links.string)

def fetchdesc(url):
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html5lib")
    links = soup.find('span', {'class': 'h-content'})
    print(links.string)


search_spider('https://www.snapdeal.com/search?clickSrc=top_searches&keyword=bluetooth%20speakers&categoryId=0&vertical=p&noOfResults=20&SRPID=topsearch&sort=rlvncy')