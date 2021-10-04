from manim import *
from VisualCafe.VGroup.visualcafeintro import *
from VisualCafe.scene.visualcafescene3d import *

#랜더링 클래스
class WheelParadox(VisualCafeScene3D):
    def set_animation_group(self):
        self.intro_object = VisualCafeIntro(Text("바퀴의 역설"))
        self.triangle = Triangle()
        self.circle = Circle(radius=2, color=BLUE_A)
        self.do_animation(1, self.intro_object, self.circle, self.triangle)

#실행부분
if __name__ == '__main__':

    scene = WheelParadox()
    scene.render()

