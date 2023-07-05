import os

from Parser.data import PlotData
from Plotter.plotter import KpiPlotter
from Parser.parser import KpiParser
from Utility.util import art_text


def main():
    # 设置欢迎界面
    art_text()
    # 输入 kpi 文件路径
    url = input("Please enter the KimariPlot input file (kpi file) path: ")
    # 创建 Parser 解析 kpi 文件
    kpi_result = KpiParser(url).parse()
    # 得到 kpi 文件中的所有数据
    plot_data = PlotData(kpi_result['header'], kpi_result['data'])
    # 绘制曲线
    fig, ax = KpiPlotter(plot_data).draw_plot()
    # 展示曲线
    fig.show()
    # 询问保存文件的格式
    filename = input("Please enter the filename to save (default is figure.png): ").strip()
    # 设置默认为 figure.png
    if not filename:
        fig.savefig("figure.png", dpi=700, bbox_inches='tight')
        print(f"Saved successfully. The image figure.png has been saved to {os.getcwd()}")
    else:
        fig.savefig(filename, dpi=700, bbox_inches='tight')
        print(f"Saved successfully. The image {filename} has been saved to {os.getcwd()}")


if __name__ == "__main__":
    main()
