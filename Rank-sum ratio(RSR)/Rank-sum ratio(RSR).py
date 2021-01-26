import pandas as pd
import numpy as np
import statsmodels.api as sm
from scipy.stats import norm


def rsr(data, weight=None, threshold=None, full_rank=True):
	Result = pd.DataFrame()
	n, m = data.shape

	# Rank the original data
	if full_rank:
		for i, X in enumerate(data.columns):
			Result[f'X{str(i + 1)}：{X}'] = data.iloc[:, i]
			Result[f'R{str(i + 1)}：{X}'] = data.iloc[:, i].rank(method="dense")
	else:
		for i, X in enumerate(data.columns):
			Result[f'X{str(i + 1)}：{X}'] = data.iloc[:, i]
			Result[f'R{str(i + 1)}：{X}'] = 1 + (n - 1) * (data.iloc[:, i].max() - data.iloc[:, i]) / (data.iloc[:, i].max() - data.iloc[:, i].min())

	# Calculate rank sum ratio
	weight = 1 / m if weight is None else np.array(weight) / sum(weight)
	Result['RSR'] = (Result.iloc[:, 1::2] * weight).sum(axis=1) / n
	Result['RSR_Rank'] = Result['RSR'].rank(ascending=False)

	# Draw the RSR distribution table
	RSR = Result['RSR']
	RSR_RANK_DICT = dict(zip(RSR.values, RSR.rank().values))
	Distribution = pd.DataFrame(index=sorted(RSR.unique()))
	Distribution['f'] = RSR.value_counts().sort_index()
	Distribution['Σ f'] = Distribution['f'].cumsum()
	Distribution[r'\bar{R} f'] = [RSR_RANK_DICT[i] for i in Distribution.index]
	Distribution[r'\bar{R}/n*100%'] = Distribution[r'\bar{R} f'] / n
	Distribution.iat[-1, -1] = 1 - 1 / (4 * n)
	Distribution['Probit'] = 5 - norm.isf(Distribution.iloc[:, -1])

	# Calculate the regression variance and perform the regression analysis
	r0 = np.polyfit(Distribution['Probit'], Distribution.index, deg=1)
	print(sm.OLS(Distribution.index, sm.add_constant(Distribution['Probit'])).fit().summary())
	if r0[1] > 0:
		print(f"\nThe equation of the regression line is：y = {r0[0]} Probit + {r0[1]}")
	else:
		print(f"\nThe equation of the regression line is：y = {r0[0]} Probit - {abs(r0[1])}")

	# Substitute it into the regression equation and sort it
	Result['Probit'] = Result['RSR'].apply(lambda item: Distribution.at[item, 'Probit'])
	Result['RSR Regression'] = np.polyval(r0, Result['Probit'])
	threshold = np.polyval(r0, [2, 4, 6, 8]) if threshold is None else np.polyval(r0, threshold)
	Result['Level'] = pd.cut(Result['RSR Regression'], threshold, labels=range(len(threshold) - 1, 0, -1))

	return Result, Distribution


def rsrAnalysis(data, file_name=None, **kwargs):
	Result, Distribution = rsr(data, **kwargs)
	file_name = 'RSR analysis results report.xlsx' if file_name is None else file_name + '.xlsx'
	Excel_Writer = pd.ExcelWriter(file_name)
	Result.to_excel(Excel_Writer, 'Comprehensive evaluation results')
	Result.sort_values(by='Level', ascending=False).to_excel(Excel_Writer, 'Sort results')
	Distribution.to_excel(Excel_Writer, 'RSR distribution table')
	Excel_Writer.save()

	return Result, Distribution


data = pd.DataFrame({'Antenatal screening rate': [99.54, 96.52, 99.36, 92.83, 91.71, 95.35, 96.09, 99.27, 94.76, 84.80],
                     'Maternal mortality rate': [60.27, 59.67, 43.91, 58.99, 35.40, 44.71, 49.81, 31.69, 22.91, 81.49],
                     'Perinatal mortality': [16.15, 20.10, 15.60, 17.04, 15.01, 13.93, 17.43, 13.89, 19.87, 23.63]},
                    index=list('ABCDEFGHIJ'), columns=['Antenatal screening rate', 'Maternal mortality rate', 'Perinatal mortality'])
data["Maternal mortality rate"] = 1 / data["Maternal mortality rate"]
data["Perinatal mortality"] = 1 / data["Perinatal mortality"]
rsr(data)
