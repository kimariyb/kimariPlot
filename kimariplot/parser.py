import toml


def parse(file_path: str):
    """
    读取 toml 文件，并返回一个 PlotData 对象列表
    """
    # 读取 toml 文件，并赋值给一个 toml 对象
    toml_data = toml.load(file_path)
    # 创建一个空的 PlotData 对象列表
    plot_data_list = []
    # 遍历 toml 对象中的所有的 profile 段落
    for name, profile_data in toml_data['profile'].items():
        # 创建一个 PlotData 对象，并添加到 plot_data_list 中
        plot_data = PlotData(profile_data['color'], profile_data['data'])
        plot_data_list.append(plot_data)
        print(plot_data)
    # 返回 PlotData 对象列表
    return plot_data_list


class PlotData:
    """
    PlotData 对象，用来存储 toml 文件中的信息，并且用来绘制图片
    """
    def __init__(self, color, data):
        self.color = color
        self.data = data

    def __str__(self):
        result = f"color: {self.color}\n"
        for i, item in enumerate(self.data):
            result += f"item {i+1}: {item}\n"
        return result


if __name__ == '__main__':
    parse("example/profile.toml")
