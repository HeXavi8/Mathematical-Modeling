## 马尔科夫链蒙特卡洛方法Markov chain Monte Carlo(MCMC)

### What:
In statistics, Markov chain Monte Carlo (MCMC) methods comprise a class of algorithms for sampling from a probability distribution. By constructing a Markov chain that has the desired distribution as its equilibrium distribution, one can obtain a sample of the desired distribution by recording states from the chain. The more steps are included, the more closely the distribution of the sample matches the actual desired distribution. Various algorithms exist for constructing chains, including the **Metropolis–Hastings algorithm** and **Gibbs Sampling**.<br/>

### Why:
Advantages of Gibbs sampling:<br/>
1. It is easy to evaluate the conditional distributions,<br/>
2. Conditionals may be conjugate and we can sample from them exactly, <br/>
3. Conditionals will be lower dimensional and we can apply rejection sampling or importance sampling. <br/>

Disadvantages of Gibbs sampling:<br/>
However, the major drawback is that when variables have strong dependencies it is hard to move around. We can introduce auxiliary variables to help move around when such high dimensional variables are correlated.<br/>

### How:
The code has been written in Metropolis–Hastings.py and Gibbs_Sampling.py.<br/>

### References:<br/>
https://en.wikipedia.org/wiki/Markov_chain_Monte_Carlo<br/>
https://www.cs.cmu.edu/~epxing/Class/10708-15/notes/10708_scribe_lecture17.pdf<br/>
http://people.duke.edu/~ccc14/sta-663/MCMC.html<br/>
https://github.com/Joseph94m/MCMC/blob/master/MCMC.ipynb<br/>
https://towardsdatascience.com/markov-chain-monte-carlo-in-python-44f7e609be98<br/>
https://machinelearningmastery.com/markov-chain-monte-carlo-for-probability/<br/>
https://link.springer.com/article/10.3758/s13423-016-1015-8<br/>
https://www.cnblogs.com/sddai/p/6144674.html<br/>


### Tips:<br/>
We highly recommended you to refer these two references if you would like to know more details about MCMC.<br/>
https://www.cs.cmu.edu/~epxing/Class/10708-15/notes/10708_scribe_lecture17.pdf<br/>
https://towardsdatascience.com/markov-chain-monte-carlo-in-python-44f7e609be98<br/>
https://github.com/Joseph94m/MCMC/blob/master/MCMC.ipynb<br/>
