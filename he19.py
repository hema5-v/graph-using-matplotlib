#creating a simple graph
import matplotlib.pyplot as plt 
# list of values of x-axis and y-axis
x=[1,4,5]
y=[7,9,10]
#plotting the points
plt.plot(x,y)
#labeling them
plt.xlabel('x-axis')
plt.ylabel('y-axis')
#giving tittle
plt.title('my first graph')
plt.show()