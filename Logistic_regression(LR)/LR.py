import math
import numpy as np
import matplotlib.pyplot as plt


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


def init_data():
    data = np.loadtxt('data.csv')
    dataMatIn = data[:, 0:-1]
    classLabels = data[:, -1]
    dataMatIn = np.insert(dataMatIn, 0, 1, axis=1)  #Feature data set, adding 1 is to construct constant term x0
    return dataMatIn, classLabels


def grad_ascent(dataMatIn, classLabels):
    dataMatrix = np.mat(dataMatIn)  #(m,n)
    labelMat = np.mat(classLabels).transpose()
    m, n = np.shape(dataMatrix)
    weights = np.ones((n, 1))  #Initialize regression coefficients（n, 1)
    alpha = 0.001 #Stride
    maxCycle = 500  #Maximum number of cycles

    for i in range(maxCycle):
        h = sigmoid(dataMatrix * weights)  #sigmoid function
        error = labelMat - h  #y-h, (m - 1)
        weights = weights + alpha * dataMatrix.transpose() * error
    return weights


def plotBestFIt(weights):
    dataMatIn, classLabels = init_data()
    n = np.shape(dataMatIn)[0]
    xcord1 = []
    ycord1 = []
    xcord2 = []
    ycord2 = []
    for i in range(n):
        if classLabels[i] == 1:
            xcord1.append(dataMatIn[i][1])
            ycord1.append(dataMatIn[i][2])
        else:
            xcord2.append(dataMatIn[i][1])
            ycord2.append(dataMatIn[i][2])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord1, ycord1,s=30, c='red', marker='s')
    ax.scatter(xcord2, ycord2, s=30, c='green')
    x = np.arange(-3, 3, 0.1)
    y = (-weights[0, 0] - weights[1, 0] * x) / weights[2, 0]  #matix
    ax.plot(x, y)
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.show()


# The idea of the stochastic gradient ascent method is to use only one data sample point to update the regression coefficients at a time. This greatly reduces computational overhead
def stoc_grad_ascent(dataMatIn, classLabels):
    m, n = np.shape(dataMatIn)
    alpha = 0.01
    weights = np.ones(n)
    for i in range(m):
        h = sigmoid(sum(dataMatIn[i] * weights))  #Calculate
        error = classLabels[i] - h
        weights = weights + alpha * error * dataMatIn[i]
    return weights

# The idea of the stochastic gradient ascent method is to use only one data sample point to update the regression coefficients at a time. This greatly reduces computational overhead
def stoc_grad_ascent_one(dataMatIn, classLabels, numIter=150):
    m, n = np.shape(dataMatIn)
    weights = np.ones(n)
    for j in range(numIter):
        dataIndex = list(range(m))
        for i in range(m):
            alpha = 4 / (1 + i + j) + 0.01 #Ensure that new data is still influential after multiple iterations
            randIndex = int(np.random.uniform(0, len(dataIndex)))
            h = sigmoid(sum(dataMatIn[i] * weights))  # Calculate
            error = classLabels[i] - h
            weights = weights + alpha * error * dataMatIn[i]
            del(dataIndex[randIndex])
    return weights

# Evaluation of the advantages and disadvantages of the algorithm depends on whether it converges or not and whether it reaches a stable value. The faster the convergence, the better the algorithm.


if __name__ == '__main__':
    dataMatIn, classLabels = init_data()
    r = stoc_grad_ascent_one(dataMatIn, classLabels)
    r = np.mat(r).transpose()
    print(r)
    plotBestFIt(r)

