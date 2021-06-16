from typing import Text
import pandas as pd
import requests
from requests import get
from bs4 import BeautifulSoup
import re
import json
from time import time
from random import randint
from time import sleep
import math
sloth = "\n\n\n"
resultAnswer = ''
counter = 1
predictionCorrectness = 0
positivity = True
start_time = time()
requests = 0

with open('smoothfiltering/model2.json', 'r+') as Observer:
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

with open('smoothfiltering/result.txt', 'w') as f:

    for i in resultAnswer:
        f.write(i)

f2.close()
Observer.close()
f.close()
#####################################################################################
#####################################################################################


sloth = "\n\n\n"
resultAnswer1 = ''
counter = 1
predictionCorrectness = 0
positivity = True
start_time = time()
requests = 0

with open('smoothfiltering/model2Point1.json', 'r+') as Observer:
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

with open('smoothfiltering/resultPoint1.txt', 'w') as f:

    for i in resultAnswer1:
        f.write(i)

f2.close()
Observer.close()
f.close()

#####################################################################################
#####################################################################################


sloth = "\n\n\n"
resultAnswer2 = ''
counter = 1
predictionCorrectness = 0
positivity = True
start_time = time()
requests = 0

with open('smoothfiltering/model2Point2.json', 'r+') as Observer:
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

with open('smoothfiltering/resultPoint2.txt', 'w') as f:

    for i in resultAnswer2:
        f.write(i)


f2.close()
Observer.close()
f.close()

#####################################################################################
#####################################################################################


sloth = "\n\n\n"
resultAnswer3 = ''
counter = 1
predictionCorrectness = 0
positivity = True
start_time = time()
requests = 0

with open('smoothfiltering/model2Point3.json', 'r+') as Observer:
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

with open('smoothfiltering/resultPoint3.txt', 'w') as f:

    for i in resultAnswer3:
        f.write(i)

with open('smoothfiltering/smooth-result.txt', 'w') as f:

    for i in resultAnswer3:
        f.write(i)


f2.close()
Observer.close()
f.close()

#####################################################################################
#####################################################################################


sloth = "\n\n\n"
resultAnswer4 = ''
counter = 1
predictionCorrectness = 0
positivity = True
start_time = time()
requests = 0

with open('smoothfiltering/model2Point4.json', 'r+') as Observer:
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

with open('smoothfiltering/resultPoint4.txt', 'w') as f:

    for i in resultAnswer4:
        f.write(i)


f2.close()
Observer.close()
f.close()


#####################################################################################
#####################################################################################


sloth = "\n\n\n"
resultAnswer5 = ''
counter = 1
predictionCorrectness = 0
positivity = True
start_time = time()
requests = 0

with open('smoothfiltering/model2Point5.json', 'r+') as Observer:
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

with open('smoothfiltering/resultPoint5.txt', 'w') as f:

    for i in resultAnswer5:
        f.write(i)


f2.close()
Observer.close()
f.close()
