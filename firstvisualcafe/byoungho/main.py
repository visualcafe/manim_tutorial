from manim import *
import numpy as np
import sys

sys.path.append('../')

class DrawMultiparaSurface(ThreeDScene):
    def func(self, u, v):
        return np.array([u, v, u**2 + v**2])
    
    def construct(self):
        axes = ThreeDAxes(x_range=[-4,4], x_length=8)
        surface = Surface(
            lambda u, v: axes.c2p(*self.func(u, v)),
            u_range=[-PI, PI],
            v_range=[-PI, PI]
        )
        self.set_camera_orientation(theta=50 * DEGREES, phi=75 * DEGREES)
        self.add(axes, surface)
        

if __name__ == '__main__':

    scene = DrawMultiparaSurface()
    scene.render()