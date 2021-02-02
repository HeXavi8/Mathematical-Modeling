## 逻辑回归Logistic regression(LR)

### What:
In statistics, the logistic model (or logit model) is used to model the probability of a certain class or event existing such as pass/fail, win/lose, alive/dead or healthy/sick. This can be extended to model several classes of events such as determining whether an image contains a cat, dog, lion, etc. Each object being detected in the image would be assigned a probability between 0 and 1, with a sum of one.<br/>
Logistic regression is a statistical model that in its basic form uses a logistic function to model a binary dependent variable, although many more complex extensions exist. In regression analysis, logistic regression[1] (or logit regression) is estimating the parameters of a logistic model (a form of binary regression). Mathematically, a binary logistic model has a dependent variable with two possible values, such as pass/fail which is represented by an indicator variable, where the two values are labeled "0" and "1". In the logistic model, the log-odds (the logarithm of the odds) for the value labeled "1" is a linear combination of one or more independent variables ("predictors"); the independent variables can each be a binary variable (two classes, coded by an indicator variable) or a continuous variable (any real value). The corresponding probability of the value labeled "1" can vary between 0 (certainly the value "0") and 1 (certainly the value "1"), hence the labeling; the function that converts log-odds to probability is the logistic function, hence the name. The unit of measurement for the log-odds scale is called a logit, from logistic unit, hence the alternative names. Analogous models with a different sigmoid function instead of the logistic function can also be used, such as the probit model; the defining characteristic of the logistic model is that increasing one of the independent variables multiplicatively scales the odds of the given outcome at a constant rate, with each independent variable having its own parameter; for a binary dependent variable this generalizes the odds ratio.<br/>

### Why:
Advantages of LR:<br/>
1. Logistic regression is easier to implement, interpret, and very efficient to train.<br/>
2. It makes no assumptions about distributions of classes in feature space.<br/>
3. It can easily extend to multiple classes(multinomial regression) and a natural probabilistic view of class predictions.<br/>
4. It not only provides a measure of how appropriate a predictor(coefficient size)is, but also its direction of association (positive or negative).<br/>
5. It is very fast at classifying unknown records.<br/>
6. Good accuracy for many simple data sets and it performs well when the dataset is linearly separable.
7. It can interpret model coefficients as indicators of feature importance.
8. Logistic regression is less inclined to over-fitting but it can overfit in high dimensional datasets.One may consider Regularization (L1 and L2) techniques to avoid over-fittingin these scenarios.

Disadvantages of LR:<br/>
1. If the number of observations is lesser than the number of features, Logistic Regression should not be used, otherwise, it may lead to overfitting.
2. It constructs linear boundaries.
3. The major limitation of Logistic Regression is the assumption of linearity between the dependent variable and the independent variables.
4. It can only be used to predict discrete functions. Hence, the dependent variable of Logistic Regression is bound to the discrete number set.
5. Non-linear problems can’t be solved with logistic regression because it has a linear decision surface. Linearly separable data is rarely found in real-world scenarios.
6. Logistic Regression requires average or no multicollinearity between independent variables.
7. It is tough to obtain complex relationships using logistic regression. More powerful and compact algorithms such as Neural Networks can easily outperform this algorithm.
8. In Linear Regression independent and dependent variables are related linearly. But Logistic Regression needs that independent variables are linearly related to the log odds (log(p/(1-p)).

### How:
A sample has been written in LR.py.<br/>

### References:<br/>
https://en.wikipedia.org/wiki/Logistic_regression<br/>
https://www.geeksforgeeks.org/advantages-and-disadvantages-of-logistic-regression/<br/>
https://blog.csdn.net/zouxy09/article/details/20319673<br/>
https://www.jianshu.com/p/4cfb4f734358<br/>
