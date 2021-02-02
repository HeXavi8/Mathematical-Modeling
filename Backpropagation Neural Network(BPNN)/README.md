## BP神经网络Backpropagation Neural Network(BPNN)

### What:
The back propagation (BP) neural network algorithm is a multi-layer feedforward network trained according to error back propagation algorithm and is one of the most widely applied neural network models. BP network can be used to learn and store a great deal of mapping relations of input-output model, and no need to disclose in advance the mathematical equation that describes these mapping relations. Its learning rule is to adopt the steepest descent method in which the back propagation is used to regulate the weight value and threshold value of the network to achieve the minimum error sum of square. <br/>
Two Types of Backpropagation Networks are:<br/>
* Static Back-propagation<br/>
* Recurrent Backpropagation<br/>

### Why:
Advantages of BPNN:<br/>
1. Backpropagation is fast, simple and easy to program<br/>
2. It has no parameters to tune apart from the numbers of input<br/>
3. It is a flexible method as it does not require prior knowledge about the network<br/>
4. It is a standard method that generally works well<br/>
5. It does not need any special mention of the features of the function to be learned

Disadvantages of BPNN:<br/>
1. Perhaps the best known is called “Local Minima”. This occurs because the algorithm always changes the weights in such a way as to cause the error to fall. But the error might briefly have to rise as part of a more general fall, If this is the case, the algorithm will “get stuck” (because it can‟t go uphill) and the error will not decrease further.
2. Network paralysis occurs when the weights are adjusted to very large values during training, large weights can force most of the units to operate at extreme values, in a region where the derivative of the activation function is very small.
3. A multilayer neural network requires many repeated presentations of the input patterns, for which the weights need to be adjusted before the network is able to settle down into an optimal solution.

### How:
The code has been written in BPNN.py.<br/>

### References:<br/>
https://link.springer.com/chapter/10.1007/978-3-642-30223-7_87<br/>
https://www.quora.com/What-are-the-advantages-and-disadvantages-of-training-artificial-neural-nets-via-back-propagation-a-probabilistic-hill-climbing-algorithm-a-combination-of-the-two-and-other-methods-if-they-exist<br/>
https://machinelearningmastery.com/implement-backpropagation-algorithm-scratch-python/<br/>
