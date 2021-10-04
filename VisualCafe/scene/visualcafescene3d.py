from manim import *
from VisualCafe.VGroup.visualcafeintro import *
__all__ = ["VisualCafeScene3D"]

#랜더링 클래스
class VisualCafeScene3D(ThreeDScene):
    def setup(self):
        self.intro_object = VisualCafeIntro(Text("Visual Cafe"))

    def construct(self):
        self.set_animation_group()

    def set_animation_group(self):
        self.do_animation(1, self.intro_object)

    def do_animation(self, wait_second, *args):
        for arg in args:
            self.create_and_fadeout(arg, wait_second)

    def create_and_fadeout(self, object, wait_second):
        self.play(Create(object))
        self.play(FadeOut(object))
        self.wait(wait_second)

