from manim import *
from viettex import VietTex

class PythagoreanProof(Scene):
  def construct(self):
    def get_corner_coordinates(Object):
      return [
        Object.point_from_proportion(i * 1/4) for i in range(4)
      ]

    def get_triangle_coordinates(Object, Side):
      return [
        Object.point_from_proportion(i * 1/4 + 1/16) for i in range(4)
      ] if Side.lower() == "left" else [
        Object.point_from_proportion(i * 1/4 + j * 1/16) for i, j in zip(range(4), [1,3,3,1])
      ]

    left_square, right_square =  Square(), Square()
    VGroup(left_square,right_square).scale(2).arrange_submobjects(buff=2).set_z_index(1)

    self.play(*[Create(Dot(point=i, radius=0.05).set_z_index(3)) for i1 in [left_square,right_square] for i in get_corner_coordinates(i1)])
    self.play(Create(left_square), Create(right_square))

    corner_coords1 = get_corner_coordinates(left_square)
    corner_coords2 = get_corner_coordinates(right_square)

    triangles_coords1 = get_triangle_coordinates(left_square, "Left")
    triangles_coords2 = get_triangle_coordinates(right_square, "Right")

    self.play(*[Create(Dot(point=i, radius=0.05).set_z_index(3)) for i in triangles_coords1])
    self.play(*[Create(Dot(point=i, radius=0.05).set_z_index(3)) for i in triangles_coords2])
    
    middle_point = np.array([
        triangles_coords2[0][0],
        triangles_coords2[1][1],
        0
    ])

    triangles1 = VGroup(*[Polygon(triangles_coords1[i], corner_coords1[i], triangles_coords1[i-1], stroke_width=0, fill_opacity=0.7).set_z_index(0) for i in range(4)])
    triangles2 = VGroup(*[
      Polygon(triangles_coords2[0], corner_coords2[0], triangles_coords2[-1], stroke_width=0, fill_opacity=0.7).set_z_index(0),
      Polygon(triangles_coords2[0], middle_point, triangles_coords2[-1], stroke_width=0, fill_opacity=0.7).set_z_index(0),
      Polygon(triangles_coords2[1], corner_coords2[2], triangles_coords2[2], stroke_width=0, fill_opacity=0.7).set_z_index(0),
      Polygon(triangles_coords2[1], middle_point, triangles_coords2[2], stroke_width=0, fill_opacity=0.7).set_z_index(0)
    ])
    self.play(*[DrawBorderThenFill(i) for i in triangles1.copy()])

    self.play(Rotate(triangles1[1], PI/2), Rotate(triangles1[2], -PI/2))
    self.play(*[triangles1[i].animate.move_to(triangles2[i]) for i in range(4)])

    a_square = Polygon(*triangles_coords1, color=ORANGE, fill_opacity=0.6).set_z_index(2)
    b_square = Polygon(*[triangles_coords2[0], corner_coords2[1], triangles_coords2[1], middle_point], color=ORANGE, fill_opacity=0.6).set_z_index(2)
    c_square = Polygon(*[triangles_coords2[3], middle_point, triangles_coords2[2], corner_coords2[3]], color=ORANGE, fill_opacity=0.6).set_z_index(2)
    self.play(DrawBorderThenFill(a_square), DrawBorderThenFill(b_square), DrawBorderThenFill(c_square))

    a_square_text = MathTex(r"a^2").move_to(a_square.get_center())
    b_square_text = MathTex(r"b^2").move_to(b_square.get_center())
    c_square_text = MathTex(r"c^2").move_to(c_square.get_center())
    self.play(Write(a_square_text), Write(b_square_text), Write(c_square_text))

    variables = VGroup(a_square_text, b_square_text, c_square_text)
    equation = MathTex(r"{{a^2}}",r"=",r"{{b^2}}",r"+",r"{{c^2}}").to_edge(DOWN)

    self.play(Write(equation[1]), Write(equation[3]))
    self.play(*[in_square.copy().animate.move_to(in_equation) for in_square, in_equation in zip(variables,[equation[0], equation[2], equation[4]])])
    out_box = SurroundingRectangle(equation)
    self.play(Create(out_box))

    self.wait()
  
