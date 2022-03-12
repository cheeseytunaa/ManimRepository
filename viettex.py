# This file was forked and modified by Chifuyu#3652
# It will help you to use Vietnamese (UTF-8 Unicode Characters) TaLeX in Manim (Community Edition) easily!

# Dependencies: Manim (Community Edition), LaTeX UTF-8 Package (Vietnamese)

from manim import *

class VietTex(MathTex):
  VietnameseTemplate = TexTemplate()
  VietnameseTemplate.add_to_preamble(r"\usepackage[utf8]{inputenc}")
  VietnameseTemplate.add_to_preamble(r"\usepackage[utf8]{vietnam}")

  def __init__(
    self,
    *tex_strings,
    arg_separator="",
    tex_environment="center",
    tex_template=VietnameseTemplate,
    **kwargs
  ):
    super().__init__(
      *tex_strings,
      arg_separator=arg_separator,
      tex_environment=tex_environment,
      tex_template=tex_template,
      **kwargs,
    )