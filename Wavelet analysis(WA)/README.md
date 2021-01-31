## 小波分析Wavelet analysis(WA)

### What:
A wavelet is a wave-like oscillation with an amplitude that begins at zero, increases, and then decreases back to zero. It can typically be visualized as a "brief oscillation" like one recorded by a seismograph or heart monitor. Generally, wavelets are intentionally crafted to have specific properties that make them useful for signal processing.br/>

### Why:
The advantages of WA:
1. A wavelet transform can be used to decompose or divide a signal into small wavelets and in wavelet theory, it is possible to obtain a good estimation of the given function f by using only a few coefficients which is a great attainment as compared to Fourier transform.
2. One of the main advantages of wavelets is that they provide a concurrent fixing or localization in domain of time and frequency. Wavelets also use fast wavelet transform, so it is very fast.
3. Wavelet transform can frequently squeeze or de-noise a signal in absence of considerable degradation.
4. Wavelets have the advantage of being able to divide the pure details in a signal. Smaller wavelets can be applied to dissociate the most elementary details in a signal, while very large wavelets can identify other details of coarse analysis.
5. Wavelet theory is competent to declare aspects of data that other signal analysis method misses. The features like breakdown points and segregation in higher order derivatives are perfect example for this. 

The disadvantages of WA:
1. The selection of wavelet basis is very difficult.
2. For signals whose properties are stable over time, the ideal tool for processing is still Fourier analysis.

### How:
A sample of wavelet transform has been written in wavelet_transform.py.<br/>
Some types of wavelets have been written in Some_types_of_wavelets.py.<br/>
If you would like to know more about the details and code, you can refer to this website https://ataspinar.com/2018/12/21/a-guide-for-using-the-wavelet-transform-in-machine-learning/<br/>

### References:
https://en.wikipedia.org/wiki/Wavelets<br/>
https://ataspinar.com/2018/12/21/a-guide-for-using-the-wavelet-transform-in-machine-learning/<br/>
https://zhuanlan.zhihu.com/p/22450818<br/>
http://users.rowan.edu/~polikar/WTtutorial.html<br/>
https://www.krishisanskriti.org/ElectricalandElectronics/paper%208.pdf<br/>


