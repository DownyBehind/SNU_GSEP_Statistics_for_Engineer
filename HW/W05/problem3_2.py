# 재실행: 필요한 패키지 재임포트 및 데이터 재정의
import numpy as np
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['font.family'] = 'AppleGothic'  
plt.rcParams['axes.unicode_minus'] = False


# 기존 50일 생산량 데이터
old_data = [87, 106, 87, 127, 95, 114, 109, 94, 111, 110,
            95, 87, 77, 91, 119, 102, 86, 110, 110, 94,
            140, 92, 107, 101, 103, 104, 111, 94, 93, 94,
            109, 98, 102, 120, 108, 93, 102, 93, 77, 97,
            101, 82, 98, 101, 98, 90, 101, 88, 81, 114]

# 신기술 적용 20일 생산량 데이터
new_data = [116, 122, 131, 135, 139, 126, 109, 113, 132, 144,
            103, 121, 128, 128, 101, 121, 122, 118, 112, 117]

# 평균 계산
old_mean = np.mean(old_data)
new_mean = np.mean(new_data)


# 결과 출력
print("📊 이전 평균 (Old Mean):", round(old_mean, 2))
print("🆕 신기술 평균 (New Mean):", round(new_mean, 2))

# 시각화: 두 그룹 평균 비교
plt.figure(figsize=(8, 5))
sns.boxplot(data=[old_data, new_data], palette="Set2")
plt.xticks([0, 1], ['기존 공정', '신기술 공정'])
plt.title("📦 생산량 비교 (기존 vs 신기술)")
plt.ylabel("일별 생산량")
plt.grid(True)
plt.show()
