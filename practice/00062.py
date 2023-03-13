from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
url = "https://prices.runescape.wiki/osrs/item/1998"
driver.get(url)

# Use Beautiful Soup to parse the HTML content of the page
soup = BeautifulSoup(driver.page_source, 'html.parser')
search=soup.find('span', class_='wgl-item-price')
price=search.text[0:5].replace(",", "")
#print(ye)
if type(price) is int:
    print(int((price)))

driver.quit()