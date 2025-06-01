import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

# 1. 데이터 불러오기
df_ev = pd.read_csv('Electric_Vehicle_Population_Data.csv')
df_hist = pd.read_csv('Electric_Vehicle_Population_Size_History_By_County_.csv')

# 2. 카운티별 “평균 EV 주행거리(Avg_EV_Range)” 계산
df_ev_range = df_ev[['County','State','Electric Range']].dropna()
df_range = df_ev_range.groupby(['County','State'])['Electric Range']\
                     .mean().reset_index(name='Avg_EV_Range')

# 3. “Percent Electric Vehicles” (2023년 12월 31일 데이터 추출)
df_hist23 = df_hist[df_hist['Date'] == 'December 31 2023']\
                [['County','State','Percent Electric Vehicles']]\
                .rename(columns={'Percent Electric Vehicles':'EV_Percent_2023'})

# 4. 두 데이터셋 병합 (카운티, 주 기준)
df_merged = df_range.merge(df_hist23, on=['County','State'], how='inner')\
                    .dropna(subset=['Avg_EV_Range','EV_Percent_2023'])

# 5. 기술 통계량
desc_stats = df_merged[['Avg_EV_Range','EV_Percent_2023']].describe()
print("Descriptive Statistics:\n", desc_stats)

# 6. 산점도: Avg_EV_Range vs EV_Percent_2023
plt.figure(figsize=(8,6))
sns.scatterplot(
    x='Avg_EV_Range',
    y='EV_Percent_2023',
    data=df_merged,
    s=70,
    alpha=0.7
)
plt.title('County-Level Average EV Range vs EV Percent (Dec 31, 2023)')
plt.xlabel('Average EV Range (miles)')
plt.ylabel('EV Percent (%)')
plt.grid(linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# 7. Pearson 상관분석
r, p_val = stats.pearsonr(df_merged['Avg_EV_Range'], df_merged['EV_Percent_2023'])
print(f"Pearson r = {r:.4f}, p-value = {p_val:.4f}")

# 8. 그룹 비교 (Low vs High Range) - t-검정
median_range = df_merged['Avg_EV_Range'].median()
high_group = df_merged[df_merged['Avg_EV_Range'] >= median_range]['EV_Percent_2023']
low_group  = df_merged[df_merged['Avg_EV_Range'] <  median_range]['EV_Percent_2023']

# 정규성 검정 (Shapiro)
sw_high = stats.shapiro(high_group)
sw_low  = stats.shapiro(low_group)

# 등분산성 검정 (Levene’s)
lev_stat, lev_p = stats.levene(high_group, low_group)

# t-검정 (equal_var 여부 결정)
t_stat, t_p = stats.ttest_ind(high_group, low_group, equal_var=(lev_p > 0.05))
print("Shapiro (High):", sw_high)
print("Shapiro (Low) :", sw_low)
print("Levene’s     :", lev_stat, lev_p)
print("T-test       :", t_stat, t_p)

# 박스플롯
plt.figure(figsize=(8,6))
sns.boxplot(
    x=pd.cut(df_merged['Avg_EV_Range'],
             bins=[df_merged['Avg_EV_Range'].min(), median_range, df_merged['Avg_EV_Range'].max()],
             labels=['Low Range','High Range']),
    y='EV_Percent_2023',
    data=df_merged,
    palette='pastel'
)
plt.title('EV Percent by Low vs High Avg EV Range Counties')
plt.xlabel('Avg EV Range Group')
plt.ylabel('EV Percent (%)')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# 9. 회귀분석: EV_Percent_2023 ~ Avg_EV_Range
X = sm.add_constant(df_merged['Avg_EV_Range'])
y = df_merged['EV_Percent_2023']
model = sm.OLS(y, X).fit()
print(model.summary())

plt.figure(figsize=(8,6))
sns.regplot(
    x='Avg_EV_Range',
    y='EV_Percent_2023',
    data=df_merged,
    scatter_kws={'s':50, 'alpha':0.7},
    line_kws={'color':'red'}
)
plt.title('Regression: EV Percent vs Avg EV Range')
plt.xlabel('Average EV Range (miles)')
plt.ylabel('EV Percent (%)')
plt.grid(linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
