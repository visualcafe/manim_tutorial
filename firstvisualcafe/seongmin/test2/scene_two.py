from manim import *


# 객체 클래스
class Wheels(Scene):
    """
    [1][객체 생성]

    1. 트래커 변수
    2. 큰원
        -큰원 아래 붙어있는 점
        -큰원 아래 처음에만 붙어있는점
        -큰원 아래 그려주는 라인
    3. 작은원
        -작은원 아래 붙어있는 점
        -작은원 아래 처음에만 붙어있는점
        -작은원 아래 그려주는 라인
    4. 반지름 (큰원에 붙어있음)
    5. 원의 중심        
    6. 설명객체들
        - 등호 2개
        - 물음표
        - 설명 텍스트

    [2][업데이터 등록]
    [3][업데이터 해제]
    """

    #[1][객체 생성]
    def __init__(self):

        # 트래커 변수
        self.circle_tracker = ValueTracker(0)

        # 큰원
        self.circleBig = Circle(radius=1.0,
                                stroke_color=RED,
                                stroke_opacity=1.0,
                                fill_color=RED,
                                fill_opacity=0.5).shift(RIGHT * (-PI))

        # 큰원 아래붙어있는 점
        self.circleBig_UnderDot = Dot(fill_color=RED,
                                      fill_opacity=1.0).move_to(
                                          self.circleBig.get_bottom())

        # 큰원 아래 처음에만 붙어있는점
        self.circleBig_UnderDot_NotMoving = Dot(
            fill_color=RED,
            fill_opacity=1.0).move_to(self.circleBig.get_bottom())

        # 큰원 아래 그려주는 라인
        self.circleBig_UnderLine = Line(
            start=self.circleBig.get_bottom(),
            end=self.circleBig_UnderDot.get_center(),
            stroke_color=RED)

        # 작은 원
        self.circleSmall = Circle(radius=0.5,
                                  stroke_color=YELLOW,
                                  stroke_opacity=1.0,
                                  fill_color=YELLOW,
                                  fill_opacity=0.5).shift(RIGHT * (-PI))

        # 작은원 아래 붙어있는 점
        self.circleSmall_UnderDot = Dot(fill_color=YELLOW,
                                        fill_opacity=1.0).move_to(
                                            self.circleSmall.get_bottom())

        # 작은원 아래 처음에만 붙어있는점
        self.circleSmall_UnderDot_NotMoving = Dot(
            fill_color=YELLOW,
            fill_opacity=1.0).move_to(self.circleSmall.get_bottom())

        # 작은원 아래 그려주는 라인
        self.circleSmall_UnderLine = Line(
            start=self.circleSmall.get_bottom(),
            end=self.circleSmall_UnderDot.get_center(),
            stroke_color=YELLOW)

        # 반지름
        self.circleBig_RadiusLine = Line(start=self.circleBig.get_center(),
                                         end=self.circleBig.get_bottom())

        # 원의 중심
        self.centerDot = Dot(color=WHITE).shift(RIGHT * (-PI))

        # 등호
        self.equals_1 = MathTex(r"=").shift(DOWN + RIGHT * PI * 5 / 8)
        self.equals_2 = MathTex(r"=").shift(UP + RIGHT * PI * 5 / 8)
        # 물음표
        self.ques_m = MathTex(r"?", font_size=144).shift(UP * 2.5 +
                                                         RIGHT * PI * 7 / 4)
        # 설명
        self.caption1 = Tex(
            "Let's roll two circles which have the same center.").to_edge(
                DOWN, buff=1)

    # [2][업데이터 등록]
    def wheel_Add_Updater(self):

        self.circleBig.add_updater(
            lambda mob: mob.move_to(self.centerDot.get_center()))

        self.circleBig_UnderDot.add_updater(
            lambda mob: mob.move_to(self.circleBig.get_bottom()))

        self.circleBig_UnderLine.add_updater(lambda mob: mob.become(
            Line(self.circleBig_UnderDot_NotMoving.get_center(),
                 self.circleBig_UnderDot.get_center(),
                 stroke_color=RED)))

        self.circleSmall.add_updater(
            lambda mob: mob.move_to(self.centerDot.get_center()))

        self.circleSmall_UnderDot.add_updater(
            lambda mob: mob.move_to(self.circleSmall.get_bottom()))

        self.circleSmall_UnderLine.add_updater(lambda mob: mob.become(
            Line(self.circleSmall_UnderDot_NotMoving.get_center(),
                 self.circleSmall_UnderDot.get_center(),
                 stroke_color=YELLOW)))

        self.circleBig_RadiusLine.add_updater(
            lambda mob: mob.put_start_and_end_on(
                self.circleBig.get_center(),
                self.circleBig.point_at_angle((3 * PI / 2 - self.circle_tracker
                                               .get_value()) % (2 * PI))))

    # [3][업데이터 등록 해제]
    def wheel_Clear_Updaters(self):

        self.circleBig.clear_updaters()
        self.circleBig_UnderDot.clear_updaters()
        self.circleBig_UnderDot_NotMoving.clear_updaters()
        self.circleBig_UnderLine.clear_updaters()
        self.circleBig_RadiusLine.clear_updaters()

        self.circleSmall.clear_updaters()
        self.circleSmall_UnderDot.clear_updaters()
        self.circleSmall_UnderDot_NotMoving.clear_updaters()
        self.circleSmall_UnderLine.clear_updaters()


# 랜더링 클래스
class WheelParadox(Scene):
    def construct(self):

        #객체들 생성및 업데이터 등록
        wheels = Wheels()
        wheels.wheel_Add_Updater()

        #화면 처음 [애니메이션]
        self.play(
            LaggedStart(Create(wheels.circleBig),
                        Create(wheels.circleBig_UnderDot),
                        Create(wheels.circleBig_UnderLine),
                        Create(wheels.circleSmall),
                        Create(wheels.circleSmall_UnderDot),
                        Create(wheels.circleSmall_UnderLine),
                        Create(wheels.circleBig_RadiusLine),
                        lag_ratio=0.5))

        self.wait(0.5)

        #한바퀴 굴림 [애니메이션]
        self.play(
            AnimationGroup(wheels.centerDot.animate.shift(RIGHT * (2 * PI)),
                           wheels.circle_tracker.animate.shift(RIGHT *
                                                               (2 * PI)),
                           run_time=5))
        self.wait(0.5)

        # 업데이터 등록 해제
        wheels.wheel_Clear_Updaters()

        # 필요없는 객체들 지우기 [애니메이션]
        self.remove(wheels.centerDot, wheels.circleBig_UnderDot,
                    wheels.circleBig_UnderDot_NotMoving,
                    wheels.circleBig_RadiusLine, wheels.circleSmall_UnderDot,
                    wheels.circleSmall_UnderDot_NotMoving)

        # 객체들 해체 [애니메이션]
        self.play(
            wheels.circleBig.animate.shift(UP + RIGHT * PI / 4),
            wheels.circleSmall.animate.shift(DOWN + RIGHT * PI / 4),
            wheels.circleBig_UnderLine.animate.shift(UP * 1.5 +
                                                     LEFT * PI * 3 / 4),
            wheels.circleSmall_UnderLine.animate.shift(LEFT * PI * 3 / 4))

        self.wait(0.5)

        # 설명글 [애니메이션]
        self.play(
            AnimationGroup(Write(wheels.caption1), Write(wheels.equals_1),
                           Write(wheels.equals_2), Write(wheels.ques_m)))

        self.wait(1)

        # 화면 클리어
        self.clear()

        wheels2 = Wheels()
        wheels2.wheel_Add_Updater()

        # 필요없는 객체들 지우기 [애니메이션]
        self.remove(wheels2.circleBig_UnderDot,
                    wheels2.circleBig_UnderDot_NotMoving,
                    wheels2.circleBig_UnderLine, wheels2.circleBig_RadiusLine,
                    wheels2.circleSmall_UnderDot,
                    wheels2.circleSmall_UnderDot_NotMoving,
                    wheels2.circleSmall_UnderLine)

        wheels2.centerDot

        self.play(Create(wheels2.circleBig), Create(wheels2.circleSmall))

        tracker = ValueTracker(100)

        regularPolygon = RegularPolygon(3,
                                        radius=1.0,
                                        fill_opacity=0,
                                        fill_color=RED).move_to(
                                            wheels2.circleBig.get_center())

        regularPolygon.origin

        def update_func(mob):
            n = int(tracker.get_value())
            new_mob = RegularPolygon(n,
                                     radius=3,
                                     fill_opacity=0,
                                     fill_color=RED).move_to(
                                         wheels2.circleBig.get_center())
            mob.become(new_mob)

        self.add(regularPolygon)
        self.play(tracker.animate.set_value(3),
                  UpdateFromFunc(regularPolygon, update_func),
                  run_time=8,
                  lag_ratio=1)
        self.wait(2)


#실행부분
if __name__ == '__main__':

    scene = WheelParadox()
    scene.render()
