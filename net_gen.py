import numpy as np
import matplotlib.pyplot as plt
import sys
import time

print "This"

print "and that."
sys.setrecursionlimit(15000)

#plt.ion()
#plt.show()  

def move(net,x,y,x_prev,y_prev,x_fin,y_fin,net_max):
	net_path=net
	
	while not x == x_fin or not y == y_fin:
		
		x_or_y = (-1)**(np.random.binomial(1,0.5,1)+1)
		x_prob=0.5+(x_fin-x)-(x_fin-x_prev)
		 / (np.max([x_fin,x])*1.5)
		
		xi = (-1)**(np.random.binomial(1,x_prob,1)+1)

		yi = (-1)**(np.random.binomial(1,y_prob,1)+1)
		if x_or_y ==1:
			#plt.clf()
			x_step=x+xi
			if not x_step ==x_prev and x_step<=net_max and x_step>=0:
				
				net_path[x_step,y]+=1
				
				#plt.imshow(net,interpolation="nearest")
				#plt.pause(0.001)
				
				x_prev,y_prev,x = x,y,x_step
		elif x_or_y == -1:
			y_step=y+yi
			if not y_step ==y_prev and y_step<=net_max and y_step>=0:
				net_path[x,y_step]+=1
				x_prev,y_prev,y = x,y,y_step
				#plt.imshow(net,interpolation="nearest")
				#plt.pause(0.001)
	return net_path
l=np.zeros((90,90))
for i in range(20):
	print i
	l=move(l, 20,20,0,0,60,60,89 )

plt.imshow(l)
plt.show()

dists=np.arange(20,50)



