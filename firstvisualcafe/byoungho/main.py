# import sys
# sys.path.append('../../')

from manim import *

class Practice(Scene):
  def construct(self):
      poly_3 = RegularPolygon(3, radius=1)
      poly_4 = RegularPolygon(4, radius=1)
      poly_5 = RegularPolygon(5, radius=1)
      poly_6 = RegularPolygon(6, radius=1)
      print('3-----------------------')
      print(poly_3.get_vertices())
      print('4-----------------------')
      print(poly_4.get_vertices())
      print('5-----------------------')
      print(poly_5.get_vertices())
      print('6-----------------------')
      print(poly_6.get_vertices())
      
      

# if __name__ == '__main__':

#     scene = Tute()
#     scene.render()