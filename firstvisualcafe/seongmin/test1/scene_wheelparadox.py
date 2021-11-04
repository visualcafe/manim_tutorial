from manim import *
from VisualCafe.VGroup.visualcafeintro import *
from VisualCafe.scene.visualcafescene3d import *
import VisualCafe.QuadricSurfaces as vcq

#랜더링 클래스
class WheelParadox(VisualCafeScene3D):
    def visualcafe_construct(self):
        self.circleBig = Circle()
        tracker = ValueTracker(3)

        self.circleBig = Circle(radius=3).shift(LEFT*2)
        self.add(self.circleBig)
        for i in range(3, 15):
            ss = RegularPolygon(17 - i, radius=3, fill_opacity=0, fill_color=RED)
            ss.add_updater(lambda mob : mob.next_to(self.circleBig.get_center(), ORIGIN))
            self.add(ss)
            self.wait(0.2)
            self.remove(ss)
        self.wait(2)

        """
        value tracker랑 UpdateFromFunc 클래스를 사용해서
        100각형을 3각형으로 만들어줍니다. 위와 다를바 없습니다. 
        성능도 별 차이 없던것 같습니다.
        오히려 lag_ratio랑 런타임을 조정해서 스피드를 조정하는게
        더 어렵습니다. 100각형은 눈에 잘 보이지도 않습니다.
        """
        # tracker = ValueTracker(100)
        # rp = RegularPolygon(3, fill_opacity=0, fill_color=RED)
        #
        # def update_func(mob):
        #     n = int(tracker.get_value())
        #     new_mob = RegularPolygon(n, radius=3, fill_opacity=0, fill_color=RED)
        #     mob.become(new_mob)
        #
        # self.add(rp)
        # self.play(tracker.animate.set_value(3), UpdateFromFunc(rp, update_func), run_time=20, lag_ratio=2)
        # self.wait(2)
#실행부분
if __name__ == '__main__':

    scene = WheelParadox()
    scene.render()

