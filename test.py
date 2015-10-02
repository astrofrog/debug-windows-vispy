from vispy import scene

import numpy as np

data = np.arange(1000).reshape((10, 10, 10))

canvas = scene.SceneCanvas(show=True)
view = canvas.central_widget.add_view()
volume = scene.visuals.Volume(data, parent=view.scene, emulate_texture=True)
view.camera = scene.cameras.TurntableCamera(parent=view.scene)

canvas.render()
