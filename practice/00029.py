import matplotlib.pyplot as plt

# x-coordinates of left sides of bars
left = [1, 2, 3, 4, 5]

height = [10, 24, 60, 40, 5]

tick_label = ['model1', 'model2', 'model3', 'model4', 'model5']

plt.bar(left, height, tick_label=tick_label,
        width=0.8, color=['red', 'red', 'blue'])

plt.xlabel('types of models')
plt.ylabel('accuracy in %')
plt.title('Rehoboam Analysis')

# function to show the plot
plt.show()
