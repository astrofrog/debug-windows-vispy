from vispy import scene

import numpy as np

data = np.arange(1000).reshape((10, 10, 10))

canvas = scene.SceneCanvas(show=True)
view = canvas.central_widget.add_view()
axis = scene.visuals.XYZAxis(parent=view.scene)
view.camera = scene.cameras.TurntableCamera(parent=view.scene)

with canvas:
    canvas.render()
