import sys
sys.path.append('../../')

from manim import *
from VisualCafe.scene.visualcafescene2d import *

class Tute(VisualCafeScene2D):
  def visualcafe_construct(self):
      circle = Circle()
      self.add(circle)

if __name__ == '__main__':

    scene = Tute()
    scene.render()