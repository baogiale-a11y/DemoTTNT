#thuật Toán CCPC
from scipy.optimize import linear_sum_assignment
import numpy as np

# Bước 1: Nhập ma trận chi phí
cost_matrix = np.array([
    [6, 4, 7],
    [5, 3, 2],
    [8, 5, 3],
    [9, 2, 6]
])

# Bước 2: Áp dụng Hungarian Algorithm
row_indices, col_indices = linear_sum_assignment(cost_matrix)

# Bước 3: In kết quả
print("Phân công tối ưu:")
total_cost = 0
for i, j in zip(row_indices, col_indices):
    print(f"Nhân viên {i + 1} làm công việc {j + 1} với chi phí {cost_matrix[i, j]}")
    total_cost += cost_matrix[i, j]

print(f"Tổng chi phí tối thiểu: {total_cost}")