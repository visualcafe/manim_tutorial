from manim import *

class Szene11(Scene):
    def construct(self):
        def func(pos):
            a =pos
            return (2/(np.linalg.norm(a if (np.linalg.norm(a)>0.1) else np.array([100,100,100])))**2)*(a)
        vector_field = ArrowVectorField(func, delta_x=1, delta_y=1, length_func=lambda x:x/2)
        #self.add(vector_field)
        circle = Circle(radius=2).shift(LEFT)
        #self.add(circle.copy().set_color(GRAY))
        dot = Dot().move_to(circle)
        c2=circle.copy().set_color(GRAY)

        #vector_field.nudge(circle, -2, 60, True)
        #vector_field.nudge(dot, -2, 60)
        #vector_field.nudge(c2, -2, 60)

        #circle.add_updater(vector_field.get_nudge_updater(pointwise=True))
        #dot.add_updater(vector_field.get_nudge_updater())
        #c2.add_updater(vector_field.get_nudge_updater())
        
        stl=StreamLines(func,max_anchors_per_line=35)
        
        self.add(stl)
        stl.start_animation()
        self.wait(5)