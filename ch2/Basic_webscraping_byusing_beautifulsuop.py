# Various ways to scrape the page here I'm using my own blog pages.

import requests
from bs4 import BeautifulSoup


def Get_the_page_by_beautibulsoup():
    page = requests.get("https://simplifydatascience.wordpress.com/about/")
    #print page.status_code
    #print page.content
    soup = BeautifulSoup(page.content, 'html.parser')
    #print soup()
    #print(soup.prettify()) #display source of the html page in readable format.
    soup = BeautifulSoup(page.content, 'html.parser')
    print soup.find_all('p')[0].get_text()
    print soup.find_all('p')[1].get_text()
    print soup.find_all('p')[2].get_text()
    print soup.find_all('p')[3].get_text()


if __name__ =="__main__":
    Get_the_page_by_beautibulsoup()
