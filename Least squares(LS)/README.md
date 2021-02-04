## 最小二乘法Least squares(LS)

### What:
The method of least squares is a standard approach in regression analysis to approximate the solution of overdetermined systems (sets of equations in which there are more equations than unknowns) by minimizing the sum of the squares of the residuals made in the results of every single equation.<br/>
The most important application is in data fitting. The best fit in the least-squares sense minimizes the sum of squared residuals (a residual being: the difference between an observed value, and the fitted value provided by a model). When the problem has substantial uncertainties in the independent variable (the x variable), then simple regression and least-squares methods have problems; in such cases, the methodology required for fitting errors-in-variables models may be considered instead of that for least squares.<br/>

### Why:
Advantages of LS:<br/>
1. Simplicity: It is very easy to explain and to understand
2. Applicability: There are hardly any applications where least squares doesn’t make sense
3. Theoretical Underpinning: It is the maximum-likelihood solution and, if the Gauss-Markov conditions apply, the best linear unbiased estimator


Disadvantages of LS:<br/>
1. Sensitivity to outliers
2. Test statistics might be unreliable when the data is not normally distributed (but with many datapoints that problem gets mitigated)
3. Tendency to overfit data (LASSO or Ridge Regression might be advantageous)

### How:
The code has been written in LS.py.

### References:<br/>
https://en.wikipedia.org/wiki/Least_squares<br/>
https://www.quora.com/What-are-the-advantages-and-disadvantages-of-least-square-approximation<br/>
https://zhuanlan.zhihu.com/p/38128785<br/>
