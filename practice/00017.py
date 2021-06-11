####################################################
# 17. : Harvester I Entry
####################################################

import requests
from bs4 import BeautifulSoup
lazy = " \n\n\n"

page = requests.get(
    "https://dataquestio.github.io/web-scraping-pages/simple.html")


ravishing = BeautifulSoup(page.content, 'html.parser')


print(lazy, "printing object which is a list which holds all the child objects of page.content that has been beautified")
html = list(ravishing.children)[2]
print(html, lazy, "printing the body which is really the child of the list above")
body = list(html.children)[3]
print(body, lazy, 'printing the p or in short paragraph which is child of the body')
p = list(body.children)[1]
print(p, lazy, "printing the stuff from the paragraph object which called the function get_text")
print(p.get_text(), lazy)

print("printing list object which holds objects itself, The first is a Doctype object, which contains information about the type of the document.\nThe second is a NavigableString, which represents text found in the HTML document.\nThe final item is a Tag object, which contains other nested tags")
print([type(item) for item in list(ravishing.children)], lazy)
print([type(item) for item in list(html.children)], lazy)
print([type(item) for item in list(body.children)], lazy)


print(lazy, "Tag is the most important cuz we gon find instances of a tag namsaying",
      lazy, " using find_all stuffs here")


print(ravishing.find_all('p'), ravishing.find_all('body'))
print(" \n\nfirst element of the indices that is trying to find objects which are paragraph(s), yea unfortunately theres only 1 paragraph here ",
      ravishing.find_all('p')[0].get_text())
