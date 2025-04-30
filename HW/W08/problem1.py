import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2

# 1. 정규분포 Z에서 10000개 샘플 생성
np.random.seed(0)
Z = np.random.normal(loc=0, scale=1, size=10000)

# 2. V = Z^2
V = Z**2

# 3. 밀도 그래프
plt.figure()
plt.hist(V, bins=100, density=True, alpha=0.6, label='Empirical V = Z^2')
x = np.linspace(0, 10, 1000)
plt.plot(x, chi2.pdf(x, df=1), 'r-', lw=2, label='Chi-square(df=1)')
plt.title('Density of V = Z^2')
plt.xlabel('V')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()

# 4. V < 1, V < 4의 비율 계산
prob_v_lt_1_empirical = np.mean(V < 1)
prob_v_lt_4_empirical = np.mean(V < 4)

# 5. 자유도 1인 chi-square 분포의 이론값과 비교
prob_v_lt_1_theoretical = chi2.cdf(1, df=1)
prob_v_lt_4_theoretical = chi2.cdf(4, df=1)

# 결과 출력
print(f"Empirical P(V < 1): {prob_v_lt_1_empirical:.4f}")
print(f"Theoretical P(V < 1) (Chi2 df=1): {prob_v_lt_1_theoretical:.4f}")
print()
print(f"Empirical P(V < 4): {prob_v_lt_4_empirical:.4f}")
print(f"Theoretical P(V < 4) (Chi2 df=1): {prob_v_lt_4_theoretical:.4f}")
