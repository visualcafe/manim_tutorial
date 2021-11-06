from manim import *
import numpy as np


class OneScala(ThreeDScene):
    def construct(self):
        #좌표축
        axes = ThreeDAxes(x_range=[-1, 1, 0.2],
                          x_length=8,
                          y_range=[0, 0.5, 0.2],
                          y_length=8,
                          z_range=[0, 2, 0.2],
                          z_length=8).add_coordinates()
        #좌표축에 그래프 추출
        graph = axes.get_parametric_curve(
            lambda t: np.array([np.sin(6 * t), 1 / 4 * t, t**2 / 2]),
            t_range=[0, 2],
            color=BLUE)

        #불렛리스트
        # blist = BulletedList(Text("x(t) = sin(6t)"),
        #                      Text("y(t) = t/4"),
        #                      Text("z(t) = t^2/2"),
        #                      height=2,
        #                      width=2)
        # blist.set_color_by_tex("x(t) = sin(6t)", RED)
        # blist.set_color_by_tex("y(t) = t/4", GREEN)
        # blist.set_color_by_tex("z(t) = t^2/2", BLUE)

        # self.play(Write(blist))
        # self.wait()
        # self.play(blist.animate.to_edge(UR).scale(0.5),
        #           runtime=2)  # 오른쪽 위로 위치시키고 스케일은 50%

        #불렛리스트
        word = Tex("x(t) = sin(6t)", "y(t) = t/4", "z(t) = t\^2/2")
        for part in word:
            dot = MathTex("\\cdot").scale(4)
            dot.next_to(part[0], LEFT, buff=0.4)
            part.add_to_back(dot)
            word.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
            self.add(word)
        for part in word:
            self.play(word.animate.to_edge(UR).scale(0.5))

        self.add(axes)
        self.wait()

        self.move_camera(phi=60 * DEGREES)
        self.wait()
        self.move_camera(theta=-45 * DEGREES)

        self.begin_ambient_camera_rotation(
            rate=PI / 10, about="theta")  # 라디안/second 속도로 돌아갑니다.
        self.wait()
        self.play(Create(graph))
        self.wait()
        self.stop_ambient_camera_rotation()

        self.wait()
        self.begin_ambient_camera_rotation(rate=-PI / 10, about="theta")
        self.wait(3)
        self.stop_ambient_camera_rotation()


if __name__ == "__main__":
    scene = OneScala()
    scene.render()