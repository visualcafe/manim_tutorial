from manim import *

class HypoCycloid(Scene):
    def construct(self):
        circle = Circle(radius=4)
        fixedpoint = Dot(point=circle.point_from_proportion(0)).save_state()
        rotatingpoint = fixedpoint.copy()
        smolcircle = circle.copy()
        smolcircle.move_to(circle.get_right()).scale(0.25).shift(LEFT).save_state()

        trace = TracedPath(rotatingpoint.get_center, color=BLUE)

        def moving(mob, alpha):
            mob1, mob2, mob3 = mob
            mob1.restore()
            mob2.restore()
            mob1.rotate(angle=6 * alpha, about_point=circle.get_center())
            mob2.rotate(angle=6 * alpha, about_point=circle.get_center()).set_color(GREEN).set_opacity(0)
            mob3.become(mob2.copy().rotate(angle=-4 * 6 * alpha, about_point=mob1.get_center())).set_color(
                YELLOW).set_opacity(1)

        mob = VGroup(smolcircle, fixedpoint, rotatingpoint)
        self.add(circle, smolcircle, trace, mob[0], mob[2])
        self.play(UpdateFromAlphaFunc(mob, moving), run_time=2 * PI)

if __name__ == '__main__':
    scene = HypoCycloid()
    scene.render()