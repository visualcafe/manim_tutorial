from manim import *
import numpy as np

class TriangleRotating(Scene):
    def construct(self):
        #음.... 일단 삼각형과같이 다각형 클래스중에 이름있는것
        #예를들어 사각형 삼각형 이런것들은 수정하기가 어렵습니다.
        #따라서 polygon클래스를 이용해서 객체를 생성하는편이 좋은것 같습니다.
        theta = PI / 7
        triangle = Polygon(
            ORIGIN,
            RIGHT*(1+2*np.cos(2*theta)),
            RIGHT*(1+2*np.cos(2*theta)) + UP*2*np.sin(theta)*(np.cos(theta) + np.cos(3*theta))
            )
        self.add(triangle)
        self.play(Rotating(triangle, about_point=ORIGIN, radians=PI))

if __name__ == "main":
    scene = TriangleRotating()
    scene.render()