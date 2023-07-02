import numpy as np
from matplotlib import pyplot as plt
from scipy.interpolate import interp1d
from Utility.math_function import find_extremas, find_suitable_y
from Entity.data import PlotData


class KpiPlotter:
    def __init__(self, data: PlotData):
        self.data = data

    def draw_plot_line(self):
        """
        Draws a line plot of the data.
        """
        # 设置全局字体、字重和轴线宽度
        plt.rcParams.update({
            'font.family': self.data.font,
            'font.weight': 'bold',
            'axes.linewidth': 1.5
        })

        # 创建画布和子图对象
        fig, ax = plt.subplots(figsize=self.data.size)

        num_x = self.data.get_num_x()
        num_y = self.data.get_num_y()

        # 设置 x 轴和 y 轴的范围
        ax.set_xlim(0, num_x.max() + 1)
        # 寻找最适合的 y 坐标
        suitable_y_min, suitable_y_max = find_suitable_y(num_y)
        ax.set_ylim(suitable_y_min, suitable_y_max)

        # 设置 y 轴刻度均匀分布
        yticks = np.linspace(suitable_y_min, suitable_y_max, 8)
        ax.yaxis.set_ticks(yticks)

        # 绘制平台
        # 在每个数据点上绘制长度为 0.4 的水平线，并在水平线上显示数字
        for i, (x, y) in enumerate(zip(num_x, num_y)):
            ax.plot([x - 0.2, x + 0.2], [y, y], color=self.data.color[0], linewidth=3)
            if abs(y) > 100:
                ax.text(x, y + 2, f"{y:.1f}", ha='center', va='bottom', fontsize=11.5, color=self.data.color[2])
            else:
                ax.text(x, y + 0.5, f"{y:.1f}", ha='center', va='bottom', fontsize=11.5, color=self.data.color[2])
        # 以折线连接平台
        for i in range(len(num_x) - 1):
            ax.plot([num_x[i] + 0.2, num_x[i + 1] - 0.2], [num_y[i], num_y[i + 1]], color=self.data.color[1], linewidth=1,
                    linestyle='--')

        # 设置标题、x轴、y轴标签
        ax.set_title(self.data.title, fontweight='bold', fontsize=18)
        ax.set_xlabel(self.data.x_label, fontweight='bold', fontsize=14)
        y_label = f"{self.data.y_label} in ({self.data.unit})"
        ax.set_ylabel(y_label, fontweight='bold', fontsize=14)

        # 将 x 轴的刻度线和标签设置为空
        ax.tick_params(axis='x', which='both', length=0, labelsize=0)
        # 调整标题的垂直位置
        ax.title.set_y(0.8)

        return fig, ax

    def draw_plot_curve(self):
        """
        Draws a curve plot of the data.
        """
        # 设置全局字体、字重和轴线宽度
        plt.rcParams.update({
            'font.family': self.data.font,
            'font.weight': 'bold',
            'axes.linewidth': 1.5
        })
        # 创建画布和子图对象
        fig, ax = plt.subplots(figsize=self.data.size)

        # 设置 x 轴和 y 轴的范围
        num_x = self.data.get_num_x()
        num_y = self.data.get_num_y()
        # 分别得到 x 和 y 的最大、最小值
        x_max = self.data.get_x_max()
        x_min = self.data.get_x_min()
        y_max = self.data.get_y_max()
        y_min = self.data.get_y_min()
        # 处理最小值为 0 时，不扩展 y 轴范围的情况
        if y_min == 0:
            y_max *= 1.05 if y_max > 0 else 0.95
            y_min = -15
        else:
            y_min *= 1.05 if y_min < 0 else 0.95
            y_max *= 1.05 if y_max > 0 else 0.95
        ax.set_xlim(num_x.min(), num_x.max())
        ax.set_ylim(y_min, y_max)

        # 设置 x 轴刻度均匀分布
        xticks = np.linspace(num_x.min(), num_x.max(), 13)
        ax.xaxis.set_ticks(xticks)

        # 创建插值函数
        f = interp1d(num_x, num_y, kind='cubic')

        # 生成平滑的数据
        x_smooth = np.linspace(x_max, x_min, 1000)
        y_smooth = f(x_smooth)

        # 绘制图形
        ax.plot(x_smooth, y_smooth, color=self.data.color[1], linewidth=2, linestyle="-")
        # 寻找并绘制极值
        extremas = find_extremas(x_smooth, y_smooth)
        plt.plot(*zip(*extremas["maxima"]), linestyle='None', marker='o', color=self.data.color[0])
        plt.plot(*zip(*extremas["minima"]), linestyle='None', marker='o', color=self.data.color[0])

        # 设置标题、x轴、y轴标签
        ax.set_title(self.data.title, fontweight='bold', fontsize=18)
        ax.set_xlabel(self.data.x_label, fontweight='bold', fontsize=14)
        y_label = f"{self.data.y_label} in ({self.data.unit})"
        ax.set_ylabel(y_label, fontweight='bold', fontsize=14)

        # 调整标题的垂直位置
        ax.title.set_y(0.8)

        return fig, ax

    def draw_plot(self):
        """
         根据绘图类型绘制图像
         """
        if self.data.style == 'line':
            return self.draw_plot_line()
        elif self.data.style == 'curve':
            return self.draw_plot_curve()

