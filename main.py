from Entity.plot_data import PlotData
from Service.plotter import KpiPlotter
from Utility.art import art_text
from Utility.parser import KpiParser


def main():
    # 设置欢迎界面
    art_text()
    # 输入 kpi 文件路径
    print("请输入 KimariPlot input 文件：")
    url = input()
    # 创建 Parser 解析 kpi 文件
    kpi_result = KpiParser(url).parse()
    # 得到 kpi 文件中的所有数据
    plot_data = PlotData(kpi_result['header'], kpi_result['data'])
    # 绘制曲线
    fig, ax = KpiPlotter(plot_data).draw_plot()
    # 展示曲线
    fig.show()
    # 询问保存文件的格式
    print("请输入需要保存的文件名（默认为 figure.png）：")
    filename = input().strip()
    # 设置默认为 figure.png
    if not filename:
        fig.savefig("figure.png", dpi=700, bbox_inches='tight')
    else:
        fig.savefig(filename, dpi=None, bbox_inches='tight')


if __name__ == "__main__":
    main()
