from scipy.stats import f

# 자유도
d1, d2 = 9, 9

# 누적분포함수 값
cdf_val = f.cdf(2, d1, d2)
prob = 1 - cdf_val

print(f"P(F > 2) = {prob:.4f}")
