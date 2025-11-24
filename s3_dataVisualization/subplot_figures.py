import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y1 = [2,3,5,7,11]
y2 = [1,4,6,8,10]

fig,(ax1,ax2) = plt.subplots(1,2)
ax1.plot(x,y1,color='r')
ax2.plot(x,y2,color='g')
ax1.set_title('Line 1')
ax2.set_title('Line 2')
plt.show()
