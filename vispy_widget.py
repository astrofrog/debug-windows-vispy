from __future__ import absolute_import, division, print_function

from PyQt4 import QtGui
from vispy import scene

__all__ = ['QtVispyWidget']


class QtVispyWidget(QtGui.QWidget):

    def __init__(self, parent=None, data=None):

        super(QtVispyWidget, self).__init__(parent=parent)

        self.canvas = scene.SceneCanvas(keys='interactive', size=(800, 600), show=True)
        self.canvas.measure_fps()

        self.view = self.canvas.central_widget.add_view()

        self.volume = scene.visuals.Volume(data, parent=self.view.scene,
                                           threshold=0.1,
                                           emulate_texture=False)

        self.view.camera = scene.cameras.TurntableCamera(parent=self.view.scene,
                                                         fov=60.,
                                                         name='Turntable')
