import numpy as np
from vispy_widget import QtVispyWidget
from glue.qt import get_qapp

# Make sure QApplication is started
get_qapp()

# Create fake data
data = np.arange(1000).reshape((10,10,10))

# Set up widget
w = QtVispyWidget()
w.set_data(data)
w.set_canvas()
w.canvas.render()
