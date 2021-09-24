from manim import *
from firstvisualcafe.VisualCafe.visualcafeintro import *
ManimBanner
#랜더링 클래스
class RenderProject(ThreeDScene):
    def construct(self):
        intro_object = VisualCafeIntro(Text("Visual Cafe"))
        # self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        self.play(Create(intro_object))
        self.play(intro_object.animate.scale(1.5))
        self.play(intro_object.animate.clear_content())

        self.wait()

#실행부분
if __name__ == '__main__':

    scene = RenderProject()
    scene.render()
