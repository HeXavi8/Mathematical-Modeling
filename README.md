# Mathematical-Modeling

A sharing of the learning process of mathematical modeling

---

## 1.AHP


## 2.Topsis
### what:
The Technique for Order of Preference by Similarity to Ideal Solution (TOPSIS) is a multi-criteria decision analysis method, which was originally developed by Ching-Lai Hwang and Yoon in 1981 with further developments by Yoon in 1987, and Hwang, Lai and Liu in 1993. TOPSIS is based on the concept that the chosen alternative should have the shortest geometric distance from the positive ideal solution (PIS) and the longest geometric distance from the negative ideal solution (NIS).
### why:
Topsis法 的优点：<br/>
1.避免了数据的主观性，不需要目标函数，不用通过检验，而且能够很好的刻画多个影响指标的综合影响力度<br/>
2.对于数据分布及样本量、指标多少无严格限制，既适于小样本资料，也适于多评价单元、多指标的大系统,较为灵活、方便<br/>
Topsis法 的缺点：<br/>
1.需要的每个指标的数据，对应的量化指标选取会有一定难度<br/>
2.不确定指标的选取个数为多少适宜，才能够去很好刻画指标的影响力度<br/>
3.必须有两个以上的研究对象才可以进行使用<br/>
Advantages of TOPSIS method:<br/>
1.It avoids the subjectivity of the data, does not need the objective function, does not need to pass the test, and can well describe the comprehensive impact of multiple impact indicators<br/>
2.There is no strict restriction on the data distribution, sample size and the number of indicators. It is flexible and convenient for both small sample data and large system with multiple evaluation units and multiple indicators<br/>
Disadvantages of TOPSIS method:<br/>
1.As for the required data of each index, it will be somewhat difficult to select the corresponding quantitative index<br/>
2.Only by selecting the appropriate number of uncertain indicators can we describe the influence of indicators well<br/>
3.There must be more than two research objects before it can be used<br/>
### how:
The code has been written in Topsis.py and topsis.xlsx is the data file. Please download them both if you wanna try out.<br/>


reference:<br/>
https://en.wikipedia.org/wiki/TOPSIS<br/>
https://www.it610.com/article/1293378434029920256.htm<br/>
https://blog.csdn.net/weixin_41799019/article/details/97611462<br/>
https://blog.csdn.net/weixin_44830815/article/details/105603566<br/>

## 3.秩和比综合分析法Rank-sum ratio(RSR)

其基本思想是在一个 n 行（n 评价对象）p 列（p 个评价指标）矩阵中，通过秩转换，获得无量纲的统计量RSR，以RSR值对评价对象的优劣进行排序或分档排序。秩和比的值能够包含所有评价指标的信息，显示出这些评价指标的综合水平，RSR值越大表明综合评价越优。<br/>
The basic idea of RSR is to get the dimensionless statistic RSR in a matrix of n rows (n evaluation objects) and p columns (p evaluation indexes) by rank transformation, and then sort the evaluation objects by RSR value.The value of rank to sum ratio can contain the information of all evaluation indexes and show the comprehensive level of these evaluation indexes. The larger the RSR value is, the better the comprehensive evaluation is.<br/>

reference:<br/>
https://zhuanlan.zhihu.com/p/38209882<br/>
https://baike.baidu.com/item/%E7%A7%A9%E5%92%8C%E6%AF%94%E6%B3%95/2805901#1<br/>
