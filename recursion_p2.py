from manim import *


class Factorial(Scene):
    def construct(self):
        theta_applied = MathTex(r"\Theta \ F = F \ (\Theta \ F)",
                                substrings_to_isolate=[r"=", "F", "\Theta"])
        theta_applied.set_color_by_tex(r"\Theta", BLUE)
        theta_applied.set_color_by_tex(r"=", BLUE)
        theta_applied.set_color_by_tex("F", ORANGE)

        theta_applied.move_to(ORIGIN).shift(3 * UP).scale(0.7)
        self.add(theta_applied)

        fac_tex = MathTex(r"fac = \lambda n.(\text{IST\_0} \ n) \ &1 \\ &(* \ n \ (fac \ (pred \ n)))",
                          substrings_to_isolate=["fac = ", "fac", r"\text{IST\_0}", "*", "pred", "1", "n",
                                                 "\lambda n.", "(", ")"]).shift(LEFT)
        fac_tex.set_color_by_tex("fac", RED)
        fac_tex.set_color_by_tex("fac = ", BLUE)
        fac_tex.set_color_by_tex(r"IST\_0", BLUE)
        fac_tex.set_color_by_tex("*", BLUE)
        fac_tex.set_color_by_tex("pred", BLUE)
        fac_tex.set_color_by_tex("1", BLUE)

        fac_tex_no_recurs = MathTex(
            r"fac = \lambda f.\lambda n.(\text{IST\_0} \ n) \ &1 \\ &(* \ n \ (f \ (pred \ n)))",
            substrings_to_isolate=["fac = ", r"\text{IST\_0}", "*", "pred", "1", "n", "\lambda n.", "\lambda f.", "(",
                                   ")"]).shift(LEFT)
        fac_tex_no_recurs.set_color_by_tex("fac = ", BLUE)
        fac_tex_no_recurs.set_color_by_tex(r"IST\_0", BLUE)
        fac_tex_no_recurs.set_color_by_tex("*", BLUE)
        fac_tex_no_recurs.set_color_by_tex("pred", BLUE)
        fac_tex_no_recurs.set_color_by_tex("1", BLUE)

        self.play(Write(fac_tex))
        self.wait()
        self.play(TransformMatchingTex(fac_tex, fac_tex_no_recurs))
        self.wait()

        theta_fac = (MathTex(r"\Theta \ fac = fac \ (\Theta \ fac)",
                             substrings_to_isolate=["\Theta \ fac = ", "fac", "\Theta", "(", ")"])
                     .next_to(fac_tex_no_recurs, DOWN, buff=0.5).align_to(fac_tex_no_recurs, LEFT))
        theta_fac.set_color_by_tex("fac", BLUE)
        theta_fac.set_color_by_tex("\Theta", BLUE)
        self.play(Write(theta_fac))
        self.wait()

        theta_fac_expanded = (MathTex(
            r"\Theta \ fac = (\lambda f.\lambda n.(\text{IST\_0} \ n) \ &1 \\ &(* \ n \ (f \ (pred \ n)))) (\Theta \ fac)",
            substrings_to_isolate=["\Theta \ fac = ", "fac", "\Theta", "(", ")", "(\Theta \ fac)", "*"])
                              .align_to(theta_fac, UP).align_to(theta_fac, LEFT))
        theta_fac_expanded.set_color_by_tex("fac", BLUE)
        theta_fac_expanded.set_color_by_tex("\Theta", BLUE)
        theta_fac_expanded.set_color_by_tex(r"IST\_0", BLUE)
        theta_fac_expanded.set_color_by_tex("*", BLUE)
        theta_fac_expanded.set_color_by_tex("pred", BLUE)
        theta_fac_expanded.set_color_by_tex("1", BLUE)

        self.play(TransformMatchingTex(theta_fac, theta_fac_expanded))
        self.wait()

        theta_fac_expanded_reduced = (MathTex(
            r"\Theta \ fac = \lambda n.(\text{IST\_0} \ n) \ &1 \\ &(* \ n \ ((\Theta \ fac) \ (pred \ n)))",
            substrings_to_isolate=["\Theta \ fac = ", "fac", "\Theta", "(", ")", "(\Theta \ fac)", "n"])
                                      .align_to(theta_fac, UP).align_to(theta_fac, LEFT))
        theta_fac_expanded_reduced.set_color_by_tex("fac", BLUE)
        theta_fac_expanded_reduced.set_color_by_tex("\Theta", BLUE)
        theta_fac_expanded_reduced.set_color_by_tex(r"IST\_0", BLUE)
        theta_fac_expanded_reduced.set_color_by_tex("*", BLUE)
        theta_fac_expanded_reduced.set_color_by_tex("pred", BLUE)
        theta_fac_expanded_reduced.set_color_by_tex("1", BLUE)

        theta_fac_hidden = (MathTex(
            r"\Theta \ fac = \lambda n.(\text{IST\_0} \ n) \ &1 \\ &(* \ n \ ((\Theta \ fac) \ (pred \ n)))",
            substrings_to_isolate=["\Theta \ fac"])
                            .align_to(theta_fac, UP).align_to(theta_fac, LEFT))

        self.play(TransformMatchingTex(theta_fac_expanded, theta_fac_expanded_reduced))
        self.wait()

        bounding_box_1 = SurroundingRectangle(theta_fac_hidden[0])
        bounding_box_2 = SurroundingRectangle(theta_fac_hidden[2])
        self.play(Create(bounding_box_1), Create(bounding_box_2))
        self.wait()
