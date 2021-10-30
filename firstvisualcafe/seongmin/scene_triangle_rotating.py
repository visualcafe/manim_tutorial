from manim import *
import numpy as np


#속도개선 필요
#트레이스 추가

class TriangleRotating(Scene):
    def construct(self):
        #음.... 일단 삼각형과같이 다각형 클래스중에 이름있는것
        #예를들어 사각형 삼각형 이런것들은 수정하기가 어렵습니다.
        #따라서 polygon클래스를 이용해서 객체를 생성하는편이 좋은것 같습니다.
        
        triangle = Polygon(
            ORIGIN,
            RIGHT,
            RIGHT/2 + UP*np.sin(PI/3)
        )
        self.add(triangle)
        for i in range(4):
            self.play(Rotating(triangle, about_point=LEFT*i, radians=2*PI/3))
            

if __name__ == "__main__":
    scene = TriangleRotating()
    scene.render()