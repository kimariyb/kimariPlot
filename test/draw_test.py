from Entity.data import PlotData
from Service.plotter import KpiPlotter
from Utility.parser import KpiParser


def test_line():
    url = "../example/line_test.kpi"
    result = KpiParser(url).parse()
    plot_data = PlotData(result["header"], result["data"])
    fig, ax = KpiPlotter(plot_data).draw_plot()
    fig.show()


def test_curve():
    url = "../example/curve_test.kpi"
    result = KpiParser(url).parse()
    plot_data = PlotData(result["header"], result["data"])
    fig, ax = KpiPlotter(plot_data).draw_plot()
    fig.show()


if __name__ == '__main__':
    test_line()
    # test_curve()
