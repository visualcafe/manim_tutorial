from manim import *
import numpy as np
class OneParameterFunc(ThreeDScene):
    def construct(self):
        #좌표축 주의: Axes 아님
        axes = ThreeDAxes(
            x_range=[-1, 1, 0.2],
            y_range=[0, 0.5, 0.2],
            z_range=[0, 2, 0.2],
            x_length=7,
            y_length=7,
            z_length=7,
        ).add_coordinates()

        #BulletedList 를 사용하는것 보다 그냥 이렇게 만들어서 사용하는게 좋은것 같습니다.
        #이유는 사이에 buff를 마음대로 넣을 수 있기 때문입니다.
        word = Tex("sin(6t)", "t/4", "t\^2")
        for part in word:
            dot = MathTex("\\cdot").scale(4)
            dot.next_to(part[0], LEFT, buff=0.4)
            part.add_to_back(dot)
        word.arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        graph = axes.get_parametric_curve(
            lambda t: np.array([np.sin(6*t), t/4, t**2/2]),
            t_range=[0, 2],
            color=BLUE
        )
        self.add(axes)
        self.play(Write(word))
        self.wait()
        self.play(word.animate.to_edge(UR).scale(0.5))

        ##THE CAMERA IS AUTO SET TO PHI = 0 and THETA = -90

        self.move_camera(phi=60 * DEGREES)
        self.wait()
        self.move_camera(theta=-45 * DEGREES)

        self.begin_ambient_camera_rotation(
            rate=PI / 10, about="theta"
        )  # Rotates at a rate of radians per second
        self.wait()
        self.play(Create(graph))
        self.wait()
        self.stop_ambient_camera_rotation()

        self.wait()
        self.begin_ambient_camera_rotation(
            rate=-2*PI / 10, about="theta"
        )  # Rotates at a rate of radians per second
        self.wait(2)
        self.stop_ambient_camera_rotation()

if __name__ == "__main__":
    scene = OneParameterFunc()
    scene.render()
