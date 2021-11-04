from manim import *
# from VisualCafe import *
# from VisualCafe.scene.visualcafescene2d import *

# class NotImportant1(VisualCafeScene2D):
#     def construct(self):
#         e = ValueTracker(0)

#         dot = always_redraw(lambda: Dot().shift(RIGHT * (-PI + e.get_value())))
#         circle1 = always_redraw(
#             lambda: Circle(radius=1.0, stroke_color=RED, stroke_opacity=1.0, fill_color=RED, fill_opacity=0.5).shift(
#                 RIGHT * (-PI + e.get_value())))
#         circle2 = always_redraw(lambda: Circle(radius=0.5, stroke_color=YELLOW, stroke_opacity=1.0, fill_color=YELLOW,
#                                                fill_opacity=0.5).shift(RIGHT * (-PI + e.get_value())))
#         radius = always_redraw(lambda: Line(start=circle1.get_center(),
#                                             end=circle1.point_at_angle((3 * PI / 2 - e.get_value()) % (2 * PI))))

#         self.play(Create(circle1))
#         self.play(Create(dot))

# class Count(Animation):
#     def __init__(self, math_tex: Tex, start: int, end: int, **kwargs) -> None:
#         super().__init__(math_tex,  **kwargs)
#         self.start = start
#         self.end = end


#     def interpolate_mobject(self, alpha: float) -> None:
#         y = str(int(self.start + (alpha * (self.end - self.start))))
#         self.mobject.become(Text(r"2^{{"+y+r"}} \neq {{"+y+r"}}^2"))

# class c2s2(Scene):
#     def construct(self):
#         eq = Text(r"2^{{3}} \neq {{3}}^2")
#         eq.add_updater(lambda x: x.move_to(ORIGIN))

#         self.play(FadeIn(eq))

#         self.play(Count(eq, 3, 100), run_time=4, rate_func=linear)

# class creation(Scene):
#     def construct(self):
#         creation = [Create,DrawBorderThenFill,ShowIncreasingSubsets,ShowSubmobjectsOneByOne,Write,AddTextLetterByLetter]
#         names = [Text(i.__name__).scale(1.2) for i in creation]

#         for i in range(len(names)):
#             names[i].shift(UP)
#         circle = Circle(fill_opacity=0.5, fill_color=ORANGE).shift(DOWN)
#         self.add(names[0])
#         for i in range(len(names)):

#             self.play(creation[i](names[i]))
#             if creation[i] is ShowIncreasingSubsets:
#                 vg = VGroup(Circle().shift(DOWN,LEFT*2), Triangle().shift(DOWN), Square().shift(DOWN,RIGHT*2))
#                 self.play(creation[i](vg))
#                 self.play(FadeOut(vg))
#             else:
#                 self.play(creation[i](circle))
#                 self.play(FadeOut(circle))
#             self.play(AnimationGroup(
#                 FadeOut(names[i], shift=UP * 1.5),
#                 FadeIn(names[(i+1)%len(names)], shift=UP*1.5),
#             ))

# class trianglevertices(Scene):
#     def construct(self):
#         triangle = Triangle().shift(LEFT*2)
#         tri_arr = triangle.get_vertices() # 어레이로 리턴함. 삼각형이니깐 이중어레이 3개의 꼭짓점이므로 3요소를 가짐 근데 요소안의 요소도 3요소임.xyz이기 때문임.
#         for arr in tri_arr:
#             self.play(Create(Dot().move_to(arr)))
#         triangle.rotate()

# class triangleverticestrace(Scene):
#     def construct(self):
#         def updater_back(mobj, dt):
#             mobj.rotate(dt)

#         e = ValueTracker(0)
#         triangle = Triangle()
#         triangle.set_center(triangle.get_vertices()[0])
#         triangle_redraw = always_redraw(lambda : triangle.shift(RIGHT*(-PI+e.get_value())))
#         dot1 = always_redraw(lambda : Dot().move_to(triangle_redraw.get_vertices()[0]))
#         dot2 = always_redraw(lambda : Dot().move_to(triangle_redraw.get_vertices()[1]))
#         dot3 = always_redraw(lambda : Dot().move_to(triangle_redraw.get_vertices()[2]))

#         # triangle.add_updater(updater_back)
#         triangle_redraw.set_center(dot1.get_center())
#         self.add(triangle_redraw)
#         self.play(Create(dot1), Create(dot2), Create(dot3))
#         self.play(Rotate(triangle_redraw, angle=-2*(PI/3)))
#         # self.play(e.animate.set_value(2*PI), run_time=4)
# class Roll(Scene):

#     def polygon_roll_function(self, n: int, radius: int, times: int):
#             ang = PI*(n-2)/n
#             length = 2 * radius * np.cos(ang/2)
            
#             poly = RegularPolygon(n, radius=radius).shift(LEFT*2)
#             poly2 = RegularPolygon(n, radius=radius).shift(LEFT*2)
            
            

#             rotate_animation = []
#             fixedpoints = []
#             polys = []
#             for i in range(times):
#                 fixedpoint = Dot(poly.get_bottom()).shift(RIGHT*length/2)
#                 polys.append(poly)
#                 fixedpoints.append(fixedpoint)
#                 polys.append(poly.rotate(about_point=fixedpoints[i].get_center(), angle=ang-PI))
#                 # self.play(Rotate(poly, about_point=fixedpoints[i].get_center(), angle=ang-PI, rate_func=linear))
            
#             # rotate_animation.append(Rotate(polys[i], about_point=fixedpoints[i].get_center(), angle=ang-PI, rate_func=linear))
            
#             self.play(Succession(*rotate_animation))

    # def construct(self):
    #     n = 5
    #     r = 1
    #     # self.polygon_roll_function(n,r, 5)

    #     self.polygon_roll_function(n, r, n)
    #     self.wait()
class UpdaterTest(Scene):
    def construct(self):
        circleBig = Circle(
            radius=1.0, stroke_color=RED, stroke_opacity=1.0, fill_color=RED, fill_opacity=0.5
        ).shift(
            RIGHT * (-PI)
        )

        circleSmall = Circle(
            radius=0.5, stroke_color=YELLOW, stroke_opacity=1.0, fill_color=YELLOW, fill_opacity=0.5
        ).shift(
            RIGHT * (-PI)
        )

        centerDot = Dot(
            color = BLUE
        ).shift(
            RIGHT * (-PI)
        )
        circleBig.add_updater(lambda x: x.move_to(centerDot.get_center()))
        self.add(circleBig, circleSmall, centerDot)
        self.play(centerDot.animate.shift(RIGHT*8))
        

#실행부분
if __name__ == '__main__':

    scene = UpdaterTest()
    scene.render()