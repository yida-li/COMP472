####################################################
# 25. : Harvester X Extraction
####################################################
from warnings import warn
from time import time
from time import sleep
from random import randint
from IPython.core.display import clear_output
import pandas as pd
import requests
from requests import get
from bs4 import BeautifulSoup
languid = ('\n\n\n')


pages = [str(i) for i in range(1, 2)]
years_url = [str(i) for i in range(2017, 2018)]


names = []
years = []
imdb_ratings = []
metascores = []
votes = []
start_time = time()
requests = 0

for year_url in years_url:

    for page in pages:

        response = get('https://www.imdb.com/search/title?release_date=' + year_url +
                       '&sort=num_votes,desc&page=' + page)

        sleep(randint(1, 3))

        requests += 1
        elapsed_time = time() - start_time
        print('Request:{}; Frequency: {} requests/s'.format(requests,
              requests/elapsed_time))
        clear_output(wait=True)
        # Dont get ip banned
        if requests > 72:
            warn('Number of requests was greater than expected.')
            break
        page_html = BeautifulSoup(response.text, 'html.parser')
        mv_containers = page_html.find_all(
            'div', class_='lister-item mode-advanced')
        for container in mv_containers:
            if container.find('div', class_='ratings-metascore') is not None:
                name = container.h3.a.text
                names.append(name)
                year = container.h3.find(
                    'span', class_='lister-item-year').text
                years.append(year)
                imdb = float(container.strong.text)
                imdb_ratings.append(imdb)
                m_score = container.find('span', class_='metascore').text
                metascores.append(int(m_score))
                vote = container.find('span', attrs={'name': 'nv'})[
                    'data-value']
                votes.append(int(vote))


movie_ratings = pd.DataFrame({'movie': names,
                              'year': years,
                              'imdb': imdb_ratings,
                              'metascore': metascores,
                              'votes': votes
                              })


# rearrangement
movie_ratings = movie_ratings[['movie', 'year', 'imdb', 'metascore', 'votes']]
# conversion
movie_ratings.loc[:, 'year'] = movie_ratings['year'].str[-5:-1].astype(int)
# storage
movie_ratings.to_csv('data_set.csv')
