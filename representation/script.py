import numpy as np
import scipy as sp
import matplotlib.pyplot as plt


data = sp.genfromtxt("web_traffic.tsv",delimiter='\t')
print(data[:10])
print(data.shape)
x = data[:,0]
y = data[:,1]
sp.sum(sp.isnan(y))
x = x[~sp.isnan(y)]
y = y[~sp.isnan(y)]

print(x.shape,y.shape)

plt.scatter(x,y)
plt.title("Web Traffic over last month ")
plt.xlabel("Time")
plt.ylabel("Hits/hour")
plt.xticks([w*7*24 for w in range(10)] , ['week %i'%w for w in range(10)])
plt.autoscale(tight =False)
plt.grid()
plt.show()
               