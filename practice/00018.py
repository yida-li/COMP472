####################################################
# 18. : Harvester II Appetizer
####################################################

import requests
from bs4 import BeautifulSoup
bum = " \n\n\n"
page = requests.get(
    "https://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
stunning = BeautifulSoup(page.content, 'html.parser')

print(stunning)


print(bum, "Now, he is using the find_all method to search for items by class or by id. In the below example, we’ll search for any p tag that has the class outer-text", bum)
print(stunning.find_all('p', class_='outer-text'))

print(bum, 'find all class= outer-text')
print(stunning.find_all(class_="outer-text"))
print("yea they are the same but what can you do, gotta think outside the box and assume the obvious and take the laziest way of thinking", bum)

print("finding  all id = first")
print(stunning.find_all(id="first"))


print(bum, "Now a mega hard example, CSS selectors: find all p tags inside a div")
print(stunning.select("div p"))
