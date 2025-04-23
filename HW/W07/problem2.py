import math

# sample data
data = [180, 230, 220, 270, 200]
n = len(data)
mean = sum(data) / n

# sample standard deviation
squared_diffs = [(x - mean) ** 2 for x in data]
s2 = sum(squared_diffs) / (n - 1)
s = math.sqrt(s2)

# standard error
se = s / math.sqrt(n)

# z or t statistic for cutoff 230
cutoff = 230
t_stat = (cutoff - mean) / se

# helper: one‑sided upper tail of standard normal
def norm_sf(z):
    """Survival function (1-CDF) for standard normal using error function."""
    return 0.5 * math.erfc(z / math.sqrt(2))

# try to use Student‑t survival if scipy available
try:
    from scipy.stats import t
    p_t = t.sf(t_stat, df=n - 1)  # survival (upper‑tail) probability
except Exception:
    p_t = None

p_norm = norm_sf(t_stat)

print(f"Sample mean  = {mean:.4f}")
print(f"Sample std   = {s:.4f}")
print(f"Standard err = {se:.4f}")
print(f"t (or z)     = {t_stat:.4f}")
print()
print("Upper‑tail probability P(X̄ > 230)")
print("------------------------------------")
print(f"Using normal approx.: {p_norm:.4f}")
if p_t is not None:
    print(f"Using t(df={n-1})      : {p_t:.4f}")
else:
    print("scipy not available → t‑tail not computed")

