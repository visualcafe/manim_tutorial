from manim import *
from VisualCafe.VGroup.visualcafeintro import *

#랜더링 클래스
class RenderProject(ThreeDScene):
    def setup(self):
        pass

    def construct(self):
        self.animation_group()


    def animation_group(self):
        self.intro_object = VisualCafeIntro(Text("Visual Cafe"))

        #연습
        self.axes = ThreeDAxes(x_range=[-4, 4], x_length=8)
        self.surface = Surface(
            lambda u, v: self.axes.c2p(*self.func(u, v)),
            u_range=[-PI, PI],
            v_range=[0, TAU]
        )

        #연습용
        self.circle = Circle(radius=1.5, color=GREEN)
        self.square = Square()
        self.triangle = Triangle()



        #애니메이션 실행 메서드
        self.do_animation("1. lag_ratio=0", 1)

    def func(self, u, v):
        return np.array([np.cos(u) * np.cos(v), np.cos(u) * np.sin(v), u])

    def do_animation(self, name, ratio):
        pass
        self.add(self.intro_object, self.axes, self.surface)

        animation1 = [
            Create(self.axes, run_time=2),
            Create(self.surface, run_time=2)
        ]

        animation2 = [
            FadeOut(self.axes, run_time=2),
            FadeOut(self.surface, run_time=2),
        ]

        # 그래프 그리기
        animation_group1 = AnimationGroup(*animation1, lag_ratio=ratio,)
        #그래프 지우기
        animation_group2 = AnimationGroup(*animation2, lag_ratio=ratio, )


        self.play(Create(self.intro_object))
        self.play(self.intro_object.animate.scale(1.5))
        self.play(self.intro_object.animate.clear_content())
        self.play(FadeOut(self.intro_object))
        self.wait(1)
        self.set_camera_orientation(theta=70 * DEGREES, phi=75 * DEGREES)
        self.play(animation_group1)
        self.play(animation_group2)
        self.wait(2)


#실행부분
if __name__ == '__main__':

    scene = RenderProject()
    scene.render()

