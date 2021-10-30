from manim import *

class RollPolygon(Scene):
    def construct(self):
        n = 5
        r = 1
        ang = PI*(n-2)/n
        l = 2 * r * np.cos(ang/2)
        wheels = 1
        
        poly = RegularPolygon(n, radius=r).shift(LEFT*(l*n/2))
        
        self.play(Create(poly))
        self.wait()
        
        for i in range(n*wheels):
            fixedpoint = Dot(poly.get_bottom()).shift(RIGHT*l/2)
            self.play(Rotate(
                poly, about_point=fixedpoint.get_center(), angle=ang-PI, rate_func=linear
                ))
        
        self.wait()
        
        def dkdk(n: int, t: str):
            