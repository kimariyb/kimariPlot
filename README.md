<h1 align="center">
    <img src="figure/logo.png" width="200">
</h1><br>

KimariPlot 是一个开源的 Python 绘图脚本，用来绘制科研中的 Free Energy Profile。KimariPlot 使用简单，可以直接从命令行读取 Toml 文件绘制 Free Energy Profile，可以不需要用鼠标一直拖来拖去，是懒人绘制 Free Energy Profile 的极佳选择。

## 安装

KimariPlot 可以使用 pip 工具直接安装。

```shell
pip install kimariplot
```

与此同时还需要安装 matplotlib 以及 toml 库（暂时不需要安装 numpy 和 pandas 库，以后可能需要）。

```shell
pip install matplotlib, toml
```

## 使用

安装完 KimariPlot 之后，可以直接通过如下命令在命令行中运行。

```shell
kimariplot profile.toml
```

其中，`profile.toml` 是一个记录了颜色、曲线格式以及绘制所需要的数据的 Toml 文件。以下是 `kimariplot/example/profile1.toml` 和 `kimariplot/example/profile2.toml` 的内容，以及生成的 Free Energy Profile 图像。

```toml
[path.1]
color = "black"
style = "-"
data = [
    ["7", "1", "-0.7"],
    ["TS1", "2", "22.4"],
    ["8", "3", "10.9"],
    ["TS2", "4", "18.0"],
    ["9", "5", "-8.7"],
    ["10", "6", "-10.0"]
]

[path.2]
color = "red"
style = "--"
data = [
    ["7", "1", "-0.7"],
    ["TS3", "2", "34.9"],
    ["11", "3", "17.2"],
    ["TS4", "4", "23.8"],
    ["10", "6", "-10.0"]
]
```

<img src="figure/1.png">

```toml
[path.1]
color = "black"
style = "-"
data = [
    ["R", "1", "0.0"],
    ["", "2", "-2.9"],
    ["", "3", "16.6"],
    ["CP2", "4", "-3.6"],
    ["P", "5", "-2.1"]
]

[path.2]
color = "red"
style = "--"
data = [
    ["R", "1", "0.0"],
    ["CP1", "2", "-4.4"],
    ["TS1", "3", "13.5"],
    ["", "4", "-1.5"],
    ["P", "5", "-2.1"]
]

[path.3]
color = "blue"
style = "--"
data = [
    ["", "1", "0.0"],
    ["", "2", "1.2"],
    ["", "3", "18.1"],
    ["", "4", "1.3"],
    ["", "5", "-2.1"]
]

[path.4]
color = "green"
style = "--"
data = [
    ["", "1", "0.0"],
    ["", "2", "2.3"],
    ["", "3", "19.8"],
    ["", "4", "2.5"],
    ["", "5", "-2.1"]
]
```

<img src="figure/2.png">

## 鸣谢

KimariPlot 的开发离不开以下开源项目：

- **NumPy**
- **Matplotlib**
- **SciPy**
- **Toml**

还要感谢所有为 KimariPlot 做出贡献的开发者 Kimariyb 和用户。

## 许可证

KimariPlot 基于 **MIT** 许可证开源。这意味着您可以自由地使用、修改和分发代码。有关更多信息，请参见 LICENSE 文件。