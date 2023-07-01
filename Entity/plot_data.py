import numpy as np


class PlotData:

    def __init__(self, plot_header: dict, plot_data: list):
        self.title = plot_header['title']
        self.x_label = plot_header['x_label']
        self.y_label = plot_header['y_label']
        self.unit = plot_header['unit']
        self.size = plot_header['size']
        self.color = plot_header['color']
        self.font = plot_header['font']
        self.style = plot_header['style']
        self.data = plot_data

    def __str__(self):
        return f'PlotData(title={self.title}, x_label={self.x_label}, y_label={self.y_label}, unit={self.unit}, size={self.size}, color={self.color}, font={self.font}, style={self.style}, data={self.data})'

    def get_num_data(self):
        return np.array(self.data)

    def get_num_x(self):
        """
        Returns the number of x values in the data.
        """
        return self.get_num_data()[:, 0]

    def get_num_y(self):
        """
        Returns the number of y values in the data.
        """
        return self.get_num_data()[:, 1]

    def get_x_max(self):
        """
        Returns the maximum x value in the data.
        """
        return self.get_num_x().max()

    def get_x_min(self):
        """
        Returns the minimum x value in the data.
        """
        return self.get_num_x().min()

    def get_y_max(self):
        """
        Returns the maximum y value in the data.
        """
        return self.get_num_y().max()

    def get_y_min(self):
        """
        Returns the minimum y value in the data.
        """
        return self.get_num_y().min()
