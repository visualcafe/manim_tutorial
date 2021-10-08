from manim import *
from VisualCafe.VGroup.visualcafeintro import *
from VisualCafe.scene.visualcafescene3d import *
import VisualCafe.QuadricSurfaces as vcq

#랜더링 클래스
class WheelParadox(VisualCafeScene3D):
    def visualcafe_construct(self):
        self.circleBig = Circle()
        tracker = ValueTracker(3)

        self.circleBig = Circle(radius=3)
        self.add(self.circleBig)
        for i in range(3, 15):
            ss = RegularPolygon(17 - i, radius=3, fill_opacity=0, fill_color=RED)
            self.add(ss)
            self.wait(0.2)
            self.remove(ss)
        self.wait(2)
#실행부분
if __name__ == '__main__':

    scene = WheelParadox()
    scene.render()

