from manim import *
from VisualCafe.VGroup.visualcafeintro import *
from VisualCafe.scene.visualcafescene3d import *
import VisualCafe.QuadricSurfaces as vcq

#랜더링 클래스
class TestUpdaters(Scene):
    def construct(self):
        self.circleBig = Circle(radius=3)
        self.add(self.circleBig)
        tracker = ValueTracker(100)
        rp = RegularPolygon(3, fill_opacity=0, fill_color=RED)

        def update_func(mob):
            n = int(tracker.get_value())
            new_mob = RegularPolygon(n, radius=3, fill_opacity=0, fill_color=RED)
            mob.become(new_mob)

        self.add(rp)
        self.play(tracker.animate.set_value(3), UpdateFromFunc(rp, update_func), run_time=20, lag_ratio=2)
        self.wait(2)
#실행부분
if __name__ == '__main__':

    scene = TestUpdaters()
    scene.render()

