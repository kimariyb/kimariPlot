# -*- coding: utf-8 -*-
"""
plotter.py
Briefly describe the functionality and purpose of the file.

This is a Main function file!

This file is part of KimariPlot.
KimariPlot is a Python script that quickly creating energy profile.

@author:
Kimariyb (kimariyb@163.com)

@license:
Licensed under the MIT License.
For details, see the LICENSE file.

@Data:
2023-09-12
"""
import argparse
import os

from datetime import datetime
from pathlib import Path

import matplotlib.pyplot as plt
import toml

# 获取当前文件被修改的最后一次时间
time_last = os.path.getmtime(os.path.abspath(__file__))
# 全局的静态变量
__version__ = "v1.3.2"
__developer__ = "Kimariyb, Ryan Hsiun"
__address__ = "XiaMen University, School of Electronic Science and Engineering"
__website__ = "https://github.com/kimariyb/kimariPlot"
__release__ = str(datetime.fromtimestamp(time_last).strftime("%b-%d-%Y"))


class PlotData:
    """
    PlotData 对象，用来存储 toml 文件中的信息，并且用来绘制图片
    """

    def __init__(self, color, style, data):
        self.color = color
        self.style = style
        self.data = data

    def __str__(self):
        result = f"The data of plotting: \ncolor: {self.color}\nstyle: {self.style}\n"
        for i, item in enumerate(self.data):
            result += f"item {i + 1}: {item}\n"
        return result

    def get_labels(self):
        """
        get the first elements of data
        """
        return [sublist[0] for sublist in self.data]

    def get_x(self):
        """
        get the second elements of data
        """
        return [float(sublist[1]) for sublist in self.data]

    def get_y(self):
        """
        get the third elements of data
        """
        return [float(sublist[2]) for sublist in self.data]


def parse(file_path: str):
    """
    读取 toml 文件，并返回一个 PlotData 对象列表
    """
    try:
        # 使用 Path 对象表示文件路径
        file_path = Path(file_path)
        # 使用上下文管理器打开文件，读取 toml 文件，并赋值给一个 toml 对象
        with file_path.open('r', encoding='utf-8') as f:
            toml_data = toml.load(f)

        # 创建一个空的 PlotData 对象列表
        plot_data_list = []

        # 遍历 toml 对象中的所有的 path 段落
        for path_data in toml_data['path']:
            plot_data = PlotData(path_data['color'], path_data['style'], path_data['data'])
            plot_data_list.append(plot_data)

        # 返回 PlotData 对象列表
        return plot_data_list
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{file_path}' not found.")
    except (toml.TomlDecodeError, KeyError) as e:
        raise ValueError(f"Error parsing TOML file: {e}")
    except Exception as e:
        raise Exception(f"An error occurred while parsing the file: {e}")


def get_suitable_x(plot_data_list):
    """
    returns a suitable x
    """
    x_lists = [plot_data.get_x() for plot_data in plot_data_list]
    # 找到每个列表中的最大值，并将它们存储在一个列表中
    max_values = [max(lst) for lst in x_lists]
    # 找到列表中的最大值
    max_value = max(max_values)

    return max_value


def get_suitable_y(plot_data_list):
    """
    returns a suitable y
    """
    y_lists = [plot_data.get_y() for plot_data in plot_data_list]
    # 找到每个列表中的最大值，并将它们存储在一个列表中
    max_values = [max(lst) for lst in y_lists]
    # 找到每个列表中的最小值，并将它们存储在一个列表中
    min_values = [min(lst) for lst in y_lists]
    # 找到列表中的最大值
    max_value = max(max_values)
    # 找到列表中的最小值
    min_value = min(min_values)

    return max_value, min_value


def plot_line(ax, x, y, labels, color, style, data_list):
    """
    Plots a line graph of the energy profile for a single path.

    Args:
        ax (matplotlib.axes.Axes): Matplotlib axes object.
        x (list): X positions.
        y (list): Y positions.
        labels (list): List of labels.
        color (str): Color of the data.
        style (str): Style of the data.
        data_list (list): List of the plot data.
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
                fontweight='medium', color=color)
        # 绘制 label
        ax.text(x_new, y_new - y_add_num * 1.8, labels[i], ha='center', va='top', fontsize=8.5, fontweight='bold',
                color=color)

    # 以折线连接平台
    for i in range(len(x) - 1):
        ax.plot([x[i] + 0.15, x[i + 1] - 0.15], [y[i], y[i + 1]], linestyle=style, linewidth=1, color=color)


def plot_all_lines(data_list, dpi, size, font, output_type):
    """
    Draws all the paths in reverse order.

    Args:
        data_list (list): List of plot data.
        dpi (int): DPI of the graph.
        size (tuple[float]): Size of the graph.
        font (str): Font of the graph.
        output_type (str): Output type of the graph.
    """
    try:
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
            plot_line(ax, x, y, labels, color, style, data_list)

        # 找到所有 x_list 中最大的一个值
        x_suitable = get_suitable_x(data_list)

        # 设置 x 轴坐标刻度
        ax.set_xlim(0.5, x_suitable + 0.5)
        # 设置 y 轴标题
        ax.set_ylabel("Gibbs Free Energy (kcal/mol)", fontsize=16, fontweight="bold")
        # 设置 0.5 留白
        ax.margins(0.5)

        # 将 x 轴和 y 轴的刻度线和标签设置为空
        ax.tick_params(axis='both', which='both', length=0, labelsize=0)

        # 显示图形
        fig.show()
        # 保存路径为当前文件夹下的 figure 文件
        save_name = "figure." + output_type
        # 保存
        fig.savefig(save_name, dpi=dpi, bbox_inches='tight')
        # 保存成功后提示成功信息
        print("============================================================================")
        print("The graph has been successfully saved! The new graph is named figure!\n")

    except Exception as e:
        raise Exception(f"An error occurred while plotting the graph: {e}")


def main():
    # 创建 ArgumentParser 对象
    parser = argparse.ArgumentParser(prog='KimariPlot', add_help=False,
                                     description='KimariPlot -- '
                                                 'A plotting software used for quickly creating energy profile.')
    # 添加 -h 参数
    parser.add_argument('--help', '-h', action='help', help='Show this help message and exit')
    # 添加输入文件参数
    parser.add_argument('input_file', type=str, help='Please input a Toml file')
    # 添加输出文件格式参数
    parser.add_argument('--output_type', '-o', dest='output', type=str, help='The output type of the graph',
                        default='png')
    # 添加输出文件 dpi 参数
    parser.add_argument('--dpi', '-d', dest='dpi', type=int, help='The dpi of the output graph', default=500)
    # 添加全局字体参数
    parser.add_argument('--font', '-f', dest='font', type=str, help='The font family of the graph', default='Arial')
    # 添加图像大小参数
    parser.add_argument('--size', '-s', dest='size', type=str, help='The size of the graph', default='10,7.5')
    # 添加版权信息和参数
    parser.add_argument('--version', '-v', action='version', help='Show the version information',
                        version=__version__)
    # 解析命令行参数
    args = parser.parse_args()

    # 得到 Toml 文件中的数据列表
    plot_data_list = parse(args.input_file)
    # 将 size 参数转换为元组类型
    size = tuple(map(float, args.size.split(',')))
    # 绘制所有路径
    plot_all_lines(plot_data_list, args.dpi, size, args.font, args.output)
    # 程序最后输出版本和基础信息
    print(f"KimariPlot -- A plotting software used for quickly creating energy profile.")
    print(f"Version: {__version__}, release date: {__release__}")
    print(f"Developer: {__developer__}")
    print(f"Address: {__address__}")
    print(f"KimariPlot home website: {__website__}\n")
    # 获取当前日期和时间
    now = datetime.now().strftime("%b-%d-%Y, %H:%M:%S")
    # 程序结束后提示版权信息和问候语
    print(f"Thank you for using our plotting tool! Have a great day!")
    print("Copyright (C) 2023 Kimariyb. All rights reserved.")
    print(f"Currently timeline: {now}")
    print("============================================================================")
