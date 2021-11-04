from manim import *

class circle(Scene):
    def construct(self):
        circle = Circle(radius=1,color='#FFFFFF').set_fill(opacity=1).move_to(DOWN)
        self.play(Create(circle))
        self.wait()

        #Take out a slice
        circle_center = circle.get_center()
        sector = Sector(outer_radius=1,inner_radius=0,angle=PI/4,arc_center=circle_center).set_color(BLACK)
        self.play(Create(sector))
        self.wait()

if __name__ == "__main__":
    scene = circle();
    scene.render();