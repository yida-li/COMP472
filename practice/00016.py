####################################################
# 16. : Dormir
####################################################
import requests
from time import sleep
from random import randint

from time import time
from IPython.core.display import clear_output
start_time = time()
requests = 0
for _ in range(5):
    # A request would go here
    requests += 1
    sleep(randint(1, 3))
    current_time = time()
    elapsed_time = current_time - start_time
    print('well the elapsed time is : {};'.format(elapsed_time))
    print('Request: {}; Frequency: {} requests/s'.format(requests, requests/elapsed_time))

clear_output(wait=True)
