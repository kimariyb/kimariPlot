import argparse

from parser import parse
from poltter import plot_all_line_paths


# 定义自定义类型
def tuple_type(s):
    try:
        x, y = map(int, s.split(','))
        return x, y
    except:
        raise argparse.ArgumentTypeError("Invalid tuple format. Please use the format 'x,y'.")


def main():
    # 创建 ArgumentParser 对象
    parser = argparse.ArgumentParser(description='Generate a energy profile using kimariplot', add_help=False)
    # 添加 -h 参数
    parser.add_argument('--help', '-h', action='help', help='Show this help message and exit')
    # 添加输入文件参数
    parser.add_argument('input_file', type=str, help='Please input a Toml file')
    # 添加输出文件格式参数
    parser.add_argument('--output_type', '-o', dest='output', type=str, help='The output type of the graph', default='png')
    # 添加输出文件 dpi 参数
    parser.add_argument('--dpi', '-d', dest='dpi', type=int, help='The dpi of the output graph', default=500)
    # 添加全局字体参数
    parser.add_argument('--font', '-f', dest='font', type=str, help='The font family of the graph', default='Arial')
    # 添加图像大小参数
    parser.add_argument('--size', '-s', dest='size', type=tuple_type, help='The size of the graph', default=(10, 7.5))
    # 解析命令行参数
    args = parser.parse_args()
    # 得到 Toml 文件中的数据列表
    plot_data_list = parse(args.input_file)
    # 绘制所有路径
    plot_all_line_paths(plot_data_list, args.dpi, args.size, args.font, args.output)

if __name__ == '__main__':
    main()