import numpy as np
import matplotlib.pyplot as plt
import platform

# 폰트 설정 (Mac용)
if platform.system() == 'Darwin':
    plt.rcParams['font.family'] = 'AppleGothic'
else:
    plt.rcParams['font.family'] = 'Malgun Gothic'

plt.rcParams['axes.unicode_minus'] = False

# 시드 고정
np.random.seed(42)

# 파라미터 설정
mean = 100
std_dev = 10
days = 100
samples_per_day = 30
scale_exp = 100

# 문제 [1] - 하루 동안 30개 정규분포 샘플 평균
day1_lifespans = np.random.normal(loc=mean, scale=std_dev, size=samples_per_day)
day1_average = np.mean(day1_lifespans)

# 문제 [2] - 정규분포 기반 100일 평균
lifespan_100days = np.random.normal(loc=mean, scale=std_dev, size=(days, samples_per_day))
daily_means_normal = np.mean(lifespan_100days, axis=1)
outside_range_normal = np.sum((daily_means_normal < 97) | (daily_means_normal > 103))

# 문제 [3] - 지수분포 기반 100일 평균
lifespan_exp_100days = np.random.exponential(scale=scale_exp, size=(days, samples_per_day))
daily_means_exponential = np.mean(lifespan_exp_100days, axis=1)
outside_range_exp = np.sum((daily_means_exponential < 97) | (daily_means_exponential > 103))

# 문제 [3-1] - 하루 동안 30개 지수분포 샘플 평균
day1_lifespans_exp = np.random.exponential(scale=scale_exp, size=samples_per_day)
day1_average_exp = np.mean(day1_lifespans_exp)

# 결과 출력
print("[1] 하루 동안 생산된 30개 전구 평균 수명 (정규분포): {:.2f}분".format(day1_average))
print("[2] 정규분포 기반 100일 평균 중 97~103 범위 벗어난 날 수: {}일".format(outside_range_normal))
print("[3-1] 하루 동안 생산된 30개 전구 평균 수명 (지수분포): {:.2f}분".format(day1_average_exp))
print("[3-2] 지수분포 기반 100일 평균 중 97~103 범위 벗어난 날 수: {}일".format(outside_range_exp))


# 문제별 그래프 그리기
plt.figure(figsize=(15, 10))

# 문제 1: 하루 평균 수명 (정규분포)
plt.subplot(4, 1, 1)
plt.hist(day1_lifespans, bins=10, color='skyblue', edgecolor='black')
plt.axvline(day1_average, color='red', linestyle='--', label=f"평균: {day1_average:.2f}")
plt.title("[문제 1] 하루 동안 생산된 30개 전구의 수명 분포 (정규분포)")
plt.xlabel("전구 수명 (분)")
plt.ylabel("빈도수")
plt.legend()

# 문제 2: 정규분포 기반 100일 평균
plt.subplot(4, 1, 2)
plt.hist(daily_means_normal, bins=15, color='cornflowerblue', edgecolor='black')
plt.axvline(97, color='red', linestyle='--', label="하한선: 97분")
plt.axvline(103, color='red', linestyle='--', label="상한선: 103분")
plt.title("[문제 2] 정규분포 기반 100일 평균 수명 분포")
plt.xlabel("평균 수명 (분)")
plt.ylabel("빈도수")
plt.legend()

# 문제 3-1: 하루 평균 수명 (지수분포)
plt.subplot(4, 1, 3)
plt.hist(day1_lifespans_exp, bins=10, color='orange', edgecolor='black')
plt.axvline(day1_average_exp, color='red', linestyle='--', label=f"평균: {day1_average_exp:.2f}")
plt.title("[문제 3-1] 하루 동안 생산된 30개 전구의 수명 분포 (지수분포)")
plt.xlabel("전구 수명 (분)")
plt.ylabel("빈도수")
plt.legend()

# 문제 3-2: 지수분포 기반 100일 평균
plt.subplot(4, 1, 4)
plt.hist(daily_means_exponential, bins=15, color='salmon', edgecolor='black')
plt.axvline(97, color='red', linestyle='--', label="하한선: 97분")
plt.axvline(103, color='red', linestyle='--', label="상한선: 103분")
plt.title("[문제 3-2] 지수분포 기반 100일 평균 수명 분포")
plt.xlabel("평균 수명 (분)")
plt.ylabel("빈도수")
plt.legend()


plt.tight_layout()
plt.show()
