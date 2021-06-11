####################################################
# 23. : Harvester VII Scalar
####################################################
import requests
from requests import get
from bs4 import BeautifulSoup
lethargy = ('\n\n\n')
url = 'https://www.imdb.com/search/title?release_date=2017&sort=num_votes,desc&page=1'
response = get(url)
html_soup = BeautifulSoup(response.text, 'html.parser')

# Potentially CSS selector
movie_containers = html_soup.find_all(
    'div', class_='lister-item mode-advanced')
print(type(movie_containers))
print(len(movie_containers))


first_movie = movie_containers[0]


print(lethargy, first_movie.h3.a)
print(lethargy, first_movie.div)
print(lethargy, first_movie.a)
print(lethargy, first_movie.h3)
print(lethargy, "finally isolated wolverine!", first_movie.h3.a.text)


print(lethargy, " finaly found the year ", first_movie.h3.find(
    'span', class_='lister-item-year text-muted unbold').text)

print(lethargy, " finaly found rating ", float(first_movie.strong.text))

print(lethargy, " finaly found power chart ", int(
    first_movie.find('span', class_='metascore favorable').text))

print(lethargy, " finaly found how many minions ",
      int(first_movie.find('span', attrs={'name': 'nv'})['data-value']))
