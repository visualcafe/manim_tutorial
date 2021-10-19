from manim import *
class WheelTrace(Scene):
    def construct(self):
        def rotateandshift(mob, alpha):
            mob.shift(RIGHT * alpha / 10)
            mob.rotate(angle=-alpha / 10, about_point=mob.get_center())


        circ = Circle(color=RED).shift(4 * LEFT)
        dot = (
            Dot(color=RED)
                .move_to(circ.get_end())
               .add_updater(lambda m: m.move_to(circ.get_end()))
        )

        trace = TracedPath(circ.get_end)
        self.add(trace, circ, dot)
        circ.rotate(angle=3 * PI / 2, about_point=circ.get_center()).shift(0.7 * LEFT)
        self.play(UpdateFromAlphaFunc(circ, rotateandshift), run_time=5)
        self.wait()


if __name__ == '__main__':
    scene = WheelTrace()
    scene.render()