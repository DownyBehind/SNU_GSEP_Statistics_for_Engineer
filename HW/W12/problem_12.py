import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from statsmodels.stats.diagnostic import het_breuschpagan
from scipy import stats

# Load dataset
file_path = 'HW_13_statisticalpuzzle.txt'
df = pd.read_csv(file_path, delim_whitespace=True)

# Separate predictors and response
Y = df['y']
X = df.drop(columns=['y'])
X = sm.add_constant(X)  # add intercept

# Fit multiple regression model
model = sm.OLS(Y, X).fit()

# Display model summary
print(model.summary())

# Obtain fitted values and residuals
fitted = model.fittedvalues
residuals = model.resid

# Residuals vs Fitted plot
plt.figure()
plt.scatter(fitted, residuals)
plt.axhline(0)
plt.xlabel("Fitted values")
plt.ylabel("Residuals")
plt.title("Residuals vs Fitted")
plt.show()

# QQ plot for residuals
sm.qqplot(residuals, line='45')
plt.title("QQ Plot of Residuals")
plt.show()

# Histogram of residuals
plt.figure()
plt.hist(residuals, bins=30)
plt.title("Histogram of Residuals")
plt.xlabel("Residuals")
plt.ylabel("Frequency")
plt.show()

# Breusch-Pagan test for heteroscedasticity
bp_test = het_breuschpagan(residuals, X)
labels = ['Lagrange multiplier statistic', 'p-value', 'f-value', 'f p-value']
print("Breusch-Pagan test results:", dict(zip(labels, bp_test)))

# Jarque-Bera test for normality
jb_stat, jb_pvalue = stats.jarque_bera(residuals)
print(f"Jarque-Bera test: stat = {jb_stat:.4f}, p-value = {jb_pvalue:.4f}")
