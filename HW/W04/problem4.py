import math
import matplotlib.pyplot as plt

def poisson_pmf(k, lam):
    return (lam**k) * math.exp(-lam) / math.factorial(k)

def expected_min(Q, lam=17, max_k=60):
    # E[min(X, Q)] = Σ min(k, Q) * P(X=k), k=0..∞ (실제로는 0..max_k까지만)
    val = 0.0
    for k in range(max_k+1):
        val += min(k, Q) * poisson_pmf(k, lam)
    return val

def expected_profit(Q, lam=17):
    # 기대이윤 = 25,000 * E[min(X, Q)] - 5,000 * Q
    em = expected_min(Q, lam)
    revenue = 25000 * em
    cost = 5000 * Q
    return revenue - cost

# 주요 변수
lam = 17

# Q 후보를 0부터 50까지 순회하여 기대이윤을 계산
Q_candidates = range(0, 51)
profit_list = []
max_profit = -1e9
best_Q = None

for q in Q_candidates:
    ep = expected_profit(q, lam)
    profit_list.append(ep)
    if ep > max_profit:
        max_profit = ep
        best_Q = q

# 결과 출력
print("최적 Q =", best_Q)
print("최대 기대이윤 =", max_profit)

# 그래프 시각화
plt.plot(Q_candidates, profit_list, label="Expected Profit")
plt.scatter(best_Q, max_profit, s=50)  # 최적 Q 지점 표시
plt.text(best_Q, max_profit, f"  Best Q={best_Q}", fontsize=9)  # 간단한 주석

plt.title("Expected Profit by Number of Cakes (Q)")
plt.xlabel("Number of Cakes (Q)")
plt.ylabel("Expected Profit (Won)")
plt.legend()
plt.show()
