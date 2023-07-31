import matplotlib.pyplot as plt
import numpy as np
from kimariplot.parser import parse

# 得到 Toml 文件中的数据列表
plot_data_list = parse("example/profile.toml")

# 绘制 path1
# 取出对象中的颜色
color1 = plot_data_list[0].color
# 取出对象中的 line style
style1 = plot_data_list[0].style
# 取出每一个标签列表
labels1 = plot_data_list[0].get_labels()
# 取出 x 轴和 y 轴坐标
x1 = plot_data_list[0].get_x()
y1 = plot_data_list[0].get_y()
# 创建画布
fig, ax = plt.subplots(figsize=(10, 7.5), dpi=300)
# 绘制 line_spilt
# 在每个数据点上绘制长度为 0.3 的水平线，并在水平线上显示数字，水平线下显示 label
for i, (x_new, y_new) in enumerate(zip(x1, y1)):
    ax.plot([x_new - 0.15, x_new + 0.15], [y_new, y_new], color=color1, linewidth=2.7)
    ax.text(x_new, y_new + 1, f"{y_new:.1f}", ha='center', va='bottom', fontsize=8, fontweight='medium')
    # 绘制 label
    ax.text(x_new, y_new - 1.25, labels1[i], ha='center', va='top', fontsize=8.5, fontweight='bold')

# 以折线连接平台
for i in range(len(x1) - 1):
    ax.plot([x1[i] + 0.15, x1[i + 1] - 0.15], [y1[i], y1[i + 1]], linestyle=style1, linewidth=1, color=color1)

# 绘制 path2
# 取出对象中的颜色
color2 = plot_data_list[1].color
# 取出对象中的 line style
style2 = plot_data_list[1].style
# 取出每一个标签列表
labels2 = plot_data_list[1].get_labels()
# 取出 x 轴和 y 轴坐标
x2 = plot_data_list[1].get_x()
y2 = plot_data_list[1].get_y()
# 绘制 line_spilt
# 在每个数据点上绘制长度为 0.3 的水平线，并在水平线上显示数字，水平线下显示 label
for i, (x_new, y_new) in enumerate(zip(x2, y2)):
    ax.plot([x_new - 0.15, x_new + 0.15], [y_new, y_new], color=color2, linewidth=2.7)
    ax.text(x_new, y_new + 1, f"{y_new:.1f}", ha='center', va='bottom', fontsize=8, fontweight='medium')
    # 绘制 label
    ax.text(x_new, y_new - 1.25, labels2[i], ha='center', va='top', fontsize=8.5, fontweight='bold')

# 以折线连接平台
for i in range(len(x2) - 1):
    ax.plot([x2[i] + 0.15, x2[i + 1] - 0.15], [y2[i], y2[i + 1]], linestyle=style2, linewidth=1, color=color2)

# 自动设置坐标轴大小
ax.autoscale()
# 设置 x 轴坐标刻度
ax.set_xlim(0.5, np.max(x1) + 0.5)
# 将 x 轴的刻度线和标签设置为空
ax.tick_params(axis='x', which='both', length=0, labelsize=0)
# 将 y 轴的刻度线和标签设置为空
ax.tick_params(axis='y', which='both', length=0, labelsize=0)
# 设置 y 轴标题
ax.set_ylabel("Gibbs Free Energy (kcal/mol)", fontsize=12, fontweight="bold")
# 设置 0.4 留白
ax.margins(0.4)
fig.show()
fig.savefig("figure.png", dpi=300)