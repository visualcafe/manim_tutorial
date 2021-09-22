from manim import *

"""
    비주얼 카페 로고입니다. 
    ManimBanner 상속받아서 만들려 했지만
    latex문제때문에...
    2021-09-22
"""
__all__ = ["VisualCafeIntro"]

class VisualCafeIntro(VGroup):
    def __init__(self, content):
        super().__init__()
        self.circle = Circle()
        self.dodecahedron = Dodecahedron()
        self.content = content

        self.shapes = VGroup(self.circle, self.dodecahedron, self.content)
        self.add(self.shapes)

        content.move_to(self.circle.get_center())

    def clear_content(self):
        self.remove(self.circle)
        self.circle = None

        self.remove(self.dodecahedron)
        self.dodecahedron = None

        self.remove(self.content)
        self.content = None

    @override_animate(clear_content)
    def _clear_content_animation(self, anim_args=None):
        if anim_args is None:
            anim_args = {}
        anim = Uncreate(self.content, **anim_args)
        self.clear_content()
        return anim



