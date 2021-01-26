# Mathematical-Modeling

A sharing of the learning process of mathematical modeling

---

## 1.AHP

### what:
Analytic hierarchy process (AHP) is a decision analysis method which combines qualitative and quantitative methods to solve multi-objective complex problems. This method combines quantitative analysis with qualitative analysis, uses the experience of decision-makers to judge the relative importance of the standards to measure whether the objectives can be achieved or not, and reasonably gives the weight of each standard of each decision-making scheme, and uses the weight to calculate the priority of each scheme, which is more effectively applied to those problems that are difficult to be solved by quantitative methods.

### why:
AHP法 的优点：<br/>
1. 面对有层次结构的整体问题综合评价，逐层分解，然后在多个但准则评价的基础上进行综合<br/>
2. 简单实用，将定性与定量的方法结合起来<br/>
3. 所需定量数据较少<br/>

AHP法 的缺点：<br/>
1. 只能在给定的策略中选择最优的，而不能给出新的策略<br/>
2. AHP中所用的指标体系需要有专家系统的支持，如果给出的指标不合理，则得到的结果就会不正确<br/>
3. AHP进行多层比较时需要进行一致性检查，如果不满足一致性要求，那么AHP方法也就失去了作用<br/>
4. AHP方法需要求矩阵的特征值，对于某些病态矩阵来说，求出的特征值会有系统误差<br/>

Advantages of AHP method:<br/>
1. In the face of the comprehensive evaluation of the overall problem with hierarchical structure, it decomposes layer by layer, and then makes a comprehensive evaluation on the basis of multiple criteria <br/>
2. Simple and practical, combining qualitative and quantitative methods <br/>
3. Less quantitative data are needed <br/>

Disadvantages of AHP method:<br/>
1. We can only choose the best strategy from the given one, but can't give a new strategy <br/>
2. The index system used in AHP needs the support of expert system. If the index given is unreasonable, the result will be incorrect <br/>
3. Consistency check is needed when AHP is used for multi-layer comparison. If the consistency requirement is not met, the AHP method will lose its function <br/>
4. AHP method needs to find the eigenvalues of matrix. For some ill conditioned matrices, the eigenvalues will have systematic error <br/>

### how:
The code has been written in AHP.py. Please download them both if you wanna try out.<br/>

reference:<br/>
https://zhuanlan.zhihu.com/p/101505929?utm_source=wechat_session<br/>
https://baike.baidu.com/item/%E5%B1%82%E6%AC%A1%E5%88%86%E6%9E%90%E6%B3%95/1672?fr=aladdin<br/>
https://blog.csdn.net/mmm_jsw/article/details/84863416<br/>


## 2.优劣解距离法Topsis

### what:
The Technique for Order of Preference by Similarity to Ideal Solution (TOPSIS) is a multi-criteria decision analysis method, which was originally developed by Ching-Lai Hwang and Yoon in 1981 with further developments by Yoon in 1987, and Hwang, Lai and Liu in 1993. TOPSIS is based on the concept that the chosen alternative should have the shortest geometric distance from the positive ideal solution (PIS) and the longest geometric distance from the negative ideal solution (NIS).

### why:
Topsis法 的优点：<br/>
1. 避免了数据的主观性，不需要目标函数，不用通过检验，而且能够很好的刻画多个影响指标的综合影响力度<br/>
2. 对于数据分布及样本量、指标多少无严格限制，既适于小样本资料，也适于多评价单元、多指标的大系统,较为灵活、方便<br/>

Topsis法 的缺点：<br/>
1. 需要的每个指标的数据，对应的量化指标选取会有一定难度<br/>
2. 不确定指标的选取个数为多少适宜，才能够去很好刻画指标的影响力度<br/>
3. 必须有两个以上的研究对象才可以进行使用<br/>

Advantages of TOPSIS method:<br/>
1. It avoids the subjectivity of the data, does not need the objective function, does not need to pass the test, and can well describe the comprehensive impact of multiple impact indicators<br/>
2. There is no strict restriction on the data distribution, sample size and the number of indicators. It is flexible and convenient for both small sample data and large system with multiple evaluation units and multiple indicators<br/>

Disadvantages of TOPSIS method:<br/>
1. As for the required data of each index, it will be somewhat difficult to select the corresponding quantitative index<br/>
2. Only by selecting the appropriate number of uncertain indicators can we describe the influence of indicators well<br/>
3. There must be more than two research objects before it can be used<br/>

### how:
The code has been written in Topsis.py and topsis.xlsx is the data file. Please download them both if you wanna try out.<br/>

references:<br/>
https://en.wikipedia.org/wiki/TOPSIS<br/>
https://www.it610.com/article/1293378434029920256.htm<br/>
https://blog.csdn.net/weixin_41799019/article/details/97611462<br/>
https://blog.csdn.net/weixin_44830815/article/details/105603566<br/>


## 3.秩和比综合分析法Rank-sum ratio(RSR)

### what:
秩和比法（Rank-sum ratio，简称RSR法），是我国学者、原中国预防医学科学院田凤调教授于1988年提出的，集古典参数统计与近代非参数统计各自优点于一体的统计分析方法，它不仅适用于四格表资料的综合评价，也适用于行×列表资料的综合评价，同时也适用于计量资料和分类资料的综合评价。<br/>
其基本思想是在一个 n 行（n 评价对象）p 列（p 个评价指标）矩阵中，通过秩转换，获得无量纲的统计量RSR，以RSR值对评价对象的优劣进行排序或分档排序。秩和比的值能够包含所有评价指标的信息，显示出这些评价指标的综合水平，RSR值越大表明综合评价越优。<br/>
Rank-sum ratio (RSR method), proposed by Chinese scholar Tian Fengtiao of the Chinese Academy of Preventive Medicine in 1988, is a statistical analysis that combines the advantages of classical parameter statistics and modern non-parametric statistics. It is not only suitable for the comprehensive evaluation of four-grid table data, but also for the comprehensive evaluation of row×list data, and also for the comprehensive evaluation of measurement data and classified data.<br/>
The basic idea is to obtain a dimensionless statistic RSR in a matrix of n rows (n evaluation objects) and p columns (p evaluation indicators) through rank conversion, and rank or classify the evaluation objects according to the RSR value. Sort. The value of the rank-sum ratio can contain the information of all evaluation indicators and show the comprehensive level of these evaluation indicators. The larger the RSR value, the better the comprehensive evaluation. <br/>

### why:
Rank-sum ratio(RSR)法 的优点：<br/>
1. 秩和比是一个新的统计量，是复合信息的载体，容量大，可塑性强。<br/>
2. 秩和比法是一种全新的广谱的实用数量方法，或称统计信息方法，集参数统计与非参数统计于一身，有描述、有推断，能提高统计分析与再分析的水平，满足人们在统计研究与统计管理中的种种需求，因此，我们说秩和比法是数量方法的创新，有着极为宽广的发展前景。<br/>
3. 秩和比法的关键步骤是秩代换，具有强大的统计信息功能，针对性强，柔韧性大，操作简便，应用价值高。<br/>
4. 通过移植、嫁接。利用求得的秩和比值，可以四通八达。本法在量化研究中占有重要位置，粗中有细，细中有粗，相互对照，规律、特征自然明，是做比较、找关系的有效手段。<br/>

Rank-sum ratio(RSR)法 的缺点：<br/>
1. 排序的主要依据是利用原始数据的秩次，最终算得的RSR值反映的是综合秩次的差距，而与原始数据的顺位间的差距程度大小无关，这样在指标转化为秩次是会失去一些原始数据的信息，如原始数据的大小差别等。

The advantages of Rank-sum ratio(RSR)<br/>
1. The rank sum ratio is a new statistic, a carrier of compound information, with large capacity and strong plasticity.<br/>
2. The rank-sum ratio method is a new broad-spectrum practical quantitative method, or statistical information method, which integrates parametric statistics and non-parametric statistics. It has description and inference. It can improve the level of statistical analysis and re-analysis and satisfy people. There are various demands in statistical research and statistical management. Therefore, we say that the rank-sum ratio method is an innovation of quantitative methods and has extremely broad development prospects.<br/>
3. The key step of the rank-sum ratio method is rank substitution, which has powerful statistical information functions, strong pertinence, flexibility, simple operation and high application value.<br/>
4. Through transplantation and grafting. Using the obtained rank sum ratio, you can reach in all directions. This method occupies an important position in quantitative research. There are details in roughness and roughness in fineness. The rules and characteristics are natural and clear. It is an effective means for comparison and finding relationships.<br/>

The disadvantages of Rank-sum ratio(RSR)<br/>
1. The disadvantage of the rank-sum ratio evaluation method is that the main basis for ranking is the rank of the original data. The final calculated RSR value reflects the difference in the overall rank, and has nothing to do with the degree of the difference between the original data. When the indicator is converted to rank, some information of the original data will be lost, such as the size difference of the original data.<br/>

### how:
The code has been written in Rank-sum ratio(RSR).py .<br/>

references:<br/>
https://baike.baidu.com/item/%E7%A7%A9%E5%92%8C%E6%AF%94%E6%B3%95/2805901?fr=aladdin<br/>
https://zhuanlan.zhihu.com/p/38209882<br/>
https://baike.baidu.com/item/%E7%A7%A9%E5%92%8C%E6%AF%94%E6%B3%95/2805901#1<br/>

## 4.熵权法the entropy weight method(EWM) 

### what:
Entropy weight method (EWM) is a commonly used weighting method that measures value dispersion in decision-making. The greater the degree of dispersion, the greater the degree of differentiation, and more information can be derived. Meanwhile, higher weight should be given to the index, and vice versa.<br/>

### why:
The advantages of Entropy weight method (EWM)<br/>
1. the biggest advantage of the EWM is theavoidance of the interference of human factors on the weightof indicators, thus enhancing the objectivity of the com-prehensive evaluation results. Therefore, the EWM hasbeen widely used in decision-making in recent years.

The disadvantages of Entropy weight method (EWM)<br/>
1. EWM only considered the numerical discrimination degree andignored the rank discrimination degree of the index. 

### how:
The code has been written in EWM.py and the test data is in ewm.csv.<br/>

references:<br/>
https://www.hindawi.com/journals/mpe/2020/3564835/<br/>
https://www.researchgate.net/publication/340232284_Effectiveness_of_Entropy_Weight_Method_in_Decision-Making
https://baike.baidu.com/item/%E7%86%B5%E6%9D%83%E6%B3%95/5616693?fr=aladdin
https://www.zhihu.com/question/357680646/answer/943628631</br>
https://www.bilibili.com/video/bv1qt4y1276a<br/>
