## 蒙特卡洛算法Monte Carlo method

### What:
Monte Carlo methods, or Monte Carlo experiments, are a broad class of computational algorithms that rely on repeated random sampling to obtain numerical results. The underlying concept is to use randomness to solve problems that might be deterministic in principle. They are often used in physical and mathematical problems and are most useful when it is difficult or impossible to use other approaches. Monte Carlo methods are mainly used in three problem classes:optimization, numerical integration, and generating draws from a probability distribution.<br/>

### Why:
Advantages of MCM:<br/>
1. Very flexible. There is virtually no limit to the analysis. Empirical distributions can be handled.<br/>
2. Can generally be easily extended and developed as required.<br/>
3. Easily understood by nonmathematicians.<br/>

Disadvantages of MCM:<br/>
1. Usually requires a computer.<br/>
2. Calculations can take much longer than analytical models.<br/>
3. Solutions are not exact, but depend on the number of repeated runs used to produce the output statistics. That is, all outputs are estimates. <br/>

### How:
The code has been written in MCMforPI.py which is to estimate the value of PI. And the MCMforFunction.py is to calculate the ratio of the area under the curve to the area of the square of y=x * x from 0.0 to 1.0 of x.<br/>

### References:<br/>
https://en.wikipedia.org/wiki/Monte_Carlo_method<br/>
https://sars.org.uk/BOK/Applied%20R&M%20Manual%20for%20Defence%20Systems%20(GR-77)/p4c04.pdf
https://blog.csdn.net/bitcarmanlee/article/details/82716641<br/>
