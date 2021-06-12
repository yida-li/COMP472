from warnings import warn
from time import time
from time import sleep
from random import randint
from IPython.core.display import clear_output
import pandas as pd
import requests
from requests import get
from bs4 import BeautifulSoup
import re
lethargy = ('\n\n\n')
front = 'https://www.imdb.com/'
review = 'reviews/?ref_=tt_ql_urv'
seasons = [str(i) for i in range(1, 4)]
text = ''
index = 1
requests = 0
start_time = time()


episodeNames = []
episodeYear = []
TreasonSeason = []
reviews = []


for seasons in seasons:

    response = get(
        'https://www.imdb.com/title/tt0475784/episodes?season=' + seasons)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    sleep(randint(1, 3))

    requests += 1
    elapsed_time = time() - start_time
    print('Request:{}; Frequency: {} requests/s'.format(requests,
          requests/elapsed_time))

    # fetching the year
    episode_year = html_soup.find(
        'div', class_=['airdate'])

    year = episode_year.text.strip()[-4:]

    # fetching the episode name
    movie_containers = html_soup.find_all(
        'div', class_=['list_item even', 'list_item odd'])
    print(type(movie_containers))
    print(len(movie_containers))

    for i in range(len(movie_containers)):
        first_movie = movie_containers[i]
        temp = first_movie.strong
        for a in temp.find_all('a', href=True):
            linkName = front+a.get('href')+review
        episodeNames.append(first_movie.strong.a.text)
        episodeYear.append(year)
        TreasonSeason.append(seasons)
        reviews.append(linkName)

        text = text+" " + str(index) + " : " + first_movie.strong.a.text + \
            '\tSeason ' + seasons + '\t' + linkName + '\t' + str(year) + '\n'
        index = index+1  # index+=1


data_set = pd.DataFrame({'name': episodeNames,
                         'season': TreasonSeason,
                         'review link': reviews,
                         'year': episodeYear,

                         })
data_set.to_csv('data.csv')
