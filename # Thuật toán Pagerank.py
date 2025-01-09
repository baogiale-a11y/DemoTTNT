# Thuật toán Pagerank
import numpy as np 

def tinh_pagerank(links, he_so_giam_sat=0.85, so_lan_lap=100):
    so_trang = len(links)
    # Khởi tạo ma trận chuyển đổi
    ma_tran_chuyen_doi = np.zeros((so_trang, so_trang))
    pagerank = np.ones(so_trang) / so_trang  # Giá trị PageRank ban đầu (chia đều)
    # Xây dựng ma trận liên kết
    for i in range(so_trang):
        cac_trang_lien_ket = links[i]
        so_lien_ket = len(cac_trang_lien_ket)
        if so_lien_ket > 0:
            for j in cac_trang_lien_ket:
                ma_tran_chuyen_doi[j][i] = 1 / so_lien_ket  # Chia đều giá trị cho các liên kết

    # Tính toán PageRank qua các vòng lặp
    for _ in range(so_lan_lap):
        pagerank_moi = np.zeros(so_trang)

        for i in range(so_trang):
            for j in range(so_trang):
                pagerank_moi[i] += ma_tran_chuyen_doi[i][j] * pagerank[j]

            # Áp dụng hệ số giảm sát
            pagerank_moi[i] = (
                he_so_giam_sat * pagerank_moi[i]
                + (1 - he_so_giam_sat) / so_trang
            )
        pagerank = pagerank_moi  # Cập nhật giá trị PageRank
    return pagerank
# Ví dụ: Mạng liên kết đơn giản
# Danh sách các trang và các liên kết của chúng
links = [
    [],       # Trang 0 không liên kết đến trang nào
    [0],      # Trang 1 liên kết đến Trang 0
    [0, 1],   # Trang 2 liên kết đến Trang 0 và Trang 1
    [2]       # Trang 3 liên kết đến chính nó
]
# Tính toán PageRank
pagerank = tinh_pagerank(links)
# In kết quả
print("Giá trị PageRank của các trang:")
for i, pr in enumerate(pagerank):
    print(f"Trang {i}: {pr:.4f}")