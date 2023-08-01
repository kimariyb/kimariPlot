import toml


def parse(file_path: str):
    """
    读取 toml 文件，并返回一个 PlotData 对象列表
    """
    # 读取 toml 文件，并赋值给一个 toml 对象
    # 使用上下文管理器打开文件
    with open(file_path, 'r', encoding='utf-8') as f:
        toml_data = toml.load(f)

    # 创建一个空的 PlotData 对象列表
    plot_data_list = []

    # 遍历 toml 对象中的所有的 profile 段落
    for name, profile_data in toml_data['path'].items():
        # 创建一个 PlotData 对象，并添加到 plot_data_list 中
        plot_data = PlotData(profile_data['color'], profile_data['style'], profile_data['data'])
        # 将读取到的 PlotData 对象放入集合中
        plot_data_list.append(plot_data)

    # 返回 PlotData 对象列表
    return plot_data_list


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


