from warnings import warn
from time import time
from time import sleep
from random import randint
from IPython.core.display import clear_output
import pandas as pd
import requests
from requests import get
from bs4 import BeautifulSoup
import csv
import re
import json
import math
lethargy = ('\n\n\n')
front = 'https://www.imdb.com/'
review = 'reviews/?ref_=tt_ql_urv'

# seasons  Ragen from 1 to x-1
seasons = [str(i) for i in range(1, 4)]
text = ''
index = 1
requests = 0
start_time = time()
whole_time = time()
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
front = 'https://www.imdb.com'
back = '?ref_=rw_urv'
string = ''
count = 0
negativeReviews = []
positiveReviews = []
requests = 0
start_time = time()
with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            line_count += 1
            ########################################################################################################

            # Extract Code here

            ########################################################################################################
            url = row[3]
            response = get(url+'&sort=userRating&dir=asc&ratingFilter=0')
            html_soup = BeautifulSoup(response.text, 'html.parser')
            requests += 1
            elapsed_time = time() - start_time
            sleep(randint(1, 3))
            print('Request:{}; Frequency: {} requests/s'.format(requests,
                                                                requests/elapsed_time))
            movie_containers = html_soup.find_all(
                'div', class_='lister-item mode-detail imdb-user-review collapsable')
            print(type(movie_containers))
            print(len(movie_containers))

            for i in range(len(movie_containers)):
                first_movie = movie_containers[i]
                temp = first_movie.find('div', class_='actions text-muted')

                Rating = first_movie.find(class_='ipl-ratings-bar')
                sleep(0.05)
                ExceptionHandler = Rating
                if ExceptionHandler is None:
                    print("Skipping this review, error detected")
                    continue
                ultimateExtraction = str(Rating.span.text)
                num_strs = re.findall('[0-9,]+', ultimateExtraction)
                numbers = [int(ns.replace(',', '')) for ns in num_strs]

                if numbers[0] >= 8:
                    positivity = True
                else:
                    positivity = False

                for a in temp.find_all('a', href=True):
                    linkName = a.get('href')
                    if linkName[3] != 'g':
                        string += front+linkName+'\n'

                        if positivity == False:
                            negativeReviews.append(front+linkName+back+'\n')
                        else:
                            positiveReviews.append(front+linkName+back+'\n')
                        count += 1

    print(f'Processed {line_count} lines.')

print(len(negativeReviews))
print(len(positiveReviews))

halfNegative = len(negativeReviews)/2
halfPositive = len(positiveReviews)/2


counterA = 0
counterB = 0
# with open('dataTrainingReviews.text', 'w') as f:
with open('training_data_set.txt', 'w') as f:

    for i in negativeReviews:
        if counterA < halfNegative:
            f.write(i)
        counterA += 1
    for i in positiveReviews:
        if counterB < halfPositive:
            f.write(i)
        counterB += 1


counterC = 0
counterD = 0
# with open('dataTestingReviews.text', 'w') as f:

with open('testing_data_set.txt', 'w') as f:

    for i in negativeReviews:
        if counterC > halfNegative:
            f.write(i)
        counterC += 1
    for i in positiveReviews:
        if counterD > halfPositive:
            f.write(i)
        counterD += 1

f.close()

sloth = "\n\n\n"
ultimateDictionary = {}
positivity = True
start_time = time()
requests = 0
with open('training_data_set.txt', 'r') as f2:
    for f3 in f2:

        response = get(
            f3.strip())
        requests += 1
        elapsed_time = time() - start_time
        sleep(randint(1, 2))
        print('Request:{}; Frequency: {} requests/s'.format(requests,
                                                            requests/elapsed_time))
        tomyum = BeautifulSoup(response.content, 'html.parser')
        Text = tomyum.find(class_='text show-more__control').text
        sleep(0.05)

        Rating = tomyum.find(class_='ipl-ratings-bar')
        sleep(0.05)
        ExceptionHandler = Rating
        if ExceptionHandler is None:
            print("Skipping this review, error detected")
            continue
        ultimateExtraction = str(Rating.span.text)
        num_strs = re.findall('[0-9,]+', ultimateExtraction)
        numbers = [int(ns.replace(',', '')) for ns in num_strs]

        if numbers[0] >= 8:
            positive = True
        else:
            positive = False
        result = re.sub(r'[^A-Za-z]', ' ', Text)
        print(sloth, f3, sloth)
        f1 = result.lower().split()

        for i in range(len(f1)):
            tempWord = f1[i]
            if tempWord in ultimateDictionary:
                if positive == True:
                    # dictionary { key, [#positive, #negative, #total]}     [0] = pos, [1]= neg ,[2]=sum
                    ultimateDictionary[tempWord][0] = ultimateDictionary[tempWord][0]+1
                    ultimateDictionary[tempWord][2] = ultimateDictionary[tempWord][2]+1
                else:
                    # or else update the dictionary and  [1]++   [2]++
                    ultimateDictionary[tempWord][1] = ultimateDictionary[tempWord][1]+1
                    ultimateDictionary[tempWord][2] = ultimateDictionary[tempWord][2]+1
            else:
                if positive == True:

                    ultimateDictionary.update({tempWord: [1, 0, 1]})
                else:
                    ultimateDictionary.update({tempWord: [1, 0, 1]})


with open('dictionaryReview.json', 'w') as json_file:
    json.dump(ultimateDictionary, json_file)
nn = '\n'

json_file.close()
####################################################
#
# Calculate how many different words there is,
# the total sum of all words in positive,
# total sum of all words in negative
####################################################


with open('dictionaryReview.json', 'r+') as Observer:
    ultimateDictionary = json.load(Observer)

#print(nn, "There is a total of :", len(ultimateDictionary))
#totalWordsInPositive = 0
#totalWordsInNegative = 0
# for key in ultimateDictionary:
#    totalWordsInPositive += ultimateDictionary[key][0]
#    totalWordsInNegative += ultimateDictionary[key][1]
#print(nn, 'total pos', totalWordsInPositive)
#print(nn, 'total neg', totalWordsInNegative)


####################################################
#
# Smoothen by delta = 1
####################################################

totalWordsInPositive = 0
totalWordsInNegative = 0

for key in ultimateDictionary:
    ultimateDictionary[key][0] += 1
    ultimateDictionary[key][1] += 1
    ultimateDictionary[key][2] += 2
    totalWordsInPositive += ultimateDictionary[key][0]
    totalWordsInNegative += ultimateDictionary[key][1]


print(nn, 'total pos after smoothening', totalWordsInPositive)
print(nn, 'total neg after smoothening', totalWordsInNegative)

Positive = 75
Negative = 115

ProbablityPositive = 75/(75+115)
ProbablityNegative = 115/(75+115)

# model1 for txt format
# model2 for json format
model = ''
model2 = {}


count = 1
for key in ultimateDictionary:
    model += 'No.'+str(count)+' ' + key+'\n'
    model += str(ultimateDictionary[key][0]) + ', ' + \
        str(ultimateDictionary[key][0]/totalWordsInPositive)+', '
    model += str(ultimateDictionary[key][1]) + ', ' + \
        str(ultimateDictionary[key][1]/totalWordsInNegative)+'\n'
    model2.update({key: [ultimateDictionary[key][0], round((ultimateDictionary[key][0]/totalWordsInPositive), 6),
                  ultimateDictionary[key][1], round((ultimateDictionary[key][1]/totalWordsInNegative), 6)]})
    count += 1

with open('model.txt', 'w') as f:

    for i in model:
        f.write(i)

# open hash if file needed again
#
with open('model2.json', 'w') as json_file:
    json.dump(model2, json_file)


# open hash if file needed again
#
with open('dictionaryReviewSmoothen.json', 'w') as json_file:
    json.dump(ultimateDictionary, json_file)

json_file.close()
f.close()
Observer.close()
sloth = "\n\n\n"
resultAnswer = ''
counter = 1
predictionCorrectness = 0
positivity = True
start_time = time()
requests = 0

with open('model2.json', 'r+') as Observer:
    model2 = json.load(Observer)

with open('testing_data_set.txt', 'r') as f2:
    for f3 in f2:

        response = get(
            f3.strip())
        requests += 1
        elapsed_time = time() - start_time
        sleep(randint(1, 2))
        print('Request:{}; Frequency: {} requests/s'.format(requests,
                                                            requests/elapsed_time))
        tomyum = BeautifulSoup(response.content, 'html.parser')
        Text = tomyum.find(class_='text show-more__control').text
        sleep(0.05)

        Rating = tomyum.find(class_='ipl-ratings-bar')
        sleep(0.05)
        ExceptionHandler = Rating
        if ExceptionHandler is None:
            print("Skipping this review, error detected")
            continue
        ultimateExtraction = str(Rating.span.text)
        num_strs = re.findall('[0-9,]+', ultimateExtraction)
        numbers = [int(ns.replace(',', '')) for ns in num_strs]

        if numbers[0] >= 8:
            positivity = "positive"
        else:
            positivity = "negative"
        result = re.sub(r'[^A-Za-z]', ' ', Text)
        f1 = result.lower().split()

        ProbabilityForTruth = math.log10(75/(75+115))
        ProbabilityForFalse = math.log10(115/(75+115))

        #
        # format of model2.json for each word
        # freq in pos , conditional probability of pos , freq in neg, conditional probability in neg
        # [0]                      [1]                       [2]                [3]

        for i in range(len(f1)):
            tempWord = f1[i]
            if tempWord in model2:
                ProbabilityForTruth += math.log10(model2[tempWord][1])
                ProbabilityForFalse += math.log10(model2[tempWord][3])

        if ProbabilityForTruth > ProbabilityForFalse:
            if positivity == 'positive':
                resultAnswer += 'Review No.'+str(counter)+' '+str(ProbabilityForTruth)+' '+str(
                    ProbabilityForFalse)+' positive '+positivity+' correct\n'
                predictionCorrectness += 1
            else:
                resultAnswer += 'Review No.'+str(counter)+' '+str(ProbabilityForTruth)+' '+str(
                    ProbabilityForFalse)+' positive '+positivity+' incorrect\n'
        else:  # probably false
            if positivity == 'positive':
                resultAnswer += 'Review No.'+str(counter)+' '+str(ProbabilityForTruth)+' '+str(
                    ProbabilityForFalse)+' negative '+positivity+' incorrect\n'

            else:
                resultAnswer += 'Review No.'+str(counter)+' '+str(ProbabilityForTruth)+' '+str(
                    ProbabilityForFalse)+' negative '+positivity+' correct\n'
                predictionCorrectness += 1
        counter += 1

resultAnswer += 'The prediction correctness is ' + \
    str((predictionCorrectness/counter)*100)+'%'

with open('result.txt', 'w') as f:

    for i in resultAnswer:
        f.write(i)

f.close()
