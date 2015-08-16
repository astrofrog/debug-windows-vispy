from PyQt4 import QtGui
from vispy import scene

import numpy as np


class QtVispyWidget(QtGui.QWidget):

    def __init__(self, parent=None, data=None):

        super(QtVispyWidget, self).__init__(parent=parent)

        self.canvas = scene.SceneCanvas(show=True)
        view = self.canvas.central_widget.add_view()
        volume = scene.visuals.Volume(data, parent=view.scene)
        view.camera = scene.cameras.TurntableCamera(parent=view.scene)

# Start up Qt application
qapp = QtGui.QApplication([''])
qapp.setQuitOnLastWindowClosed(True)

# Create fake data
data = np.arange(1000).reshape((10, 10, 10))

# Set up widget
w = QtVispyWidget(data=data)
w.canvas.render()
