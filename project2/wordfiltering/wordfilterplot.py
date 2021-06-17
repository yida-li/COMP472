import matplotlib.pyplot as plt
import numpy as np

x = ['original', 'min2', 'min10', 'min20', 'top5', 'top10', 'top20']
y = [0.631578, 0.647368, 0.657894,
     0.673684, 0.710526, 0.742105, 0.731578]

yy = [1, 2, 3, 4, 5, 6, 7]
plt.barh(x, y, color=['red', 'red', 'red', 'red', 'red', 'blue', 'red'])

for index, value in enumerate(y):
    plt.text(value, index, str(value))
plt.ylabel('types of models')
plt.xlabel('accuracy in % out of 1')
plt.title(' Performance of Word-Filtering Classifiers ')
manager = plt.get_current_fig_manager()
manager.full_screen_toggle()
plt.xticks(yy, y)
plt.show()
