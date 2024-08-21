import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu từ file CSV
df = pd.read_csv('female.csv')

# Đếm số lần xuất hiện của mỗi họ
ho_counts = df['Nguyện vọng'].value_counts()

# Vẽ biểu đồ cột ngang
ax = ho_counts.plot(kind='barh', color='blue')

# Thiết lập tiêu đề và nhãn
plt.title("Thí sinh nữ Hà Nội đỗ nguyện vọng mấy <(')?")
plt.xlabel("Số lần xuất hiện")
plt.ylabel("Nguyện Vọng")

# Thêm số lượng lên bên trái của mỗi cột
for p in ax.patches:
    ax.annotate(str(p.get_width()), (p.get_width(), p.get_y() + p.get_height() / 2.),
                ha='left', va='center', xytext=(5, 0), textcoords='offset points')

# Hiển thị biểu đồ
plt.show()
