import math
import numpy as np

# ---------- 데이터 ----------
old = np.array([
    87,106,87,127,95,114,109,94,111,110,
    95,87,77,91,119,102,86,110,110,94,
    140,92,107,101,103,104,111,94,93,94,
    109,98,102,120,108,93,102,93,77,97,
    101,82,98,101,98,90,101,88,81,114
])

new = np.array([
    116,122,131,135,139,126,109,113,132,144,
    103,121,128,101,121,122,118,112,117
])  # 19개

# ---------- 헬퍼: 표준정규 상부꼬리 ----------
def std_normal_sf(z):
    """Z~N(0,1) 상부꼬리(SF) = 1-CDF"""
    return 0.5 * math.erfc(z / math.sqrt(2))

# ---------- 문제 3-1 ----------
n_old   = len(old)
mean_o  = old.mean()
s_old   = old.std(ddof=1)
se_old  = s_old / math.sqrt(n_old)

z31 = (105 - mean_o) / se_old      # mu0 - x̄
p31 = std_normal_sf(z31)

# ---------- 문제 3-2 & 3-3 ----------
n_new   = len(new)
mean_n  = new.mean()
s_new   = new.std(ddof=1)

diff    = mean_n - mean_o
se_diff = math.sqrt(s_old**2 / n_old + s_new**2 / n_new)

# 3-2: Δ > 0
z32 = (0 - diff) / se_diff
p32 = std_normal_sf(z32)

# 3-3: Δ > 20
z33 = (20 - diff) / se_diff
p33 = std_normal_sf(z33)

# ---------- 결과 출력 ----------
print("Problem 3-1  P(μ_old > 105)        ≈ {:.4f}".format(p31))
print("Problem 3-2  P(μ_new − μ_old > 0)  ≈ {:.4f}".format(p32))
print("Problem 3-3  P(μ_new − μ_old > 20) ≈ {:.4f}".format(p33))
