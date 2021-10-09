from manim import *

class WheelParadoxFirst(Scene):
    def construct(self):
        e = ValueTracker(0)

        dot = always_redraw(lambda: Dot().shift(RIGHT*(-PI+e.get_value())))
        circle1 = always_redraw(lambda: Circle(radius=1.0, stroke_color=RED, stroke_opacity=1.0, fill_color=RED, fill_opacity=0.5).shift(RIGHT*(-PI+e.get_value())))
        circle2 = always_redraw(lambda: Circle(radius=0.5, stroke_color=YELLOW, stroke_opacity=1.0, fill_color=YELLOW, fill_opacity=0.5).shift(RIGHT*(-PI+e.get_value())))
        radius = always_redraw(lambda: Line(start=circle1.get_center(), end=circle1.point_at_angle((3*PI/2-e.get_value())%(2*PI))))
        
        start_point1 = circle1.get_bottom()
        start_point2 = circle2.get_bottom()
        
        dot1 = always_redraw(lambda: Dot(fill_color=RED, fill_opacity=1.0).move_to(circle1.get_bottom()))
        dot2 = always_redraw(lambda: Dot(fill_color=YELLOW, fill_opacity=1.0).move_to(circle2.get_bottom()))
        
        line1 = always_redraw(lambda: Line(start=start_point1, end=dot1, stroke_color=RED))
        line2 = always_redraw(lambda: Line(start=start_point2, end=dot2, stroke_color=YELLOW))
        
        equals_1 = MathTex(r"=").shift(DOWN+RIGHT*PI*5/8)
        equals_2 = MathTex(r"=").shift(UP+RIGHT*PI*5/8)
        ques_m = MathTex(r"?", font_size=144).shift(UP*2.5+RIGHT*PI*7/4)
        
        self.play(LaggedStart(Create(circle1), Create(circle2), Create(dot), Create(radius)))
        self.wait(0.5)
        self.play(FadeIn(dot1, dot2, line1, line2))
        self.wait(0.5)
        self.play(e.animate.set_value(2*PI), run_time=4)
        self.wait(0.5)
        self.play(FadeOut(dot1, dot2))
        self.play(FadeOut(radius, dot))
        
        circle1_ = Circle(radius=1.0, stroke_color=RED, stroke_opacity=1.0, fill_color=RED, fill_opacity=0.5).shift(RIGHT*PI)
        circle2_ = Circle(radius=0.5, stroke_color=YELLOW, stroke_opacity=1.0, fill_color=YELLOW, fill_opacity=0.5).shift(RIGHT*PI)
        line1_ = Line(start=start_point1, end=dot1, stroke_color=RED)
        line2_ = Line(start=start_point2, end=dot2, stroke_color=YELLOW)
        
        self.add(circle1_, circle2_, line1_, line2_)
        self.remove(circle1, circle2, line1, line2)
        
        self.play(circle2_.animate.shift(UP+RIGHT*PI/4),
                 circle1_.animate.shift(DOWN+RIGHT*PI/4),
                 line2_.animate.shift(UP*1.5+LEFT*PI*3/4),
                 line1_.animate.shift(LEFT*PI*3/4))
        self.wait(0.5)
        
        self.play(Write(equals_1), Write(equals_2))
        self.play(Write(ques_m))
        self.wait()
        self.play(FadeOut(line1_, line2_, circle1_, circle2_, equals_1, equals_2, ques_m))
        self.wait()
        

if __name__ == '__main__':

    scene = WheelParadoxFirst()
    scene.render()