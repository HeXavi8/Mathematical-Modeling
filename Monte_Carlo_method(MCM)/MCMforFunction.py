#Calculate the area under the curve from 10000 random points X squared
import random
import matplotlib.pyplot as plt
%matplotlib inline

def integral():
    n = 10000#Bigger, more slowly, more accurate
    x_min, x_max = 0.0, 1.0
    y_min, y_max = 0.0, 1.0
    count = 0
    for i in range(0, n):
        x = random.uniform(x_min, x_max)
        y = random.uniform(y_min, y_max)
        # x*x > y，Indicates that the point is below the curve. The integral value sought is the ratio of the area under the curve to the area of ​​the square.
        if x*x > y:
            count += 1
            plt.scatter(x, y)#
    integral_value = count / float(n)
    print (integral_value)
    plt.show()#Draw the picture

integral()
