from manim import *
from VisualCafe.VGroup.visualcafeintro import *
from VisualCafe.scene.visualcafescene3d import *
import VisualCafe.QuadricSurfaces as vcq

#랜더링 클래스
class WheelParadox(VisualCafeScene3D):
    def visualcafe_construct(self):
        #super.intro_object = VisualCafeIntro(Text("바퀴의 역설"))
        self.axes = ThreeDAxes(x_range=[-4, 4], x_length=8)
        self.surface = Surface(
            lambda u, v: self.axes.c2p(*vcq.Ellipsoid(u, v)),
            u_range=[-PI, PI],
            v_range=[0, TAU]
        )

        # self.set_to_default_angled_camera_orientation()
        self.set_camera_orientation(theta=70 * DEGREES, phi=75 * DEGREES)
        self.create_and_fadeout2(2, self.axes, self.surface)

#실행부분
if __name__ == '__main__':

    scene = WheelParadox()
    scene.render()

