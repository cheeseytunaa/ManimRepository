from manim import *

class Main(MovingCameraScene):
  def construct(self):
    # Save the first camera scene
    self.camera.frame.save_state()

    # Initialize the scene
    semi_circle = Arc(radius=3,angle=PI,color=BLUE,stroke_width=2).shift(DOWN)
    diameter = Line(
      semi_circle.point_from_proportion(0),
      semi_circle.point_from_proportion(1),
      color=BLUE,stroke_width=2
    )
    init_dots = VGroup(*[Dot(semi_circle.point_from_proportion(i),radius=0.04,color=YELLOW) for i in range(2)]).set_z_index(1)
    main = VGroup(semi_circle,diameter)
    self.play(
      *[Create(init_dots[i]) for i in range(2)],
      *[Create(main[i]) for i in range(2)]
    )
    
    # Define the variables and draw polygons and labels
    dot_1 = Dot(semi_circle.point_from_proportion(0.7),radius=0.04,color=YELLOW)
    dot_2 = always_redraw(lambda: Dot([dot_1.get_x(),diameter.get_y(),0],radius=0.04,color=YELLOW))
    main_dot = VGroup(dot_1,dot_2).set_z_index(1)
    height = always_redraw(lambda: Line(dot_1,dot_2,color=BLUE,stroke_width=2))
    self.play(*[Create(main_dot[i]) for i in range(2)], Create(height))
    triangle_1 = always_redraw(lambda: Polygon(
      dot_1.get_center(),
      init_dots[0].get_center(),
      dot_2.get_center(),
      fill_opacity=0.7,stroke_width=2
    ))
    triangle_2 = always_redraw(lambda: Polygon(
      dot_1.get_center(),
      init_dots[1].get_center(),
      dot_2.get_center(),
      fill_opacity=0.7,stroke_width=2
    ))
    right_angle = always_redraw(lambda: RightAngle(height,diameter,quadrant=(-1,1),length=0.2,stroke_width=2).set_z_index(-1))
    self.play(DrawBorderThenFill(triangle_1),DrawBorderThenFill(triangle_2),Create(right_angle))
    line_1 = always_redraw(lambda: Line(init_dots[1].get_center(),dot_2.get_center(),color=GREEN,stroke_width=2))
    line_2 = always_redraw(lambda: Line(init_dots[0].get_center(),dot_2.get_center(),color=RED,stroke_width=2))
    x_label = always_redraw(lambda: MathTex(r"x",color=GREEN).move_to(line_1).shift(DOWN * 0.3))
    y_label = always_redraw(lambda: MathTex(r"y",color=RED).move_to(line_2).shift(DOWN * 0.3))
    h_label = always_redraw(lambda: MathTex(r"h",color=YELLOW).next_to(height, RIGHT))
    self.play(
      Write(VGroup(x_label,y_label,h_label)),
      Create(VGroup(line_1,line_2))
    )

    self.wait()

    # Change camera angle
    self.play(self.camera.frame.animate.scale(1.5).move_to(LEFT*5))

    # Setup similar-equation
    temp_triangle_1 = triangle_1.copy()
    temp_triangle_2 = triangle_2.copy()
    temp_triangle_group = VGroup(triangle_1.copy(),triangle_2.copy()).arrange(DOWN, buff=3).move_to(LEFT*12)
    self.play(
      Transform(temp_triangle_1,temp_triangle_group[0]),
      Transform(temp_triangle_2,temp_triangle_group[1]),
    )
    temp_x_label = x_label.copy()
    temp_y_label = y_label.copy()
    temp_h_label_1 = h_label.copy()
    temp_h_label_2 = h_label.copy()
    self.play(
      temp_h_label_1.animate.next_to(temp_triangle_1,LEFT),
      temp_h_label_2.animate.next_to(temp_triangle_2,RIGHT),
      temp_x_label.animate.next_to(temp_triangle_2,DOWN),
      temp_y_label.animate.next_to(temp_triangle_1,DOWN)
    )

    # Note
    self.play(Write(Tex("*These two triangles are similar to each other!").move_to(LEFT*5*2+UP*5).set_color(YELLOW)))

    self.wait()

    # Finalize the equations
    eq1 = MathTex(r"\frac{h}{x}=\frac{y}{h}").move_to(LEFT*5*2.5)
    self.play(*[Write(eq1[0][i]) for i in [1,3,5]])
    self.play(
      *[before.animate.move_to(after) for before, after in zip([temp_h_label_1,temp_x_label,temp_y_label,temp_h_label_2],[eq1[0][0],eq1[0][2],eq1[0][4],eq1[0][6]])]
    )
    self.wait()
    eq2 = MathTex(r"h^{2}=x \times y").next_to(eq1,RIGHT,buff=1.5)
    self.play(*[Write(eq2[0][i]) for i in [1,2,4]])
    temp = [temp_h_label_1.copy(),temp_x_label.copy(),temp_y_label.copy(),temp_h_label_2.copy()]
    self.play(
      *[before.animate.move_to(after) for before, after in zip(temp,[eq2[0][0],eq2[0][3],eq2[0][5],eq2[0][0]])]
    )
    self.wait()
    eq3 = MathTex(r"h=\sqrt{x \times y}").next_to(eq2,RIGHT,buff=1.5)
    temp = [temp[0].copy(),eq2[0][2].copy(),temp[1].copy(),eq2[0][4].copy(),temp[2].copy()]
    self.play(
      *[before.animate.move_to(after) for before, after in zip(temp,[eq3[0][0],eq3[0][1],eq3[0][4],eq3[0][5],eq3[0][6]])],
      Transform(eq2[0][1].copy(),eq3[0][2]),
      Transform(eq2[0][1].copy(),eq3[0][3])
    )
    eq3 = MathTex(r"h",r"=",r"\sqrt{x \times y}").next_to(eq2,RIGHT,buff=1.5)
    eq3[0].set_color(YELLOW)
    eq3[2][2].set_color(GREEN)
    eq3[2][4].set_color(RED)
    self.add(eq3)
    self.wait()
    self.play(
      eq3.animate.next_to(main,DOWN,buff=1),
      self.camera.frame.animate.scale(1/1.5).move_to(RIGHT*4)
    )
    self.wait()
    center_dot_1 = Dot(semi_circle.point_from_proportion(1/2),radius=0.04,color=YELLOW)
    center_dot_2 = Dot(semi_circle.get_arc_center(),radius=0.04,color=YELLOW)
    center_line = Line(center_dot_1,center_dot_2,color=TEAL,stroke_width=2)
    r_label = MathTex(r"R",color=YELLOW).next_to(center_line, RIGHT)
    self.play(*[Create(i) for i in [center_dot_1,center_dot_2,center_line]],Write(r_label))
    self.wait()
    eq4 = MathTex(r"R",r"\geq",r"h").move_to(RIGHT*7+UP)
    self.play(Write(eq4[1]))
    temp = [r_label.copy(),h_label.copy()]
    self.play(
      *[before.animate.move_to(after) for before, after in zip(temp,[eq4[0],eq4[2]])]
    )
    self.wait()
    eq5 = MathTex(r"\frac{x+y}{2}\geq",r"\sqrt{x\times y}").next_to(eq4,DOWN)
    self.play(*[Write(eq5[0][i]) for i in [1,3,4,5]])
    temp = [x_label.copy(),y_label.copy()]
    self.play(
      *[before.animate.move_to(after) for before, after in zip(temp,[eq5[0][0],eq5[0][2]])],
      *[before.animate.move_to(after) for before, after in zip(eq3[2].copy(),eq5[1])]
    )

    # Make color :L
    self.play(Create(SurroundingRectangle(eq5,color=BLUE)))

    # Proofication
    value = ValueTracker(0.7)
    dot_1.add_updater(lambda d: d.move_to(semi_circle.point_from_proportion(value.get_value())))
    self.play(value.animate.set_value(0.01),run_time=2,rate_func=linear)
    self.play(value.animate.set_value(0.99),run_time=2,rate_func=linear)
    self.play(value.animate.set_value(0.7),run_time=2,rate_func=linear)

    self.wait()
