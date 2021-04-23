## 时间序列分析Time series analysis(TSA)

### What:
Time series analysis comprises methods for analyzing time series data in order to extract meaningful statistics and other characteristics of the data. Time series forecasting is the use of a model to predict future values based on previously observed values. While regression analysis is often employed in such a way as to test relationships between one more different time series, this type of analysis is not usually called "time series analysis," which refers in particular to relationships between different points in time within a single series. Interrupted time series analysis is used to detect changes in the evolution of a time series from before to after some intervention which may affect the underlying variable.<br/>

### Why:
Advantages of TSA:
1. Temporal effects (that is, the effects of time passing) are literally everywhere in whatever you want to call “problem solving using data” (data science, machine learning, applied statistics…).
2. Hypothetically speaking the “best” way to deal with temporal effects is time series analysis.
3. As a practitioner, you work in of the hardest and most fascinating areas in what we do. Other data scientists have to deal with extrapolation from, e.g., covariate shift that is hypothetically detectable and often only happens in certain cases. When one is dealing with time, you’re looking at “How does one deal with events that may or may not occur?”, black and grey swan effects, and the like.
4. Most machine learning algorithms don’t deal with time well. (Advantage if you like research and ripping algorithms apart and altering and adjusting for this kind of thing like I do.)

Disadvantages of TSA:
1. Time series methods draw on vastly different areas in statistics, and lately, machine learning. You have to know a lot about all of these things, in general, to make sense of what you’re doing. There is no real unification of the theory, either.
2. Often there are ways around getting a model that is time-series based where the predictions are almost as good and is faster to implement. Note that this may or may not blow up in your face later on. In some cases, however, temporal effects are so weak that it makes more sense to just use the non-temporal ones… which can be difficult to explain (the need to check) to a manager if we’ve had to spend 2.5 weeks setting up the tests for temporal effects. Personal experience here.
This is hard stuff, and if you’re not motivated by challenge, you can get overwhelmed. Also, there is, in some other areas of data science, the notion that all we use are ARIMA models and EWMA; while we do often use these tools, we also use RNN and LTSM networks and a whole lot of interesting things.
3. Most machine learning algorithms don’t deal with time well. (Disadvantage if this isn’t cool to you.)

### How:
You can analyze the data in this website https://spssau.com/index.html<br/>
Or if you would like to know more about how to implement this model by using python. Please refer to this https://github.com/aarshayj/analytics_vidhya/blob/master/Articles/Time_Series_Analysis/Time_Series_AirPassenger.ipynb<br/>

### References:
https://en.wikipedia.org/wiki/Time_series<br/>
https://www.quora.com/What-is-time-series-analysis-What-are-its-advantages-and-disadvantages<br/>
https://www.machinelearningplus.com/time-series/time-series-analysis-python/<br/>
https://www.bilibili.com/video/BV12T4y1u7L3<br/>

