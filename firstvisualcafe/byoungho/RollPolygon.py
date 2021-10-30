from manim import *

class Roll(Scene):
    def construct(self):
        n = 5
        r = 1
        ang = PI*(n-2)/n
        l = 2 * r * np.cos(ang/2)
        
        poly = RegularPolygon(n, radius=r).shift(LEFT*2)
        
        self.play(Create(poly))
        self.wait()
        
        for i in range(n):
            fixedpoint = Dot(poly.get_bottom()).shift(RIGHT*l/2)
            self.play(Rotate(
                poly, about_point=fixedpoint.get_center(), angle=ang-PI, rate_func=linear
                ))
        
        self.wait()