from typing import Text
import matplotlib.pyplot as plt
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
import matplotlib.pyplot as plt
import numpy as np
import sys

import pygame


def Analysis():

    front = 'https://www.imdb.com/'
    review = 'reviews/?ref_=tt_ql_urv'

    print('Search for your favorite tv show and get the title and the title number of the show \n')
    titleLink = input(
        'Please copy paste the FULL LINK format, ( exmaple: https://www.imdb.com/title/tt0903747/ )\n:')
    numberOfS = int(input(
        'Please enter the CORRECT amount of seasons you would like to apply machine learning on:\n'))

    # seasons  Ragen from 1 to x-1
    seasons = [str(i) for i in range(1, numberOfS+1)]
    text = ''
    index = 1
    requests = 0
    episodeNames = []
    episodeYear = []
    TreasonSeason = []
    reviews = []

    for seasons in seasons:

        response = get(
            titleLink+'episodes?season=' + seasons)
        html_soup = BeautifulSoup(response.text, 'html.parser')
        episode_year = html_soup.find(
            'div', class_=['airdate'])
        year = episode_year.text.strip()[-4:]
        movie_containers = html_soup.find_all(
            'div', class_=['list_item even', 'list_item odd'])
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
                '\tSeason ' + seasons + '\t' + \
                linkName + '\t' + str(year) + '\n'
            index = index+1  # index+=1

    data_set = pd.DataFrame({'name': episodeNames,
                            'season': TreasonSeason,
                             'review link': reviews,
                             'year': episodeYear,

                             })
    data_set.to_csv('data.csv')
    print('\nData cvs file generated\n')

    front = 'https://www.imdb.com'
    back = '?ref_=rw_urv'
    string = ''
    count = 0
    negativeReviews = []
    positiveReviews = []
    requests = 0

    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                line_count += 1
                url = row[3]
                response = get(url+'&sort=userRating&dir=asc&ratingFilter=0')
                html_soup = BeautifulSoup(response.text, 'html.parser')
                requests += 1
                movie_containers = html_soup.find_all(
                    'div', class_='lister-item mode-detail imdb-user-review collapsable')

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
                                negativeReviews.append(
                                    front+linkName+back+'\n')
                            else:
                                positiveReviews.append(
                                    front+linkName+back+'\n')
                            count += 1

    print('\nThe total amount of negatives reviews collected: ', len(negativeReviews))
    print('\nThe total amount of positive reviews collected:', len(positiveReviews))

    halfNegative = len(negativeReviews)/2
    halfPositive = len(positiveReviews)/2
    print(halfNegative,
          'amount of negative reviews will be used for the training data set and testing data set')
    print(halfPositive,
          'amount of negative reviews will be used for the training data set and testing data set')

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

    print('\nData sets generated')

    ultimateDictionary = {}
    positivity = True

    requests = 0
    with open('training_data_set.txt', 'r') as f2:
        for f3 in f2:

            response = get(
                f3.strip())
            requests += 1
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

    totalWordsInPositive = 0
    totalWordsInNegative = 0

    for key in ultimateDictionary:
        ultimateDictionary[key][0] += 1
        ultimateDictionary[key][1] += 1
        ultimateDictionary[key][2] += 2
        totalWordsInPositive += ultimateDictionary[key][0]
        totalWordsInNegative += ultimateDictionary[key][1]

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

    print('\nmodel.text generated')

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
    resultAnswer = ''
    counter = 1
    predictionCorrectness = 0
    positivity = True

    requests = 0

    with open('model2.json', 'r+') as Observer:
        model2 = json.load(Observer)

    with open('testing_data_set.txt', 'r') as f2:
        for f3 in f2:

            response = get(
                f3.strip())
            requests += 1
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

    r0 = round((predictionCorrectness/counter)*100)

    with open('result.txt', 'w') as f:

        for i in resultAnswer:
            f.write(i)

    f.close()
    print('\nresults.text generated')

    ultimateDictionary = {}
    positivity = True

    requests = 0
    with open('training_data_set.txt', 'r') as f2:
        for f3 in f2:

            response = get(
                f3.strip())
            requests += 1
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

            f1 = result.lower().split()

            for i in range(len(f1)):
                tempWord = f1[i]
                if len(tempWord) >= 3:
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

    with open('lengthfiltering/length-resultMin3Dictionary.json', 'w') as json_file:
        json.dump(ultimateDictionary, json_file)

    ultimateDictionary = {}
    positivity = True

    requests = 0
    with open('training_data_set.txt', 'r') as f2:
        for f3 in f2:

            response = get(
                f3.strip())
            requests += 1
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

            f1 = result.lower().split()

            for i in range(len(f1)):
                tempWord = f1[i]
                if len(tempWord) >= 5:
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

    with open('lengthfiltering/length-resultMin5Dictionary.json', 'w') as json_file:
        json.dump(ultimateDictionary, json_file)

    ultimateDictionary = {}
    positivity = True

    requests = 0
    with open('training_data_set.txt', 'r') as f2:
        for f3 in f2:

            response = get(
                f3.strip())
            requests += 1
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

            f1 = result.lower().split()

            for i in range(len(f1)):
                tempWord = f1[i]
                if len(tempWord) >= 5 and len(tempWord) <= 9:
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

    with open('lengthfiltering/length-resultMax9Dictionary.json', 'w') as json_file:
        json.dump(ultimateDictionary, json_file)

    nn = '\n'

    with open('lengthfiltering/length-resultMin3Dictionary.json', 'r+') as Observer:
        ultimateDictionary = json.load(Observer)

    totalWordsInPositive = 0
    totalWordsInNegative = 0

    for key in ultimateDictionary:
        ultimateDictionary[key][0] += 1
        ultimateDictionary[key][1] += 1
        ultimateDictionary[key][2] += 2
        totalWordsInPositive += ultimateDictionary[key][0]
        totalWordsInNegative += ultimateDictionary[key][1]

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

    # open hash if file needed again
    #
    with open('lengthfiltering/length3Min-model2.json', 'w') as json_file:
        json.dump(model2, json_file)

    f.close()
    Observer.close()

    ###################################################################################

    with open('lengthfiltering/length-resultMin5Dictionary.json', 'r+') as Observer:
        ultimateDictionary = json.load(Observer)

    totalWordsInPositive = 0
    totalWordsInNegative = 0

    for key in ultimateDictionary:
        ultimateDictionary[key][0] += 1
        ultimateDictionary[key][1] += 1
        ultimateDictionary[key][2] += 2
        totalWordsInPositive += ultimateDictionary[key][0]
        totalWordsInNegative += ultimateDictionary[key][1]

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

    # open hash if file needed again
    #
    with open('lengthfiltering/length5Min-model2.json', 'w') as json_file:
        json.dump(model2, json_file)

    f.close()
    Observer.close()

    ###################################################################################

    with open('lengthfiltering/length-resultMax9Dictionary.json', 'r+') as Observer:
        ultimateDictionary = json.load(Observer)

    totalWordsInPositive = 0
    totalWordsInNegative = 0

    for key in ultimateDictionary:
        ultimateDictionary[key][0] += 1
        ultimateDictionary[key][1] += 1
        ultimateDictionary[key][2] += 2
        totalWordsInPositive += ultimateDictionary[key][0]
        totalWordsInNegative += ultimateDictionary[key][1]

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

    with open('lengthfiltering/length-model.txt', 'w') as f:

        for i in model:
            f.write(i)
    print('\nlength-model.txt  generated')

    # open hash if file needed again
    #
    with open('lengthfiltering/length9Max-model2.json', 'w') as json_file:
        json.dump(model2, json_file)

    f.close()
    Observer.close()

    resultAnswer = ''
    counter = 1
    predictionCorrectness = 0
    positivity = True

    requests = 0

    with open('lengthfiltering/length3Min-model2.json', 'r+') as Observer:
        model2 = json.load(Observer)

    with open('testing_data_set.txt', 'r') as f2:
        for f3 in f2:

            response = get(
                f3.strip())
            requests += 1

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

    l1 = round((predictionCorrectness/counter)*100)

    Observer.close()
    f.close()
    f2.close()

    ####################################################################################

    resultAnswer2 = ''
    counter = 1
    predictionCorrectness = 0
    positivity = True

    requests = 0

    with open('lengthfiltering/length5Min-model2.json', 'r+') as Observer:
        model2 = json.load(Observer)

    with open('testing_data_set.txt', 'r') as f2:
        for f3 in f2:

            response = get(
                f3.strip())
            requests += 1
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
                    resultAnswer2 += 'Review No.'+str(counter)+' '+str(ProbabilityForTruth)+' '+str(
                        ProbabilityForFalse)+' positive '+positivity+' correct\n'
                    predictionCorrectness += 1
                else:
                    resultAnswer2 += 'Review No.'+str(counter)+' '+str(ProbabilityForTruth)+' '+str(
                        ProbabilityForFalse)+' positive '+positivity+' incorrect\n'
            else:  # probably false
                if positivity == 'positive':
                    resultAnswer2 += 'Review No.'+str(counter)+' '+str(ProbabilityForTruth)+' '+str(
                        ProbabilityForFalse)+' negative '+positivity+' incorrect\n'
                else:
                    resultAnswer2 += 'Review No.'+str(counter)+' '+str(ProbabilityForTruth)+' '+str(
                        ProbabilityForFalse)+' negative '+positivity+' correct\n'
                    predictionCorrectness += 1
            counter += 1

    resultAnswer2 += 'The prediction correctness is ' + \
        str((predictionCorrectness/counter)*100)+'%'

    l2 = round((predictionCorrectness/counter)*100)

    Observer.close()
    f.close()
    f2.close(
    )

    resultAnswer3 = ''
    counter = 1
    predictionCorrectness = 0
    positivity = True

    requests = 0

    with open('lengthfiltering/length9Max-model2.json', 'r+') as Observer:
        model2 = json.load(Observer)

    with open('testing_data_set.txt', 'r') as f2:
        for f3 in f2:

            response = get(
                f3.strip())
            requests += 1
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
                    resultAnswer3 += 'Review No.'+str(counter)+' '+str(ProbabilityForTruth)+' '+str(
                        ProbabilityForFalse)+' positive '+positivity+' correct\n'
                    predictionCorrectness += 1
                else:
                    resultAnswer3 += 'Review No.'+str(counter)+' '+str(ProbabilityForTruth)+' '+str(
                        ProbabilityForFalse)+' positive '+positivity+' incorrect\n'
            else:  # probably false
                if positivity == 'positive':
                    resultAnswer3 += 'Review No.'+str(counter)+' '+str(ProbabilityForTruth)+' '+str(
                        ProbabilityForFalse)+' negative '+positivity+' incorrect\n'
                else:
                    resultAnswer3 += 'Review No.'+str(counter)+' '+str(ProbabilityForTruth)+' '+str(
                        ProbabilityForFalse)+' negative '+positivity+' correct\n'
                    predictionCorrectness += 1
            counter += 1

    resultAnswer3 += 'The prediction correctness is ' + \
        str((predictionCorrectness/counter)*100)+'%'

    l3 = round((predictionCorrectness/counter)*100)

    with open('lengthfiltering/length-result.txt', 'w') as f:

        for i in resultAnswer3:
            f.write(i)

    print('\nlength-result.txt  generated')

    Observer.close()
    f.close()
    f2.close()

    with open('dictionaryReview.json', 'r+') as Observer:
        ultimateDictionary = json.load(Observer)

    totalWordsInPositive = 0
    totalWordsInNegative = 0

    for key in ultimateDictionary:
        ultimateDictionary[key][0] += 1
        ultimateDictionary[key][1] += 1
        ultimateDictionary[key][2] += 2
        totalWordsInPositive += ultimateDictionary[key][0]
        totalWordsInNegative += ultimateDictionary[key][1]

    # model for txt format
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

    with open('smoothfiltering/model2.json', 'w') as json_file:
        json.dump(model2, json_file)

    f.close()
    json_file.close()

    ############################################################################
    ############################################################################

    with open('dictionaryReview.json', 'r+') as Observer:
        ultimateDictionary1 = json.load(Observer)

    totalWordsInPositive1 = 0
    totalWordsInNegative1 = 0

    for key in ultimateDictionary1:
        ultimateDictionary1[key][0] += 1.2
        ultimateDictionary1[key][1] += 1.2
        ultimateDictionary1[key][2] += 2.4
        totalWordsInPositive1 += ultimateDictionary1[key][0]
        totalWordsInNegative1 += ultimateDictionary1[key][1]

    # model1 for txt format
    # model2Point1 for json format
    modelPoint1 = ''
    model2Point1 = {}

    count = 1
    for key in ultimateDictionary1:
        modelPoint1 += 'No.'+str(count)+' ' + key+'\n'
        modelPoint1 += str(ultimateDictionary1[key][0]) + ', ' + \
            str(ultimateDictionary1[key][0]/totalWordsInPositive1)+', '
        modelPoint1 += str(ultimateDictionary1[key][1]) + ', ' + \
            str(ultimateDictionary1[key][1]/totalWordsInNegative1)+'\n'
        model2Point1.update({key: [ultimateDictionary1[key][0], round((ultimateDictionary1[key][0]/totalWordsInPositive1), 6),
                                   ultimateDictionary1[key][1], round((ultimateDictionary1[key][1]/totalWordsInNegative1), 6)]})
        count += 1

    with open('smoothfiltering/model2Point1.json', 'w') as json_file:
        json.dump(model2Point1, json_file)

    f.close()
    json_file.close()

    ############################################################################
    ############################################################################

    with open('dictionaryReview.json', 'r+') as Observer:
        ultimateDictionary2 = json.load(Observer)

    totalWordsInPositive2 = 0
    totalWordsInNegative2 = 0

    for key in ultimateDictionary2:
        ultimateDictionary2[key][0] += 1.4
        ultimateDictionary2[key][1] += 1.4
        ultimateDictionary2[key][2] += 2.8
        totalWordsInPositive2 += ultimateDictionary2[key][0]
        totalWordsInNegative2 += ultimateDictionary2[key][1]

    # model1 for txt format
    # model2Point2 for json format
    modelPoint2 = ''
    model2Point2 = {}

    count = 1
    for key in ultimateDictionary2:
        modelPoint2 += 'No.'+str(count)+' ' + key+'\n'
        modelPoint2 += str(ultimateDictionary2[key][0]) + ', ' + \
            str(ultimateDictionary2[key][0]/totalWordsInPositive2)+', '
        modelPoint2 += str(ultimateDictionary2[key][1]) + ', ' + \
            str(ultimateDictionary2[key][1]/totalWordsInNegative2)+'\n'
        model2Point2.update({key: [ultimateDictionary2[key][0], round((ultimateDictionary2[key][0]/totalWordsInPositive2), 6),
                                   ultimateDictionary2[key][1], round((ultimateDictionary2[key][1]/totalWordsInNegative2), 6)]})
        count += 1

    with open('smoothfiltering/model2Point2.json', 'w') as json_file:
        json.dump(model2Point2, json_file)

    f.close()
    json_file.close()

    ############################################################################
    ############################################################################

    with open('dictionaryReview.json', 'r+') as Observer:
        ultimateDictionary3 = json.load(Observer)

    totalWordsInPositive3 = 0
    totalWordsInNegative3 = 0

    for key in ultimateDictionary3:
        ultimateDictionary3[key][0] += 1.6
        ultimateDictionary3[key][1] += 1.6
        ultimateDictionary3[key][2] += 3.2
        totalWordsInPositive3 += ultimateDictionary3[key][0]
        totalWordsInNegative3 += ultimateDictionary3[key][1]

    # model1 for txt format
    # model2Point3 for json format
    modelPoint3 = ''
    model2Point3 = {}

    count = 1
    for key in ultimateDictionary3:
        modelPoint3 += 'No.'+str(count)+' ' + key+'\n'
        modelPoint3 += str(ultimateDictionary3[key][0]) + ', ' + \
            str(ultimateDictionary3[key][0]/totalWordsInPositive3)+', '
        modelPoint3 += str(ultimateDictionary3[key][1]) + ', ' + \
            str(ultimateDictionary3[key][1]/totalWordsInNegative3)+'\n'
        model2Point3.update({key: [ultimateDictionary3[key][0], round((ultimateDictionary3[key][0]/totalWordsInPositive3), 6),
                                   ultimateDictionary3[key][1], round((ultimateDictionary3[key][1]/totalWordsInNegative3), 6)]})
        count += 1

    with open('smoothfiltering/smooth-model.txt', 'w') as f:

        for i in modelPoint3:
            f.write(i)
    print('\nsmooth-model.txt generated')

    with open('smoothfiltering/model2Point3.json', 'w') as json_file:
        json.dump(model2Point3, json_file)

    f.close()
    json_file.close()

    ############################################################################
    ############################################################################

    with open('dictionaryReview.json', 'r+') as Observer:
        ultimateDictionary4 = json.load(Observer)

    totalWordsInPositive4 = 0
    totalWordsInNegative4 = 0

    for key in ultimateDictionary4:
        ultimateDictionary4[key][0] += 1.8
        ultimateDictionary4[key][1] += 1.8
        ultimateDictionary4[key][2] += 3.6
        totalWordsInPositive4 += ultimateDictionary4[key][0]
        totalWordsInNegative4 += ultimateDictionary4[key][1]

    # model1 for txt format
    # model2Point4 for json format
    modelPoint4 = ''
    model2Point4 = {}

    count = 1
    for key in ultimateDictionary4:
        modelPoint4 += 'No.'+str(count)+' ' + key+'\n'
        modelPoint4 += str(ultimateDictionary4[key][0]) + ', ' + \
            str(ultimateDictionary4[key][0]/totalWordsInPositive4)+', '
        modelPoint4 += str(ultimateDictionary4[key][1]) + ', ' + \
            str(ultimateDictionary4[key][1]/totalWordsInNegative4)+'\n'
        model2Point4.update({key: [ultimateDictionary4[key][0], round((ultimateDictionary4[key][0]/totalWordsInPositive4), 6),
                                   ultimateDictionary4[key][1], round((ultimateDictionary4[key][1]/totalWordsInNegative4), 6)]})
        count += 1

    with open('smoothfiltering/model2Point4.json', 'w') as json_file:
        json.dump(model2Point4, json_file)

    f.close()
    json_file.close()

    with open('dictionaryReview.json', 'r+') as Observer:
        ultimateDictionary5 = json.load(Observer)

    totalWordsInPositive5 = 0
    totalWordsInNegative5 = 0

    for key in ultimateDictionary5:
        ultimateDictionary5[key][0] += 2.0
        ultimateDictionary5[key][1] += 2.0
        ultimateDictionary5[key][2] += 4.0
        totalWordsInPositive5 += ultimateDictionary5[key][0]
        totalWordsInNegative5 += ultimateDictionary5[key][1]

    # model1 for txt format
    # model2Point5 for json format
    modelPoint5 = ''
    model2Point5 = {}

    count = 1
    for key in ultimateDictionary5:
        modelPoint5 += 'No.'+str(count)+' ' + key+'\n'
        modelPoint5 += str(ultimateDictionary5[key][0]) + ', ' + \
            str(ultimateDictionary5[key][0]/totalWordsInPositive5)+', '
        modelPoint5 += str(ultimateDictionary5[key][1]) + ', ' + \
            str(ultimateDictionary5[key][1]/totalWordsInNegative5)+'\n'
        model2Point5.update({key: [ultimateDictionary5[key][0], round((ultimateDictionary5[key][0]/totalWordsInPositive5), 6),
                                   ultimateDictionary5[key][1], round((ultimateDictionary5[key][1]/totalWordsInNegative5), 6)]})
        count += 1

    with open('smoothfiltering/model2Point5.json', 'w') as json_file:
        json.dump(model2Point5, json_file)

    f.close()
    json_file.close()

    resultAnswer = ''
    counter = 1
    predictionCorrectness = 0
    positivity = True

    requests = 0

    with open('smoothfiltering/model2.json', 'r+') as Observer:
        model2 = json.load(Observer)

    with open('testing_data_set.txt', 'r') as f2:
        for f3 in f2:

            response = get(
                f3.strip())
            requests += 1

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

    s1 = round((predictionCorrectness/counter)*100)

    f2.close()
    Observer.close()
    f.close()
    #####################################################################################
    #####################################################################################

    resultAnswer1 = ''
    counter = 1
    predictionCorrectness = 0
    positivity = True

    requests = 0

    with open('smoothfiltering/model2Point1.json', 'r+') as Observer:
        model2 = json.load(Observer)

    with open('testing_data_set.txt', 'r') as f2:
        for f3 in f2:

            response = get(
                f3.strip())
            requests += 1

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
                    resultAnswer1 += 'Review No.'+str(counter)+' '+str(ProbabilityForTruth)+' '+str(
                        ProbabilityForFalse)+' positive '+positivity+' correct\n'
                    predictionCorrectness += 1
                else:
                    resultAnswer1 += 'Review No.'+str(counter)+' '+str(ProbabilityForTruth)+' '+str(
                        ProbabilityForFalse)+' positive '+positivity+' incorrect\n'
            else:  # probably false
                if positivity == 'positive':
                    resultAnswer1 += 'Review No.'+str(counter)+' '+str(ProbabilityForTruth)+' '+str(
                        ProbabilityForFalse)+' negative '+positivity+' incorrect\n'
                else:
                    resultAnswer1 += 'Review No.'+str(counter)+' '+str(ProbabilityForTruth)+' '+str(
                        ProbabilityForFalse)+' negative '+positivity+' correct\n'
                    predictionCorrectness += 1
            counter += 1

    resultAnswer1 += 'The prediction correctness is ' + \
        str((predictionCorrectness/counter)*100)+'%'

    s1 = round((predictionCorrectness/counter)*100)

    f2.close()
    Observer.close()
    f.close()

    #####################################################################################
    #####################################################################################

    resultAnswer2 = ''
    counter = 1
    predictionCorrectness = 0
    positivity = True

    requests = 0

    with open('smoothfiltering/model2Point2.json', 'r+') as Observer:
        model2 = json.load(Observer)

    with open('testing_data_set.txt', 'r') as f2:
        for f3 in f2:

            response = get(
                f3.strip())
            requests += 1

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
                    resultAnswer2 += 'Review No.'+str(counter)+' '+str(ProbabilityForTruth)+' '+str(
                        ProbabilityForFalse)+' positive '+positivity+' correct\n'
                    predictionCorrectness += 1
                else:
                    resultAnswer2 += 'Review No.'+str(counter)+' '+str(ProbabilityForTruth)+' '+str(
                        ProbabilityForFalse)+' positive '+positivity+' incorrect\n'
            else:  # probably false
                if positivity == 'positive':
                    resultAnswer2 += 'Review No.'+str(counter)+' '+str(ProbabilityForTruth)+' '+str(
                        ProbabilityForFalse)+' negative '+positivity+' incorrect\n'
                else:
                    resultAnswer2 += 'Review No.'+str(counter)+' '+str(ProbabilityForTruth)+' '+str(
                        ProbabilityForFalse)+' negative '+positivity+' correct\n'
                    predictionCorrectness += 1
            counter += 1

    resultAnswer2 += 'The prediction correctness is ' + \
        str((predictionCorrectness/counter)*100)+'%'

    s2 = round((predictionCorrectness/counter)*100)

    f2.close()
    Observer.close()
    f.close()

    #####################################################################################
    #####################################################################################

    resultAnswer3 = ''
    counter = 1
    predictionCorrectness = 0
    positivity = True

    requests = 0

    with open('smoothfiltering/model2Point3.json', 'r+') as Observer:
        model2 = json.load(Observer)

    with open('testing_data_set.txt', 'r') as f2:
        for f3 in f2:

            response = get(
                f3.strip())
            requests += 1

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
                    resultAnswer3 += 'Review No.'+str(counter)+' '+str(ProbabilityForTruth)+' '+str(
                        ProbabilityForFalse)+' positive '+positivity+' correct\n'
                    predictionCorrectness += 1
                else:
                    resultAnswer3 += 'Review No.'+str(counter)+' '+str(ProbabilityForTruth)+' '+str(
                        ProbabilityForFalse)+' positive '+positivity+' incorrect\n'
            else:  # probably false
                if positivity == 'positive':
                    resultAnswer3 += 'Review No.'+str(counter)+' '+str(ProbabilityForTruth)+' '+str(
                        ProbabilityForFalse)+' negative '+positivity+' incorrect\n'
                else:
                    resultAnswer3 += 'Review No.'+str(counter)+' '+str(ProbabilityForTruth)+' '+str(
                        ProbabilityForFalse)+' negative '+positivity+' correct\n'
                    predictionCorrectness += 1
            counter += 1

    resultAnswer3 += 'The prediction correctness is ' + \
        str((predictionCorrectness/counter)*100)+'%'

    s3 = round((predictionCorrectness/counter)*100)

    with open('smoothfiltering/smooth-result.txt', 'w') as f:

        for i in resultAnswer3:
            f.write(i)

    print('\nsmooth-result.txt generated')

    f2.close()
    Observer.close()
    f.close()

    #####################################################################################
    #####################################################################################

    resultAnswer4 = ''
    counter = 1
    predictionCorrectness = 0
    positivity = True

    requests = 0

    with open('smoothfiltering/model2Point4.json', 'r+') as Observer:
        model2 = json.load(Observer)

    with open('testing_data_set.txt', 'r') as f2:
        for f3 in f2:

            response = get(
                f3.strip())
            requests += 1

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
                    resultAnswer4 += 'Review No.'+str(counter)+' '+str(ProbabilityForTruth)+' '+str(
                        ProbabilityForFalse)+' positive '+positivity+' correct\n'
                    predictionCorrectness += 1
                else:
                    resultAnswer4 += 'Review No.'+str(counter)+' '+str(ProbabilityForTruth)+' '+str(
                        ProbabilityForFalse)+' positive '+positivity+' incorrect\n'
            else:  # probably false
                if positivity == 'positive':
                    resultAnswer4 += 'Review No.'+str(counter)+' '+str(ProbabilityForTruth)+' '+str(
                        ProbabilityForFalse)+' negative '+positivity+' incorrect\n'
                else:
                    resultAnswer4 += 'Review No.'+str(counter)+' '+str(ProbabilityForTruth)+' '+str(
                        ProbabilityForFalse)+' negative '+positivity+' correct\n'
                    predictionCorrectness += 1
            counter += 1

    resultAnswer4 += 'The prediction correctness is ' + \
        str((predictionCorrectness/counter)*100)+'%'

    s4 = round((predictionCorrectness/counter)*100)

    f2.close()
    Observer.close()
    f.close()

    #####################################################################################
    #####################################################################################

    resultAnswer5 = ''
    counter = 1
    predictionCorrectness = 0
    positivity = True

    requests = 0

    with open('smoothfiltering/model2Point5.json', 'r+') as Observer:
        model2 = json.load(Observer)

    with open('testing_data_set.txt', 'r') as f2:
        for f3 in f2:

            response = get(
                f3.strip())
            requests += 1

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
                    resultAnswer5 += 'Review No.'+str(counter)+' '+str(ProbabilityForTruth)+' '+str(
                        ProbabilityForFalse)+' positive '+positivity+' correct\n'
                    predictionCorrectness += 1
                else:
                    resultAnswer5 += 'Review No.'+str(counter)+' '+str(ProbabilityForTruth)+' '+str(
                        ProbabilityForFalse)+' positive '+positivity+' incorrect\n'
            else:  # probably false
                if positivity == 'positive':
                    resultAnswer5 += 'Review No.'+str(counter)+' '+str(ProbabilityForTruth)+' '+str(
                        ProbabilityForFalse)+' negative '+positivity+' incorrect\n'
                else:
                    resultAnswer5 += 'Review No.'+str(counter)+' '+str(ProbabilityForTruth)+' '+str(
                        ProbabilityForFalse)+' negative '+positivity+' correct\n'
                    predictionCorrectness += 1
            counter += 1

    resultAnswer5 += 'The prediction correctness is ' + \
        str((predictionCorrectness/counter)*100)+'%'

    s5 = round((predictionCorrectness/counter)*100)

    f2.close()
    Observer.close()
    f.close()

    #####################################################################################

    #####################################################################################

    #####################################################################################

    #####################################################################################

    #####################################################################################

    with open('dictionaryReview.json', 'r+') as Observer:
        ultimateDictionary = json.load(Observer)

    removedWords = []

    totalWordsInPositive = 0
    totalWordsInNegative = 0

    for key in ultimateDictionary:

        if ultimateDictionary[key][2] >= 2:

            ultimateDictionary[key][0] += 1
            ultimateDictionary[key][1] += 1
            ultimateDictionary[key][2] += 2
            totalWordsInPositive += ultimateDictionary[key][0]
            totalWordsInNegative += ultimateDictionary[key][1]
        else:
            removedWords.append(key)

    # model1 for txt format
    # model2 for json format
    model = ''
    model2 = {}

    count = 1
    for key in ultimateDictionary:
        if ultimateDictionary[key][2] >= 4:
            model += 'No.'+str(count)+' ' + key+'\n'
            model += str(ultimateDictionary[key][0]) + ', ' + \
                str(ultimateDictionary[key][0]/totalWordsInPositive)+', '
            model += str(ultimateDictionary[key][1]) + ', ' + \
                str(ultimateDictionary[key][1]/totalWordsInNegative)+'\n'
            model2.update({key: [ultimateDictionary[key][0], round((ultimateDictionary[key][0]/totalWordsInPositive), 6),
                                 ultimateDictionary[key][1], round((ultimateDictionary[key][1]/totalWordsInNegative), 6)]})
            count += 1

    # open hash if file needed again
    #
    with open('wordfiltering/model2Min2.json', 'w') as json_file:
        json.dump(model2, json_file)

    ##########################################################################################################

    with open('dictionaryReview.json', 'r+') as Observer:
        ultimateDictionary = json.load(Observer)

    removedWords = []

    totalWordsInPositive = 0
    totalWordsInNegative = 0

    for key in ultimateDictionary:

        if ultimateDictionary[key][2] > 10:
            ultimateDictionary[key][0] += 1
            ultimateDictionary[key][1] += 1
            ultimateDictionary[key][2] += 2
            totalWordsInPositive += ultimateDictionary[key][0]
            totalWordsInNegative += ultimateDictionary[key][1]
        else:
            removedWords.append(key)

    # model1 for txt format
    # model2 for json format
    model = ''
    model2 = {}

    count = 1
    for key in ultimateDictionary:
        # > 12 because the words are smoothen by 2 to avoid a log10(0)
        if ultimateDictionary[key][2] > 12:
            model += 'No.'+str(count)+' ' + key+'\n'
            model += str(ultimateDictionary[key][0]) + ', ' + \
                str(ultimateDictionary[key][0]/totalWordsInPositive)+', '
            model += str(ultimateDictionary[key][1]) + ', ' + \
                str(ultimateDictionary[key][1]/totalWordsInNegative)+'\n'
            model2.update({key: [ultimateDictionary[key][0], round((ultimateDictionary[key][0]/totalWordsInPositive), 6),
                                 ultimateDictionary[key][1], round((ultimateDictionary[key][1]/totalWordsInNegative), 6)]})
            count += 1

    # open hash if file needed again
    #
    with open('wordfiltering/model2Min10.json', 'w') as json_file:
        json.dump(model2, json_file)

    ##########################################################################################################

    with open('dictionaryReview.json', 'r+') as Observer:
        ultimateDictionary = json.load(Observer)

    removedWords = []

    totalWordsInPositive = 0
    totalWordsInNegative = 0

    for key in ultimateDictionary:

        if ultimateDictionary[key][2] > 20:
            ultimateDictionary[key][0] += 1
            ultimateDictionary[key][1] += 1
            ultimateDictionary[key][2] += 2
            totalWordsInPositive += ultimateDictionary[key][0]
            totalWordsInNegative += ultimateDictionary[key][1]
        else:

            removedWords.append(key)

    # model1 for txt format
    # model2 for json format
    model = ''
    model2 = {}

    count = 1
    for key in ultimateDictionary:

        # > 22 because the words are smoothen by 2 to avoid a log10(0)
        if ultimateDictionary[key][2] > 22:
            model += 'No.'+str(count)+' ' + key+'\n'
            model += str(ultimateDictionary[key][0]) + ', ' + \
                str(ultimateDictionary[key][0]/totalWordsInPositive)+', '
            model += str(ultimateDictionary[key][1]) + ', ' + \
                str(ultimateDictionary[key][1]/totalWordsInNegative)+'\n'
            model2.update({key: [ultimateDictionary[key][0], round((ultimateDictionary[key][0]/totalWordsInPositive), 6),
                                 ultimateDictionary[key][1], round((ultimateDictionary[key][1]/totalWordsInNegative), 6)]})
            count += 1

    # open hash if file needed again
    #
    with open('wordfiltering/model2Min20.json', 'w') as json_file:
        json.dump(model2, json_file)

    for i in removedWords:
        del ultimateDictionary[i]

    # the remaing of the top 5% 10% 20% words will be removed from the same ultimateDictionary and added to the same removedwords.txt

    ######################################################################################################################
    ######################################################################################################################
    ######################################################################################################################
    ######################################################################################################################
    ######################################################################################################################
    # Perhaps the most important part here because i will reverse the dicitonary values so that the [0] positive frequency
    # will switch places with [2] total frequency in order to the the sorting right
    ######################################################################################################################
    ######################################################################################################################
    ######################################################################################################################
    ######################################################################################################################

    ultimateDictionary5Percent = ultimateDictionary

    # exact amount to remove from top to bottom 5% top frequent
    number = math.ceil(len(ultimateDictionary5Percent)*0.05)

    for i in ultimateDictionary5Percent:

        temp = ultimateDictionary5Percent[i][2]
        ultimateDictionary5Percent[i][0] = ultimateDictionary5Percent[i][2]
        ultimateDictionary5Percent[i][0] = temp

    # the x[3] is the sum of all frequency, and will be sorted in desc order

    for i in range(number):
        temp = 0

        for key in ultimateDictionary5Percent:
            if ultimateDictionary5Percent[key][0] > temp:
                temp = ultimateDictionary5Percent[key][0]
                inkey = key
        del ultimateDictionary5Percent[inkey]
        removedWords.append(inkey)

    model = ''
    model2 = {}

    totalWordsInPositive = 0
    totalWordsInNegative = 0

    for key in ultimateDictionary5Percent:
        ultimateDictionary5Percent[key][0] += 1
        ultimateDictionary5Percent[key][1] += 1
        ultimateDictionary5Percent[key][2] += 2
        totalWordsInPositive += ultimateDictionary5Percent[key][0]
        totalWordsInNegative += ultimateDictionary5Percent[key][1]

    count = 1
    for key in ultimateDictionary5Percent:

        model += 'No.'+str(count)+' ' + key+'\n'
        model += str(ultimateDictionary5Percent[key][0]) + ', ' + \
            str(ultimateDictionary5Percent[key][0]/totalWordsInPositive)+', '
        model += str(ultimateDictionary5Percent[key][1]) + ', ' + \
            str(ultimateDictionary5Percent[key][1]/totalWordsInNegative)+'\n'
        model2.update({key: [ultimateDictionary5Percent[key][0], round((ultimateDictionary5Percent[key][0]/totalWordsInPositive), 6),
                             ultimateDictionary5Percent[key][1], round((ultimateDictionary5Percent[key][1]/totalWordsInNegative), 6)]})
        count += 1

    # open hash if file needed again
    #
    with open('wordfiltering/model2Percent5.json', 'w') as json_file:
        json.dump(model2, json_file)

    ######################################################################################################################

    ultimateDictionary10Percent = ultimateDictionary

    # exact amount to remove from top to bottom 10% top frequent
    number = math.ceil(len(ultimateDictionary10Percent)*0.10)

    for i in ultimateDictionary10Percent:

        temp = ultimateDictionary10Percent[i][2]
        ultimateDictionary10Percent[i][0] = ultimateDictionary10Percent[i][2]
        ultimateDictionary10Percent[i][0] = temp

    # the x[3] is the sum of all frequency, and will be sorted in desc order

    for i in range(number):
        temp = 0

        for key in ultimateDictionary10Percent:
            if ultimateDictionary10Percent[key][0] > temp:
                temp = ultimateDictionary10Percent[key][0]
                inkey = key
        del ultimateDictionary10Percent[inkey]
        removedWords.append(inkey)

    model = ''
    model2 = {}

    totalWordsInPositive = 0
    totalWordsInNegative = 0

    for key in ultimateDictionary10Percent:
        ultimateDictionary10Percent[key][0] += 1
        ultimateDictionary10Percent[key][1] += 1
        ultimateDictionary10Percent[key][2] += 2
        totalWordsInPositive += ultimateDictionary10Percent[key][0]
        totalWordsInNegative += ultimateDictionary10Percent[key][1]

    count = 1
    for key in ultimateDictionary10Percent:

        model += 'No.'+str(count)+' ' + key+'\n'
        model += str(ultimateDictionary10Percent[key][0]) + ', ' + \
            str(ultimateDictionary10Percent[key][0]/totalWordsInPositive)+', '
        model += str(ultimateDictionary10Percent[key][1]) + ', ' + \
            str(ultimateDictionary10Percent[key][1]/totalWordsInNegative)+'\n'
        model2.update({key: [ultimateDictionary10Percent[key][0], round((ultimateDictionary10Percent[key][0]/totalWordsInPositive), 6),
                             ultimateDictionary10Percent[key][1], round((ultimateDictionary10Percent[key][1]/totalWordsInNegative), 6)]})
        count += 1

    # open hash if file needed again
    #
    with open('wordfiltering/model2Percent10.json', 'w') as json_file:
        json.dump(model2, json_file)

    ######################################################################################################################

    ultimateDictionary20Percent = ultimateDictionary

    # exact amount to remove from top to bottom 5% top frequent
    number = math.ceil(len(ultimateDictionary20Percent)*0.05)

    for i in ultimateDictionary20Percent:

        temp = ultimateDictionary20Percent[i][2]
        ultimateDictionary20Percent[i][0] = ultimateDictionary20Percent[i][2]
        ultimateDictionary20Percent[i][0] = temp

    # the x[3] is the sum of all frequency, and will be sorted in desc order

    for i in range(number):
        temp = 0

        for key in ultimateDictionary20Percent:
            if ultimateDictionary20Percent[key][0] > temp:
                temp = ultimateDictionary20Percent[key][0]
                inkey = key
        del ultimateDictionary20Percent[inkey]
        removedWords.append(inkey)

    model = ''
    model2 = {}

    totalWordsInPositive = 0
    totalWordsInNegative = 0

    for key in ultimateDictionary20Percent:
        ultimateDictionary20Percent[key][0] += 1
        ultimateDictionary20Percent[key][1] += 1
        ultimateDictionary20Percent[key][2] += 2
        totalWordsInPositive += ultimateDictionary20Percent[key][0]
        totalWordsInNegative += ultimateDictionary20Percent[key][1]

    count = 1
    for key in ultimateDictionary20Percent:

        model += 'No.'+str(count)+' ' + key+'\n'
        model += str(ultimateDictionary20Percent[key][0]) + ', ' + \
            str(ultimateDictionary20Percent[key][0]/totalWordsInPositive)+', '
        model += str(ultimateDictionary20Percent[key][1]) + ', ' + \
            str(ultimateDictionary20Percent[key][1]/totalWordsInNegative)+'\n'
        model2.update({key: [ultimateDictionary20Percent[key][0], round((ultimateDictionary20Percent[key][0]/totalWordsInPositive), 6),
                             ultimateDictionary20Percent[key][1], round((ultimateDictionary20Percent[key][1]/totalWordsInNegative), 6)]})
        count += 1

    ultimateDictionary20Percent = sorted(
        ultimateDictionary20Percent.items(), key=lambda x: x[1], reverse=True)

    # with open('wordfiltering/modelPercent20.txt', 'w') as f:

    #   for i in model:
    #       f.write(i)

    with open('wordfiltering/frequency-mode.txt', 'w') as f:

        for i in model:
            f.write(i)
    print('\nfrequency-mode.txt generated')

    # open hash if file needed again
    #
    with open('wordfiltering/model2Percent20.json', 'w') as json_file:
        json.dump(model2, json_file)

    textfile = open("wordfiltering/removed.txt", "w")
    for i in removedWords:
        textfile.write(i + "\n")
    textfile.close()

    print('\nremoved.txt generated')

    ######################################################################################################################

    resultAnswer = ''
    counter = 1
    predictionCorrectness = 0
    positivity = True

    requests = 0

    with open('wordfiltering/model2Min2.json', 'r+') as Observer:
        model2 = json.load(Observer)

    with open('testing_data_set.txt', 'r') as f2:
        for f3 in f2:

            response = get(
                f3.strip())
            requests += 1

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

    w1 = round((predictionCorrectness/counter)*100)

    Observer.close()
    f2.close()
    f.close()
    ###########################################################################################################################

    ######################################################################################################################

    resultAnswer1 = ''
    counter = 1
    predictionCorrectness = 0
    positivity = True

    requests = 0

    with open('wordfiltering/model2Min10.json', 'r+') as Observer:
        model2 = json.load(Observer)

    with open('testing_data_set.txt', 'r') as f2:
        for f3 in f2:

            response = get(
                f3.strip())
            requests += 1

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
                    resultAnswer1 += 'Review No.'+str(counter)+' '+str(ProbabilityForTruth)+' '+str(
                        ProbabilityForFalse)+' positive '+positivity+' correct\n'
                    predictionCorrectness += 1
                else:
                    resultAnswer1 += 'Review No.'+str(counter)+' '+str(ProbabilityForTruth)+' '+str(
                        ProbabilityForFalse)+' positive '+positivity+' incorrect\n'
            else:  # probably false
                if positivity == 'positive':
                    resultAnswer1 += 'Review No.'+str(counter)+' '+str(ProbabilityForTruth)+' '+str(
                        ProbabilityForFalse)+' negative '+positivity+' incorrect\n'
                else:
                    resultAnswer1 += 'Review No.'+str(counter)+' '+str(ProbabilityForTruth)+' '+str(
                        ProbabilityForFalse)+' negative '+positivity+' correct\n'
                    predictionCorrectness += 1
            counter += 1

    resultAnswer1 += 'The prediction correctness is ' + \
        str((predictionCorrectness/counter)*100)+'%'
    w2 = round((predictionCorrectness/counter)*100)

    Observer.close()
    f2.close()
    f.close()
    ###########################################################################################################################

    ######################################################################################################################

    resultAnswer2 = ''
    counter = 1
    predictionCorrectness = 0
    positivity = True

    requests = 0

    with open('wordfiltering/model2Min20.json', 'r+') as Observer:
        model2 = json.load(Observer)

    with open('testing_data_set.txt', 'r') as f2:
        for f3 in f2:

            response = get(
                f3.strip())
            requests += 1

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
                    resultAnswer2 += 'Review No.'+str(counter)+' '+str(ProbabilityForTruth)+' '+str(
                        ProbabilityForFalse)+' positive '+positivity+' correct\n'
                    predictionCorrectness += 1
                else:
                    resultAnswer2 += 'Review No.'+str(counter)+' '+str(ProbabilityForTruth)+' '+str(
                        ProbabilityForFalse)+' positive '+positivity+' incorrect\n'
            else:  # probably false
                if positivity == 'positive':
                    resultAnswer2 += 'Review No.'+str(counter)+' '+str(ProbabilityForTruth)+' '+str(
                        ProbabilityForFalse)+' negative '+positivity+' incorrect\n'
                else:
                    resultAnswer2 += 'Review No.'+str(counter)+' '+str(ProbabilityForTruth)+' '+str(
                        ProbabilityForFalse)+' negative '+positivity+' correct\n'
                    predictionCorrectness += 1
            counter += 1

    resultAnswer2 += 'The prediction correctness is ' + \
        str((predictionCorrectness/counter)*100)+'%'

    w3 = round((predictionCorrectness/counter)*100)

    Observer.close()
    f2.close()
    f.close()
    ###########################################################################################################################

    ######################################################################################################################

    resultAnswer3 = ''
    counter = 1
    predictionCorrectness = 0
    positivity = True

    requests = 0

    with open('wordfiltering/model2Percent5.json', 'r+') as Observer:
        model2 = json.load(Observer)

    with open('testing_data_set.txt', 'r') as f2:
        for f3 in f2:

            response = get(
                f3.strip())
            requests += 1

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
                    resultAnswer3 += 'Review No.'+str(counter)+' '+str(ProbabilityForTruth)+' '+str(
                        ProbabilityForFalse)+' positive '+positivity+' correct\n'
                    predictionCorrectness += 1
                else:
                    resultAnswer3 += 'Review No.'+str(counter)+' '+str(ProbabilityForTruth)+' '+str(
                        ProbabilityForFalse)+' positive '+positivity+' incorrect\n'
            else:  # probably false
                if positivity == 'positive':
                    resultAnswer3 += 'Review No.'+str(counter)+' '+str(ProbabilityForTruth)+' '+str(
                        ProbabilityForFalse)+' negative '+positivity+' incorrect\n'
                else:
                    resultAnswer3 += 'Review No.'+str(counter)+' '+str(ProbabilityForTruth)+' '+str(
                        ProbabilityForFalse)+' negative '+positivity+' correct\n'
                    predictionCorrectness += 1
            counter += 1

    resultAnswer3 += 'The prediction correctness is ' + \
        str((predictionCorrectness/counter)*100)+'%'

    w4 = round((predictionCorrectness/counter)*100)

    Observer.close()
    f2.close()
    f.close()
    ###########################################################################################################################

    ######################################################################################################################

    resultAnswer4 = ''
    counter = 1
    predictionCorrectness = 0
    positivity = True

    requests = 0

    with open('wordfiltering/model2Percent10.json', 'r+') as Observer:
        model2 = json.load(Observer)

    with open('testing_data_set.txt', 'r') as f2:
        for f3 in f2:

            response = get(
                f3.strip())
            requests += 1

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
                    resultAnswer4 += 'Review No.'+str(counter)+' '+str(ProbabilityForTruth)+' '+str(
                        ProbabilityForFalse)+' positive '+positivity+' correct\n'
                    predictionCorrectness += 1
                else:
                    resultAnswer4 += 'Review No.'+str(counter)+' '+str(ProbabilityForTruth)+' '+str(
                        ProbabilityForFalse)+' positive '+positivity+' incorrect\n'
            else:  # probably false
                if positivity == 'positive':
                    resultAnswer4 += 'Review No.'+str(counter)+' '+str(ProbabilityForTruth)+' '+str(
                        ProbabilityForFalse)+' negative '+positivity+' incorrect\n'
                else:
                    resultAnswer4 += 'Review No.'+str(counter)+' '+str(ProbabilityForTruth)+' '+str(
                        ProbabilityForFalse)+' negative '+positivity+' correct\n'
                    predictionCorrectness += 1
            counter += 1

    resultAnswer4 += 'The prediction correctness is ' + \
        str((predictionCorrectness/counter)*100)+'%'

    w5 = round((predictionCorrectness/counter)*100)

    Observer.close()
    f2.close()
    f.close()
    ###########################################################################################################################

    ######################################################################################################################

    resultAnswer6 = ''
    counter = 1
    predictionCorrectness = 0
    positivity = True

    requests = 0

    with open('wordfiltering/model2Percent20.json', 'r+') as Observer:
        model2 = json.load(Observer)

    with open('testing_data_set.txt', 'r') as f2:
        for f3 in f2:

            response = get(
                f3.strip())
            requests += 1

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
                    resultAnswer6 += 'Review No.'+str(counter)+' '+str(ProbabilityForTruth)+' '+str(
                        ProbabilityForFalse)+' positive '+positivity+' correct\n'
                    predictionCorrectness += 1
                else:
                    resultAnswer6 += 'Review No.'+str(counter)+' '+str(ProbabilityForTruth)+' '+str(
                        ProbabilityForFalse)+' positive '+positivity+' incorrect\n'
            else:  # probably false
                if positivity == 'positive':
                    resultAnswer6 += 'Review No.'+str(counter)+' '+str(ProbabilityForTruth)+' '+str(
                        ProbabilityForFalse)+' negative '+positivity+' incorrect\n'
                else:
                    resultAnswer6 += 'Review No.'+str(counter)+' '+str(ProbabilityForTruth)+' '+str(
                        ProbabilityForFalse)+' negative '+positivity+' correct\n'
                    predictionCorrectness += 1
            counter += 1

    resultAnswer6 += 'The prediction correctness is ' + \
        str((predictionCorrectness/counter)*100)+'%'

    w6 = round((predictionCorrectness/counter)*100)

    with open('wordfiltering/frequency-result.txt', 'w') as f:

        for i in resultAnswer6:
            f.write(i)
    print('\nfrequency-result.txt generated')
    Observer.close()
    f2.close()
    f.close()

    print('\n\n\n ::::::::::::::::::::::Analysis:::::::::::::::::::: ')
    print('Original prediction rate result:', r0)
    print('length >3 prediction rate result :', l1)
    print('length >5 prediction rate result :', l2)
    print('length <9 prediction rate result :', l3)
    print('smooth δ=1.2 prediction rate result :', s1)
    print('smooth δ=1.4 prediction rate result :', s2)
    print('smooth δ=1.6 prediction rate result :', s3)
    print('smooth δ=1.8 prediction rate result :', s4)
    print('smooth δ=2.0 prediction rate result :', s5)
    print('word frequency >2 prediction rate result  :', w1)
    print('word frequency >11 prediction rate result :', w2)
    print('word frequency >21 prediction rate result :', w3)
    print('word frequency remove top 5% prediction rate result :', w4)
    print('word frequency remove top 10% prediction rate result :', w5)
    print('word frequency remove top 20% prediction rate result :', w6)
    x = np.array(['original', 'min3', 'min5', 'max9'])
    y = np.array([r0, l1, l2, l3])

    plt.subplot(1, 3, 1)
    plt.bar(x, y)
    plt.xlabel('types of models')
    plt.ylabel('accuracy in % out of 1')
    plt.title(' Performance of Lengthening-Filtering Classifiers ')
    # plot 2:
    x = np.array(['original', 'min2', 'min10',
                 'min20', 'top5', 'top10', 'top20'])
    y = np.array([r0, w1, w2, w3, w4, w5, w6])

    plt.subplot(1, 3, 2)
    plt.bar(x, y)
    plt.xlabel('types of models')
    plt.ylabel('accuracy in % out of 1')
    plt.title(' Performance of Word-Filtering Classifiers ')
    # plot 3:
    x = np.array(['δ=1', 'δ=1.2', 'δ=1.4', 'δ=1.6', 'δ=1.8', 'δ=2'])
    y = np.array([r0, s1, s2, s3, s4, s5])

    plt.subplot(1, 3, 3)
    plt.bar(x, y)
    plt.xlabel('types of models')
    plt.ylabel('accuracy in % out of 1')
    plt.title(' Performance of Smooth-Filtering Classifiers ')

    manager = plt.get_current_fig_manager()
    manager.full_screen_toggle()
    print('/n press f to toggle screen')
    plt.show()


def Main():
    screen_pic = pygame.image.load(r'instructions.PNG')
    entry_pic = pygame.image.load(r'rehoboam.PNG')
    launch_pic = pygame.image.load(r'launch.PNG')
    pygame.display.set_caption("Rehoboam")
    WHITE = (255, 255, 255)
    pygame.init()

    win = pygame.display.set_mode((840, 653))
    win.fill(WHITE)
    win.blit(entry_pic, (0, 0))
    pygame.display.update()
    run = True

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:
                    win.fill(WHITE)
                    win.blit(launch_pic, (0, 0))
                    pygame.display.update()
                    sleep(3)
                    pygame.quit()
                    Analysis()
                    run = False
                if event.key == pygame.K_RETURN:
                    win.fill(WHITE)
                    win.blit(screen_pic, (0, 0))
                    pygame.display.update()


def superMain():
    while True:
        Main()


superMain()
