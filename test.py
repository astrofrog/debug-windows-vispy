from __future__ import absolute_import, division, print_function

from PyQt4 import QtGui
from vispy import scene

import numpy as np


class QtVispyWidget(QtGui.QWidget):

    def __init__(self, parent=None, data=None):

        super(QtVispyWidget, self).__init__(parent=parent)

        self.canvas = scene.SceneCanvas(keys='interactive', size=(800, 600), show=True)
        self.canvas.measure_fps()

        view = self.canvas.central_widget.add_view()

        volume = scene.visuals.Volume(data, parent=view.scene,
                                      threshold=0.1,
                                      emulate_texture=False)

        view.camera = scene.cameras.TurntableCamera(parent=view.scene,
                                                    fov=60.,
                                                    name='Turntable')

# Start up Qt application
qapp = QtGui.QApplication([''])
qapp.setQuitOnLastWindowClosed(True)

# Create fake data
data = np.arange(1000).reshape((10, 10, 10))

# Set up widget
w = QtVispyWidget(data=data)
w.canvas.render()
