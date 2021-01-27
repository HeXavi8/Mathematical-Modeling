## 马尔科夫链蒙特卡洛方法Markov chain Monte Carlo(MCMC)

### what:
In statistics, Markov chain Monte Carlo (MCMC) methods comprise a class of algorithms for sampling from a probability distribution. By constructing a Markov chain that has the desired distribution as its equilibrium distribution, one can obtain a sample of the desired distribution by recording states from the chain. The more steps are included, the more closely the distribution of the sample matches the actual desired distribution. Various algorithms exist for constructing chains, including the Metropolis–Hastings algorithm.<br/>

### why:
Advantages of MCMC method:<br/>
1. Very automatic: lack of tunable free parameters, proposal distribution, etc.<br/>
2. No rejections<br/>
3. Great choice when there is little knowledge about the distribution we are sampling from<br/>

Disadvantages of MCMC method:<br/>
There are also some disadvantages. When it goes to multidimensional distribution, one may sample each
variable in turn using 1D slice sampling, in a manner similar to Gibbs sampling. However, this method
severely suffer from complication introduced by dimensionality<br/>

### how:
The code has been written in MCMC.py.<br/>

references:<br/>
https://en.wikipedia.org/wiki/Markov_chain_Monte_Carlo<br/>
https://www.cs.cmu.edu/~epxing/Class/10708-15/notes/10708_scribe_lecture17.pdf<br/>
https://towardsdatascience.com/markov-chain-monte-carlo-in-python-44f7e609be98<br/>
https://machinelearningmastery.com/markov-chain-monte-carlo-for-probability/<br/>
https://www.cnblogs.com/sddai/p/6144674.html<br/>
