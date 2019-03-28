#two lines on same graph
import matplotlib.pyplot as plt 
x1=[4,7,8]
y1=[2,3,9]
plt.plot(x1,y1,label="line1")

x2=[5,7,10]
y2=[1,6,8]
plt.plot(x2,y2,label="line2")
plt.xlabel('x-axis')
plt.ylabel('y - axis') 
# giving a title to my graph 
plt.title('Two lines on same graph!') 

#giving color to them
plt.plot([4,7,8],[2,3,9],color="red")
plt.plot([5,7,10],[1,6,8],color="green")

  
# function to show the plot 
plt.show() 
