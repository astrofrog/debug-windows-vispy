import numpy as np
from vispy_widget import QtVispyWidget
from PyQt4 import QtGui

# Start up Qt application
qapp = QtGui.QApplication([''])
qapp.setQuitOnLastWindowClosed(True)

# Create fake data
data = np.arange(1000).reshape((10,10,10))

# Set up widget
w = QtVispyWidget()
w.set_data(data)
w.set_canvas()
w.canvas.render()


