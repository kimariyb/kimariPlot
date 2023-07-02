import math


def find_extremas(x, y):
    """
    寻找曲线的极值点

    参数：
    x: 一个包含曲线 x 坐标的列表或数组
    y: 一个包含曲线 y 坐标的列表或数组

    返回值：
    一个字典，包含两个键，分别为 "maxima" 和 "minima"，对应曲线的极大值点和极小值点。每个键的值是一个列表，包含极值点的坐标（x 坐标和 y 坐标）。
    """

    maxima = []
    minima = []

    # 寻找极大值点
    for i in range(1, len(y) - 1):
        if y[i] > y[i - 1] and y[i] > y[i + 1]:
            maxima.append((x[i], y[i]))

    # 寻找极小值点
    for i in range(1, len(y) - 1):
        if y[i] < y[i - 1] and y[i] < y[i + 1]:
            minima.append((x[i], y[i]))

    return {"maxima": maxima, "minima": minima}


def find_suitable_y(y_points):
    """
    寻找合适的 y 值
    """
    # 设置两个变量，记录返回值
    y_max = None
    y_min = None
    # 判断数据是否符合规则
    if y_points.min() == 0:
        y_min = y_points.max() * 0.4
        y_max = y_points.max() * 1.4
    elif abs(y_points.min()) >= abs(y_points.max()):
        y_min = y_points.min() * 1.4
        y_max = y_points.max() * 1.4
    elif abs(y_points.min()) < abs(y_points.max()):
        y_min = y_points.min() * 1.4
        y_max = y_points.max() * 1.4

    y_max = math.ceil(y_max / 10) * 10
    y_min = math.floor(y_min / 10) * 10

    return y_min, y_max
