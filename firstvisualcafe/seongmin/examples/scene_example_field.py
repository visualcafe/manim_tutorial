from manim import *

class BasicUsage(Scene):
    def construct(self):
        r=ValueTracker(-1)
        func1 = lambda pos: (pos[1] * UP + (r.get_value()-pos[0]**2) *RIGHT)
        arfun1=ArrowVectorField(func1)
        self.wait()
        self.add(arfun1)
        arfun1.add_updater(lambda x: x.become(ArrowVectorField(func1)))
        self.play(r.animate.set_value(1),run_time=10)
        self.wait()

