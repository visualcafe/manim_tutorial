from manim import *
from VisualCafe.VGroup.visualcafeintro import *
__all__ = ["VisualCafeScene2D"]

#Scene상속
class VisualCafeScene2D(Scene):

    # 기본적으로 모임 베너의 인스턴스를 가지고 있습니다.
    def setup(self):
        pass

    def construct(self):
        self.visualcafe_intro_animation()
        self.visualcafe_construct()

    def visualcafe_construct(self):
        pass

    # 디폴트 인트로 영상 플레이
    def visualcafe_intro_animation(self):
        self.intro_object = VisualCafeIntro(Text("Visual Cafe"))
        self.play(Create(self.intro_object))
        self.play(self.intro_object.animate.scale(1.5))
        # 아래는 컨텐트를 클리어하는 메서드입니다. 진짜로 지워지기 때문에 페이드아웃할 객체가 없어 일단 내버려둡니다.
        # self.play(self.intro_object.clear_content())
        self.play(FadeOut(self.intro_object))

    def create_and_fadeout(self, wait_second, *args):
        for arg in args:
            self.play(Create(arg))
            self.wait(wait_second)
            self.play(FadeOut(arg))
            self.wait(wait_second)

    def create_and_fadeout2(self, wait_second, *args):
        for arg in args:
            self.play(Create(arg))
            self.wait(wait_second)
        for arg in args:
            self.play(FadeOut(arg))
            self.wait(wait_second)
