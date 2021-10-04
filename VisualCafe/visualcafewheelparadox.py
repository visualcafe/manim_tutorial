from manim import *

class VisualCafeWheelParadox(VGroup):
    def __init__(self):
        #큰원
        self.circle = Circle()
        #100 ~ 3각형
        for i in list(range(100, 3, -1)):
            pass