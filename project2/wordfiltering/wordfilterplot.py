import matplotlib.pyplot as plt


x = ['original', 'min2', 'min10', 'min20', 'top5', 'top10', 'top20']
y = [0.631578, 0.647368, 0.657894,
     0.673684, 0.710526, 0.742105, 0.731578]
plt.barh(x, y, color=['red', 'red', 'red', 'red', 'red', 'blue', 'red'])

for index, value in enumerate(y):
    plt.text(value, index, str(value))
plt.ylabel('types of models')
plt.xlabel('accuracy in % out of 1')
plt.title(' Performance of Word-Filtering Classifiers ')

plt.show()
