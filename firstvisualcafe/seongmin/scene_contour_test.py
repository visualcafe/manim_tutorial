from manim import *
from VisualCafe.VGroup.visualcafeintro import *
from VisualCafe.scene.visualcafescene3d import *
from VisualCafe.scene.visualcafescene2d import *
import VisualCafe.scene.visualcafescene2d as vc2
import VisualCafe.QuadricSurfaces as vcq
import VisualCafe.visualcafesurfacewithcontour as vcs


class ContourTest(VisualCafeScene3D):
    def visualcafe_construct(self):
        resolution_fa = 42
        self.set_camera_orientation(phi=75 * DEGREES, theta=-120 * DEGREES)
        axes = ThreeDAxes(x_range=(0, 5, 1), y_range=(0, 5, 1), z_range=(-1, 1, 0.5))

        def param_surface(u, v):
            x = u
            y = v
            z = np.sin(x) * np.sin(y)
            return z

        def zero(u, v):
            return 0

        surface_plane = vcs.VisualCafeSurfaceContour(
            contour_func=lambda u, v: axes.c2p(u, v, zero(u, v)),
            func=lambda u, v: axes.c2p(u, v, param_surface(u, v)),
            resolution=(resolution_fa, resolution_fa),
            v_range=[0, 5],
            u_range=[0, 5])
        surface_plane.set_style(fill_opacity=1)
        surface_plane.set_fill_by_value(axes=axes, colors=[(RED, -0.4), (YELLOW, 0), (GREEN, 0.4)])
        surface_plane.set_contour_color(axes=axes, colors=[(RED, -0.4), (YELLOW, 0), (GREEN, 0.4)])
        self.add(axes, surface_plane)
        self.wait(3)


if __name__ == '__main__':
    scene = ContourTest()
    scene.render()