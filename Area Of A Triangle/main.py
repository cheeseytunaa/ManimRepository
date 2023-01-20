from typing import *
from manim import *


class LabelDot(Dot):
  def __init__(self, *args, **kwargs):
    super().__init__(
        radius=0.04,
        color=WHITE,
        *args,
        **kwargs
    )
    self.set_z_index(1)


class LabelTex(MathTex):
  def __init__(self, label: str, next_to_mobject: Mobject, direction, *args, **kwargs):
    super().__init__(
      label,
      *args,
      **kwargs
    )
    self.scale(0.7)
    buffer = 0.3 if (direction == UP).all() else 0.2 if (direction == DOWN + RIGHT).all() else 0.25
    self.move_to(next_to_mobject).shift(direction * buffer)


class Main(Scene):
  def construct(self):
    A, B, C = [-1, 1.5, 0], [-2.5, -1.5, 0], [2.5, -1.5, 0]
    triangle_ABC = Polygon(A, B, C)
    init_dots = [LabelDot(coordinations) for coordinations in [A, B, C]]
    init_labels = [
      LabelTex(label, point, direction) for label, point, direction in zip(
        ["A", "B", "C"],
        init_dots,
        [UP, DOWN + LEFT, DOWN + RIGHT]
      )
    ]

    H = [A[0], B[1], 0] # Perpendicular point
    dot_H = LabelDot(H)
    label_H = LabelTex("H", dot_H, DOWN)
    height = Line(A, H, color=BLUE)
    angle = RightAngle(Line(H, A), Line(B, C), length=0.2)

    self.play(*[Create(x) for x in [triangle_ABC, *init_dots, *init_labels]])
    self.wait()

    self.play(*[Create(x) for x in [dot_H, label_H, height, angle]])
    self.wait()
    
    triangle_ABH = Polygon(A, B, H, fill_color=RED, fill_opacity=0.4, stroke_width=0)
    triangle_ACH = Polygon(A, C, H, fill_color=GREEN, fill_opacity=0.4, stroke_width=0)

    self.play(*[Create(x) for x in [triangle_ABH, triangle_ACH]])
    self.wait()
    
    triangle_ABH_copy, triangle_ACH_copy = triangle_ABH.copy(), triangle_ACH.copy()
    self.play(
      FadeIn(triangle_ABH_copy),
      FadeIn(triangle_ACH_copy)
    )
    self.play( 
      Rotate(triangle_ABH_copy, PI),
      Rotate(triangle_ACH_copy, -PI)
    )
    self.wait()

    E, F = [B[0], A[1], 0], [C[0], A[1], 0]
    rectangle_EFCB = Polygon(E, F, C, B, color=YELLOW)
    dot_E, dot_F = LabelDot(E), LabelDot(F)
    label_E, label_F = LabelTex("E", dot_E, UP + LEFT), LabelTex("F", dot_F, UP + RIGHT)
    self.play(*[Create(x) for x in [
      dot_E,
      dot_F,
      label_E,
      label_F
    ]])
    self.wait()
    self.play(Create(rectangle_EFCB))

    formula = MathTex("S_{ABC}", "=", "\\frac{S_{EFCB}}{2}" ,"=", "\\frac{EF \\times EB}{2}", "=", "\\frac{AH \\times BC}{2}")
    formula.next_to(triangle_ABC, DOWN, 1.4).scale(0.7)

    formula_labels_copy = [
      init_labels,
      [label_E, label_F, init_labels[2], init_labels[1]],
      [label_E, label_F, label_E, init_labels[1]],
      [init_labels[0], label_H, init_labels[1], init_labels[2]]
    ]
    formula_labels_positioned = [
      [1, 2, 3],
      [1, 2, 3, 4],
      [0, 1, 3, 4],
      [0, 1, 3, 4]
    ]

    mobject_copies = []
    for index, sub_formula in enumerate(zip(formula_labels_copy, formula_labels_positioned)):
      general_pieces = []
      sub_formula_pieces = []
      for i in range(len(formula[index * 2])):
        if i not in sub_formula[1]:
          general_pieces.append(Write(formula[index * 2][i]))
      if index * 2 + 1 < len(formula):
        sub_formula_pieces.append(Write(formula[index * 2 + 1]))
      self.play(*general_pieces)

      for label, position in zip(*sub_formula):
        mobject_copy = label.copy()
        mobject_copies.append(mobject_copy)
        sub_formula_pieces.append(Transform(mobject_copy, formula[index * 2][position]))
      self.play(*sub_formula_pieces)
      self.wait()

    brace_height = Brace(Line(A, H), direction=RIGHT)
    brace_height_label = brace_height.get_text("Height")
    brace_base = Brace(Line(B, C))
    brace_base_label = brace_base.get_text("Base")
    self.play(*[Uncreate(x) for x in [label_E, label_F, dot_E, dot_F, *init_labels, label_H, triangle_ABH, triangle_ABH_copy, triangle_ACH, triangle_ACH_copy, rectangle_EFCB]])
    self.play(Transform(angle, RightAngle(Line(H, A), Line(B, C), quadrant=(1, -1), length=0.2)))
    self.play(*[Write(x) for x in [brace_base_label, brace_height_label, brace_base, brace_height]])
    self.wait()

    tex_label_h = MathTex("h").next_to(brace_height, RIGHT)
    tex_label_b = MathTex("b").next_to(brace_base, DOWN)
    self.play(
      Transform(brace_height_label, tex_label_h),
      Transform(brace_base_label, tex_label_b)
    )
    self.wait()

    final_formula = MathTex("S = \\frac{b \\times h}{2}").move_to(formula)
    self.play(Transform(VGroup(formula, *mobject_copies), final_formula))
    self.play(Circumscribe(final_formula))

    self.wait()


if __name__ == "__main__":
  import os
  cmd = f"manim {os.path.basename(__file__)} -pqh"
  try:
    __import__("subprocess").run(cmd)
  except ModuleNotFoundError:
    os.system(cmd)
