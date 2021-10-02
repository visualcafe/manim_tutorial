from manim import *
import numpy as np
from VisualCafe.QuadricSurfaces import *

class Draw(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        surface = Surface(
            lambda u, v: axes.c2p(*Ellipsoid(u, v)),
            u_range=[0, 2*PI],
            v_range=[0, PI]
            )
        self.set_camera_orientation(theta=50 * DEGREES, phi=75 * DEGREES)
        self.add(axes)
        self.play(Create(surface))
        

if __name__ == '__main__':

    scene = Draw()
    scene.render()