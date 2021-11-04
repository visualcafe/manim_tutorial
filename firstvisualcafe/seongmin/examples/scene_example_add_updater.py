from manim import *

class vec1231(VectorScene):
      def construct(self):
          grid = NumberPlane(x_range=[-2,10,1], y_range=[-2,8,1]).add_coordinates()
          func=grid.get_graph(lambda x: x,x_range=[0,4.99],color=GREEN)
          self.add(grid)
          d=Dot(color=YELLOW).move_to(func.get_end()).set_z_index(func.get_z_index()+1)
          def upd(mob,dt):
              mob.move_to(func.get_end()).set_z_index(func.get_z_index()+1)
          d.add_updater(upd)
          self.add(d)
          line2=Line(ORIGIN,5*RIGHT,color=RED)
          d2=Dot(color=BLUE).move_to(line2.point_from_proportion((grid.p2c(d.get_center())[0]/5)%1))
          d2.add_updater(lambda c:c.become(Dot(color=BLUE).move_to(line2.point_from_proportion((grid.p2c(d.get_center())[0]/5)%1))))
          self.add(line2,d2)
          self.play(Write(func),run_time=3,rate_func=linear)
          self.wait(1)

if __name__ == "__main__":
    scene = vec1231();
    scene.render();