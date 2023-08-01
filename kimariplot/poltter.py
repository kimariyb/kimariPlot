import matplotlib.pyplot as plt


def get_suitable_x(plot_data_list):
    """
    returns a suitable x
    """
    mix_list = []
    for plot_data in plot_data_list:
        mix_list.append(plot_data.get_x())
    # 找到每个列表中的最大值，并将它们存储在一个列表中
    max_values = [max(lst) for lst in mix_list]
    # 找到列表中的最大值
    max_value = max(max_values)

    return max_value


def get_suitable_y(plot_data_list):
    """
    returns a suitable y
    """
    mix_list = []
    for plot_data in plot_data_list:
        mix_list.append(plot_data.get_y())
    # 找到每个列表中的最大值，并将它们存储在一个列表中
    max_values = [max(lst) for lst in mix_list]
    # 找到每个列表中的最小值，并将它们存储在一个列表中
    min_values = [min(lst) for lst in mix_list]
    # 找到列表中的最大值
    max_value = max(max_values)
    # 找到列表中的最小值
    min_value = min(min_values)

    return max_value, min_value


def plot_line_path(ax, x, y, labels, color, style, data_list):
    """
    用来绘制单个路径的 Energy Profile
    :param ax: Matplotlib axes object
    :param x: X position
    :param y: y position
    :param labels: List of labels
    :param color: Color of the data
    :param style: Style of the data
    :param data_list: list of the plot data
    """
    # 获取合适的 y 增量
    y_max, y_min = get_suitable_y(data_list)
    y_add_num = (y_max - y_min) * 0.008
    # 在每个数据点上绘制长度为 0.3 的水平线，并在水平线上显示数字，水平线下显示 label
    for i, (x_new, y_new) in enumerate(zip(x, y)):
        # 绘制水平线
        ax.plot([x_new - 0.15, x_new + 0.15], [y_new, y_new], color=color, linewidth=2.7)
        # 显示数字
        ax.text(x_new, y_new + y_add_num, f"{y_new:.1f}", ha='center', va='bottom', fontsize=8,
                fontweight='medium')
        # 绘制 label
        ax.text(x_new, y_new - y_add_num * 1.8, labels[i], ha='center', va='top', fontsize=8.5, fontweight='bold')

    # 以折线连接平台
    for i in range(len(x) - 1):
        ax.plot([x[i] + 0.15, x[i + 1] - 0.15], [y[i], y[i + 1]], linestyle=style, linewidth=1, color=color)


def plot_all_line_paths(data_list, dpi, size, font, output_type):
    """
    绘制所有的路径，顺序从最后一个绘制
    :param data_list: list of plot data
    :param dpi: dpi of the graph
    :param size: size of the graph
    :param font: font of the graph
    :param output_type: output type of graph
    """
    # 设置字体
    plt.rcParams['font.family'] = font

    # 创建画布
    fig, ax = plt.subplots(figsize=size, dpi=300)
    # 反转列表
    reversed_data_list = list(reversed(data_list))
    # 遍历路径列表，绘制每一条路径
    for plot_data in reversed_data_list:
        color = plot_data.color
        style = plot_data.style
        labels = plot_data.get_labels()
        x = plot_data.get_x()
        y = plot_data.get_y()
        plot_line_path(ax, x, y, labels, color, style, data_list)

    # 找到所有 x_list 中最大的一个值
    x_suitable = get_suitable_x(data_list)

    # 设置 x 轴坐标刻度
    ax.set_xlim(0.5, x_suitable + 0.5)
    # 设置 y 轴标题
    ax.set_ylabel("Gibbs Free Energy (kcal/mol)", fontsize=14, fontweight="bold")
    # 设置 0.5 留白
    ax.margins(0.5)

    # 将 x 轴和 y 轴的刻度线和标签设置为空
    ax.tick_params(axis='both', which='both', length=0, labelsize=0)

    # 显示图形
    fig.show()
    # 保存路径为当前文件夹下的 figure 文件
    save_name = "figure." + output_type
    # 保存
    fig.savefig(save_name, dpi=dpi)
