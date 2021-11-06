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
    """

    # 트래커 변수
    circle_tracker = ValueTracker(0)

    # 큰원
    circleBig = Circle(radius=1.0,
                       stroke_color=RED,
                       stroke_opacity=1.0,
                       fill_color=RED,
                       fill_opacity=0.5).shift(RIGHT * (-PI))

    # 큰원 아래붙어있는 점
    circleBig_UnderDot = Dot(fill_color=RED,
                             fill_opacity=1.0).move_to(circleBig.get_bottom())

    # 큰원 아래 처음에만 붙어있는점
    circleBig_UnderDot_NotMoving = Dot(
        fill_color=RED, fill_opacity=1.0).move_to(circleBig.get_bottom())

    # 큰원 아래 그려주는 라인
    circleBig_UnderLine = Line(start=circleBig.get_bottom(),
                               end=circleBig_UnderDot.get_center(),
                               stroke_color=RED)

    # 작은 원
    circleSmall = Circle(radius=0.5,
                         stroke_color=YELLOW,
                         stroke_opacity=1.0,
                         fill_color=YELLOW,
                         fill_opacity=0.5).shift(RIGHT * (-PI))

    # 작은원 아래 붙어있는 점
    circleSmall_UnderDot = Dot(fill_color=YELLOW, fill_opacity=1.0).move_to(
        circleSmall.get_bottom())

    # 작은원 아래 처음에만 붙어있는점
    circleSmall_UnderDot_NotMoving = Dot(
        fill_color=YELLOW, fill_opacity=1.0).move_to(circleSmall.get_bottom())

    # 작은원 아래 그려주는 라인
    circleSmall_UnderLine = Line(start=circleSmall.get_bottom(),
                                 end=circleSmall_UnderDot.get_center(),
                                 stroke_color=YELLOW)

    # 반지름
    circleBig_RadiusLine = Line(start=circleBig.get_center(),
                                end=circleBig.get_bottom())

    # 원의 중심
    centerDot = Dot(color=WHITE).shift(RIGHT * (-PI))

    # 등호
    equals_1 = MathTex(r"=").shift(DOWN + RIGHT * PI * 5 / 8)
    equals_2 = MathTex(r"=").shift(UP + RIGHT * PI * 5 / 8)
    # 물음표
    ques_m = MathTex(r"?", font_size=144).shift(UP * 2.5 + RIGHT * PI * 7 / 4)
    # 설명
    caption1 = Tex(
        "Let's roll two circles which have the same center.").to_edge(DOWN,
                                                                      buff=1)


# 랜더링 클래스
class WheelParadox(Scene):
    def construct(self):
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
        """

        # # 트래커 변수
        # circle_tracker = ValueTracker(0)

        # # 큰원
        # circleBig = Circle(radius=1.0,
        #                    stroke_color=RED,
        #                    stroke_opacity=1.0,
        #                    fill_color=RED,
        #                    fill_opacity=0.5).shift(RIGHT * (-PI))

        # # 큰원 아래붙어있는 점
        # circleBig_UnderDot = Dot(fill_color=RED, fill_opacity=1.0).move_to(
        #     circleBig.get_bottom())

        # # 큰원 아래 처음에만 붙어있는점
        # circleBig_UnderDot_NotMoving = Dot(
        #     fill_color=RED, fill_opacity=1.0).move_to(circleBig.get_bottom())

        # # 큰원 아래 그려주는 라인
        # circleBig_UnderLine = Line(start=circleBig.get_bottom(),
        #                            end=circleBig_UnderDot.get_center(),
        #                            stroke_color=RED)

        # # 작은 원
        # circleSmall = Circle(radius=0.5,
        #                      stroke_color=YELLOW,
        #                      stroke_opacity=1.0,
        #                      fill_color=YELLOW,
        #                      fill_opacity=0.5).shift(RIGHT * (-PI))

        # # 작은원 아래 붙어있는 점
        # circleSmall_UnderDot = Dot(fill_color=YELLOW,
        #                            fill_opacity=1.0).move_to(
        #                                circleSmall.get_bottom())

        # # 작은원 아래 처음에만 붙어있는점
        # circleSmall_UnderDot_NotMoving = Dot(fill_color=YELLOW,
        #                                      fill_opacity=1.0).move_to(
        #                                          circleSmall.get_bottom())

        # # 작은원 아래 그려주는 라인
        # circleSmall_UnderLine = Line(start=circleSmall.get_bottom(),
        #                              end=circleSmall_UnderDot.get_center(),
        #                              stroke_color=YELLOW)

        # # 반지름
        # circleBig_RadiusLine = Line(start=circleBig.get_center(),
        #                             end=circleBig.get_bottom())

        # # 원의 중심
        # centerDot = Dot(color=WHITE).shift(RIGHT * (-PI))

        # # 등호
        # equals_1 = MathTex(r"=").shift(DOWN + RIGHT * PI * 5 / 8)
        # equals_2 = MathTex(r"=").shift(UP + RIGHT * PI * 5 / 8)
        # # 물음표
        # ques_m = MathTex(r"?",
        #                  font_size=144).shift(UP * 2.5 + RIGHT * PI * 7 / 4)
        # # 설명
        # caption1 = Tex(
        #     "Let's roll two circles which have the same center.").to_edge(
        #         DOWN, buff=1)
        wheels = Wheels()
        """
        [2][업데이터를 등록합니다]
        
        """
        wheels.circleBig.add_updater(
            lambda mob: mob.move_to(wheels.centerDot.get_center()))

        wheels.circleBig_UnderDot.add_updater(
            lambda mob: mob.move_to(wheels.circleBig.get_bottom()))

        wheels.circleBig_UnderLine.add_updater(lambda mob: mob.become(
            Line(wheels.circleBig_UnderDot_NotMoving.get_center(),
                 wheels.circleBig_UnderDot.get_center(),
                 stroke_color=RED)))

        wheels.circleSmall.add_updater(
            lambda mob: mob.move_to(wheels.centerDot.get_center()))

        wheels.circleSmall_UnderDot.add_updater(
            lambda mob: mob.move_to(wheels.circleSmall.get_bottom()))

        wheels.circleSmall_UnderLine.add_updater(lambda mob: mob.become(
            Line(wheels.circleSmall_UnderDot_NotMoving.get_center(),
                 wheels.circleSmall_UnderDot.get_center(),
                 stroke_color=YELLOW)))

        wheels.circleBig_RadiusLine.add_updater(
            lambda mob: mob.put_start_and_end_on(
                wheels.circleBig.get_center(),
                wheels.circleBig.point_at_angle(
                    (3 * PI / 2 - wheels.circle_tracker.get_value()) %
                    (2 * PI))))
        """
        [3][애니메이션을 실행합니다.]
        """

        #처음 생성
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

        #한바퀴 굴림
        self.play(
            AnimationGroup(wheels.centerDot.animate.shift(RIGHT * (2 * PI)),
                           wheels.circle_tracker.animate.shift(RIGHT *
                                                               (2 * PI)),
                           run_time=5))
        self.wait(0.5)

        # 업데이터 등록 해제

        wheels.circleBig.clear_updaters()
        wheels.circleBig_UnderDot.clear_updaters()
        wheels.circleBig_UnderDot_NotMoving.clear_updaters()
        wheels.circleBig_UnderLine.clear_updaters()
        wheels.circleBig_RadiusLine.clear_updaters()

        wheels.circleSmall.clear_updaters()
        wheels.circleSmall_UnderDot.clear_updaters()
        wheels.circleSmall_UnderDot_NotMoving.clear_updaters()
        wheels.circleSmall_UnderLine.clear_updaters()

        # 필요없는 객체들 지우기
        self.remove(wheels.centerDot, wheels.circleBig_UnderDot,
                    wheels.circleBig_UnderDot_NotMoving,
                    wheels.circleBig_RadiusLine, wheels.circleSmall_UnderDot,
                    wheels.circleSmall_UnderDot_NotMoving)

        # 객체들 해체
        self.play(
            wheels.circleBig.animate.shift(UP + RIGHT * PI / 4),
            wheels.circleSmall.animate.shift(DOWN + RIGHT * PI / 4),
            wheels.circleBig_UnderLine.animate.shift(UP * 1.5 +
                                                     LEFT * PI * 3 / 4),
            wheels.circleSmall_UnderLine.animate.shift(LEFT * PI * 3 / 4))

        self.wait(0.5)

        self.play(
            AnimationGroup(Write(wheels.caption1), Write(wheels.equals_1),
                           Write(wheels.equals_2), Write(wheels.ques_m)))

        self.wait(1)

        # 화면 클리어
        self.clear()
        """
                value tracker랑 UpdateFromFunc 클래스를 사용해서
                100각형을 3각형으로 만들어줍니다. 위와 다를바 없습니다.
                성능도 별 차이 없던것 같습니다.
                오히려 lag_ratio랑 런타임을 조정해서 스피드를 조정하는게
                더 어렵습니다. 100각형은 눈에 잘 보이지도 않습니다.
                """
        tracker = ValueTracker(100)
        rp = RegularPolygon(3, fill_opacity=0, fill_color=RED)

        def update_func(mob):
            n = int(tracker.get_value())
            new_mob = RegularPolygon(n,
                                     radius=3,
                                     fill_opacity=0,
                                     fill_color=RED)
            mob.become(new_mob)

        self.add(rp)
        self.play(tracker.animate.set_value(3),
                  UpdateFromFunc(rp, update_func),
                  run_time=8,
                  lag_ratio=1)
        self.wait(2)


#실행부분
if __name__ == '__main__':

    scene = WheelParadox()
    scene.render()
