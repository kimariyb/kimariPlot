import math
import os


class KpiParser:

    def __init__(self, filepath):
        """
        初始化方法，接收一个文件路径作为参数
        """
        self.filepath = filepath
        self._result = None

    def _validate(self, filetype):
        """
        验证文件是否存在，并检查文件类型是否符合要求
        :param filetype: 期望的文件类型
        :raises FileNotFoundError: 如果文件不存在
        :raises ValueError: 如果文件类型不符合要求
        """
        # 判断文件存在与否
        if not os.path.exists(self.filepath):
            raise FileNotFoundError(f"文件 '{self.filepath}' 不存在")

        # 获取文件的扩展名
        file_extension = os.path.splitext(self.filepath)[1]

        # 判断文件类型是否符合要求
        if file_extension != filetype:
            raise ValueError(f"文件类型 '{file_extension}' 不符合要求，期望的文件类型是 '{filetype}'")

    def _read_file(self):
        """
        读取文件内容并返回文件内容的列表
        """
        with open(self.filepath, 'r', encoding="utf-8") as f:
            lines = f.readlines()
        return lines

    def parse(self):
        """
        解析 kpi 文件，将解析结果存储在私有属性 _result 中
        :return: 将解析结果返回到一个字典中
        """
        if self._result:
            return self._result

        self._validate('.kpi')

        header = {
            'title': None,
            'x_label': None,
            'y_label': None,
            'unit': None,
            'size': None,
            'color': None,
            'font': None,
            'style': None
        }

        data = []

        # 打开文件
        lines = self._read_file()

        # 解析文件头
        for line in lines:
            line = line.strip()
            if line.startswith('%'):
                key, value = line[1:].split(' = ')
                if key == 'title':
                    header['title'] = value
                elif key == 'x':
                    header['x_label'] = value
                elif key == 'y':
                    header['y_label'] = value
                elif key == 'unit':
                    header['unit'] = value
                elif key == 'size':
                    width, height = map(int, value.split(','))
                    header['size'] = (width, height)
                elif key == 'color':
                    colors = value.split(', ')
                    header['color'] = colors
                elif key == 'font':
                    header['font'] = value
                elif key == 'style':
                    header['style'] = value
                else:
                    header[key.lower()] = value
            elif line == 'begin':
                break

        # 解析数据行
        for line in lines:
            line = line.strip()
            if line.startswith('%') or line == 'begin' or not line:
                continue
            elif line == 'end':
                break
            try:
                x, y = map(float, line.split(', '))
            except ValueError:
                raise ValueError(f'文件行 "{line}" 格式不正确')
            if not math.isfinite(x) or not math.isfinite(y):
                raise ValueError(f'文件行 "{line}" 包含非数值数据')
            data.append((x, y))

        # 将解析结果存储在字典中并返回
        self._result = {
            'header': header,
            'data': data
        }

        return self._result





