from __future__ import absolute_import, division, print_function
import numpy as np
from itertools import cycle

from PyQt4 import QtGui, QtCore
from vispy import scene
from vispy.color import get_colormaps

__all__ = ['QtVispyWidget']


class QtVispyWidget(QtGui.QWidget):

    # Setup colormap iterators
    opaque_cmaps = cycle(get_colormaps())
    opaque_cmap = next(opaque_cmaps)
    result = 1

    def __init__(self, parent=None):
        super(QtVispyWidget, self).__init__(parent=parent)

        self.canvas = scene.SceneCanvas(keys='interactive', size=(800, 600), show=True)
        self.canvas.measure_fps()

        self.data = None
        self.volume1 = self.view = None
        self.cam1 = self.cam2 = self.cam3 = None
        # self.cmap = None

    def set_data(self, data):
        self.data = data

    def set_canvas(self):
        if self.data is None:
            return
        vol1 = np.nan_to_num(np.array(self.data))

        # Prepare canvas
        # Set up a viewbox to display the image with interactive pan/zoom
        self.view = self.canvas.central_widget.add_view()

        # Set whether we are emulating a 3D texture
        emulate_texture = False

        # Create the volume visuals, only one is visible
        self.volume1 = scene.visuals.Volume(vol1, parent=self.view.scene, threshold=0.1,
                                       emulate_texture=emulate_texture)
        # volume1.transform = scene.STTransform(translate=(64, 64, 0))

        # Create two cameras (1 for firstperson, 3 for 3d person)
        fov = 60.
        self.cam1 = scene.cameras.FlyCamera(parent=self.view.scene, fov=fov, name='Fly')
        self.cam2 = scene.cameras.TurntableCamera(parent=self.view.scene, fov=fov,
                                             name='Turntable')
        self.cam3 = scene.cameras.ArcballCamera(parent=self.view.scene, fov=fov, name='Arcball')
        self.view.camera = self.cam2  # Select turntable at firstate_texture=emulate_texture)
