## 马尔科夫链Markov Chain(MC)

### what:
A Markov chain is a mathematical system that experiences transitions from one state to another according to certain probabilistic rules. The defining characteristic of a Markov chain is that no matter how the process arrived at its present state, the possible future states are fixed. In other words, the probability of transitioning to any particular state is dependent solely on the current state and time elapsed. The state space, or set of all possible states, can be anything: letters, numbers, weather conditions, baseball scores, or stock performances.<br/>

### why:
Advantages of MC :<br/>
Markov analysis has the advantage of being an analytical method which means that the reliability parameters for the system are calculated in effect by a formula. This has the considerable advantages of speed and accuracy when producing results. Speed is especially useful when investigating many alternative variations of design or exploring a range of sensitivities. In contrast accuracy is vitally important when investigating small design changes or when the reliability or availability of high integrity systems are being quantified. Markov analysis has a clear advantage over MCS in respect of speed and accuracy since MCS requires longer simulation runs to achieve higher accuracy and, unlike Markov analysis, does not produce an “exact” answer.<br/>

Disadvantages of MC :<br/>
As in the case of applying MCS, Markov analysis requires great care during the model building phase since model accuracy is all-important in obtaining valid results. The assumptions implicit in Markov models that are associated with memorilessness and the Exponential distribution to represent times to failure and repair provide additional constraints to those within MCS. Markov models can therefore become somewhat contrived if these implicit assumptions do not reflect sufficiently well the characteristics of a system and how it functions in practice. In order to gain the benefits of speed and accuracy that it can offer, Markov analysis depends to a greater extent on the experience and judgement of the modeller than MCS. Also, whilst MCS is a safer and more flexible approach, it does not always offer the speed and accuracy that may be required in particular system studies.<br/>

### how:
The code has been written in MC.py. Please download them both if you wanna try out.<br/>

reference:<br/>
https://brilliant.org/wiki/markov-chains/<br/>
https://egertonconsulting.com/markov-analysis-brief-introduction/?doing_wp_cron=1611713777.6825981140136718750000
https://www.zhihu.com/question/26665048/answer/551925518<br/>
