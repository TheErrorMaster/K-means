import numpy as np
import itertools
import matplotlib.pyplot as plt
from scipy.io import loadmat
data = loadmat('kmeansdata.mat')
X = data['X']
K = 3
initial_centroids = np.array([[3,3],[6,2],[8,5]])
num_points = len(X)
dist = np.zeros((K,num_points))
# num_points = len(X)
runTimes = 10

def distanceBetPointsAndCentroids(): # get the distance between points and centriods
    d = np.array([])
    for i in range(K):
        for j in range(num_points):
            dist[i,j] = np.linalg.norm(initial_centroids[i] -X[j])
print(distanceBetPointsAndCentroids())

def mean2(arr):# the average/mean of data given
    a = []
    for i in arr:# graph all all the data and find average/mean
        a.append([X[i][0],X[i][1]])
    np_a = np.array(a)
    result = np.mean(np_a, axis = 0)
    return result

def findMin(): # num_points, dist, initial_centriods
    x = [] # index of smallest
    y = []
    
    a0 = [] # row of smallest in column
    a1 = []
    a2 = []
 
    for i in range(num_points):
        s = np.argmin(dist[:,i]) # gets the min of column
        c = i # gets the column number 
        x.append(s)#where the smallest are r index
        y.append(c)
    for a,b in zip(x,y):
        if(a == 0):
            a0.append(b)
        elif(a == 1):
            a1.append(b)
        elif(a == 2):
            a2.append(b)
    return a0,a1,a2

def firstPlot(a,b,c): # plot initial plot
    a1 = []
    b1 = []
    c1 = []
    
    for i in a:
        a1.append([X[i][0],X[i][1]])
    for i in b:
        b1.append([X[i][0],X[i][1]])
    for i in c:
        c1.append([X[i][0],X[i][1]])

    x1 = np.array(a1)
    y1 = np.array(b1)
    z1 = np.array(c1)
    
    plt.figure()
    plt.subplot(1,1,1)
    plt.plot(x1[:,0],x1[:,1],'ko') #plot x $ y using black circle makers
    plt.plot(y1[:,0],y1[:,1],'ko')
    plt.plot(z1[:,0],z1[:,1],'ko')
    colors = ("red","green","blue") #color of centroids
    plt.scatter(initial_centroids[:,0], initial_centroids[:,1], marker = "x", c = colors)
    plt.title("initial point distrbution")
    plt.show()

min1,min2,min3 = findMin()
firstPlot(min1,min2,min3)

def colorPlot(a,b,c): #color clusters
    a1 = []
    b1 = []
    c1 = []
    
    for i in a:
        a1.append([X[i][0],X[i][1]])
    for i in b:
        b1.append([X[i][0],X[i][1]])
    for i in c:
        c1.append([X[i][0],X[i][1]])

    x1 = np.array(a1)
    y1 = np.array(b1)
    z1 = np.array(c1)
    
    plt.figure()
    plt.subplot(1,1,1)
    plt.plot(x1[:,0],x1[:,1], 'ro')#color here
    plt.plot(y1[:,0],y1[:,1], 'go')
    plt.plot(z1[:,0],z1[:,1], 'bo')
    colors = ("red","green","blue")
    plt.scatter(initial_centroids[:,0], initial_centroids[:,1], marker = "x", c = colors)
    plt.title("initial color clusters ")
    plt.show()
    
colorPlot(min1,min2,min3)

def iterPlot(a,b,c,n): #each iteration display change
    a1 = []
    b1 = []
    c1 = []
    
    for i in a:
        a1.append([X[i][0],X[i][1]])
    for i in b:
        b1.append([X[i][0],X[i][1]])
    for i in c:
        c1.append([X[i][0],X[i][1]])

    x1 = np.array(a1)
    y1 = np.array(b1)
    z1 = np.array(c1)
    
    marker = itertools.cycle(('^','+','x','v','*')) # change iteration maker symbol here
    plt.figure()
    plt.subplot(1,1,1)
    plt.plot(x1[:,0],x1[:,1], 'ro')
    plt.plot(y1[:,0],y1[:,1], 'go')
    plt.plot(z1[:,0],z1[:,1], 'bo')
    colors = ("red","green","blue")
    plt.scatter(initial_centroids[:,0], initial_centroids[:,1],n, marker = next(marker), c = colors)
    plt.title("iteration changing clusters ")
    plt.show()

def finalPlot(a,b,c): #final result of plot
    a1 = []
    b1 = []
    c1 = []
    
    for i in a:
        a1.append([X[i][0],X[i][1]])
    for i in b:
        b1.append([X[i][0],X[i][1]])
    for i in c:
        c1.append([X[i][0],X[i][1]])

    x1 = np.array(a1)
    y1 = np.array(b1)
    z1 = np.array(c1)
    
    plt.figure()
    plt.subplot(1,1,1)
    plt.plot(x1[:,0],x1[:,1], 'ro')
    plt.plot(y1[:,0],y1[:,1], 'go')
    plt.plot(z1[:,0],z1[:,1], 'bo')
    colors = ("red","green","blue")
    plt.scatter(initial_centroids[:,0], initial_centroids[:,1], marker = "x", c = colors)
    plt.title("final clusters ")
    plt.show()
    
def centeroids(a,b,c):
    initial_centroids[0] = mean2(a)
    initial_centroids[1] = mean2(b)
    initial_centroids[2] = mean2(c)

def K_mean(times): # K,num_points, dist, initial_centroids,X,runTimes
    for i in range(times):
        print('iterations: ',i+1)
        distanceBetPointsAndCentroids()
        a,b,c = findMin()
        centeroids(a,b,c)
        iterPlot(a,b,c,i)
        if(i == 9): # last iteration
            finalPlot(a,b,c)

K_mean(runTimes)