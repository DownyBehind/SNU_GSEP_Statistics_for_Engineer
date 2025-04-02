import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

# 데이터 입력
data = [87, 106, 87, 127, 95, 114, 109, 94, 111, 110,
        95, 87, 77, 91, 119, 102, 86, 110, 110, 94,
        140, 92, 107, 101, 103, 104, 111, 94, 93, 94,
        109, 98, 102, 120, 108, 93, 102, 93, 77, 97,
        101, 82, 98, 101, 98, 90, 101, 88, 81, 114]

# 평균과 분산 계산
mean = np.mean(data)
variance = np.var(data, ddof=1)
std_dev = np.std(data, ddof=1)

# 정규성 검정 (Shapiro-Wilk Test)
shapiro_stat, shapiro_p = stats.shapiro(data)

# 시각화와 함께 텍스트 출력 포함한 전체 코드

# 평균, 분산, 표준편차, p-value 출력
print(f"📊 평균 (Mean): {mean:.2f}")
print(f"📈 분산 (Variance): {variance:.2f}")
print(f"📉 표준편차 (Standard Deviation): {std_dev:.2f}")
print(f"🧪 Shapiro-Wilk 정규성 검정 p-value: {shapiro_p:.4f}")

# 히스토그램과 KDE
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
sns.histplot(data, kde=True, bins=10, color='skyblue')
plt.axvline(mean, color='red', linestyle='--', label=f'Mean = {mean:.2f}')
plt.title('Histogram with KDE')
plt.legend()

# Q-Q Plot
plt.subplot(1, 2, 2)
stats.probplot(data, dist="norm", plot=plt)
plt.title("Q-Q Plot")

plt.tight_layout()
plt.show()