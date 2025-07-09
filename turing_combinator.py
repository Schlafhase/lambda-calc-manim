from manim import *


class TuringCombinator(Scene):
    def construct(self):
        u_tex = MathTex(r"U = \lambda x.\lambda f.f \ ((x \ x) \ f)", substrings_to_isolate=["U = "]).shift(UP)
        u_tex.set_color_by_tex("U", BLUE)

        theta_tex = (MathTex(r"\Theta = U \ U", substrings_to_isolate=[r"\Theta = ", " \ U"])
                     .next_to(u_tex, DOWN).align_to(u_tex, LEFT))
        theta_tex.set_color_by_tex(r"\Theta", BLUE)
        theta_tex.set_color_by_tex("U", BLUE)

        self.play(Write(u_tex))
        self.wait()
        self.play(Write(theta_tex))
        self.wait()

        theta_expanded = (MathTex(r"\Theta = (\lambda x.\lambda f.f \ (x \ x \ f)) \ U",
                                  substrings_to_isolate=[r"\Theta = ", "U", "\lambda f.f \ (", " \ f)"])
                          .next_to(theta_tex, DOWN).align_to(theta_tex, LEFT))
        theta_expanded.set_color_by_tex(r"\Theta", BLUE)
        theta_expanded.set_color_by_tex("U", BLUE)

        self.play(TransformMatchingTex(theta_tex.copy(), theta_expanded))
        self.wait()

        theta_expanded_2 = (MathTex(r"\Theta = \lambda f.f \ (U \ U \ f)",
                                    substrings_to_isolate=[r"\Theta = ", "\lambda f.f \ (", " \ f)", "U"])
                            .move_to(theta_expanded).align_to(theta_expanded, LEFT))
        theta_expanded_2.set_color_by_tex(r"\Theta", BLUE)
        theta_expanded_2.set_color_by_tex("U", BLUE)

        self.play(TransformMatchingTex(theta_expanded, theta_expanded_2))
        self.wait()

        theta_expanded_3 = (MathTex(r"\Theta = \lambda f.f \ (\Theta \ f)",
                                    substrings_to_isolate=[r"\Theta = ", "\lambda f.f \ (", " \ f)"])
                            .move_to(theta_expanded_2).align_to(theta_expanded_2, LEFT))
        theta_expanded_3.set_color_by_tex(r"\Theta", BLUE)
        theta_expanded_3.set_color_by_tex("U", BLUE)

        self.play(TransformMatchingTex(theta_expanded_2, theta_expanded_3))
        self.wait()

        theta_applied = (MathTex(r"\Theta \ F = F \ (\Theta \ F)",
                                 substrings_to_isolate=[r"=", "F", "\Theta"])
                         .next_to(theta_expanded_3, DOWN, buff=0.5).align_to(theta_expanded_3, LEFT))
        theta_applied.set_color_by_tex(r"\Theta", BLUE)
        theta_applied.set_color_by_tex(r"=", BLUE)
        theta_applied.set_color_by_tex("F", ORANGE)
        
        self.play(Write(theta_applied))
        self.wait()
        self.play(theta_applied.animate.move_to(ORIGIN).shift(3 * UP).scale(0.7),
                  Unwrite(theta_expanded_3), Unwrite(u_tex), Unwrite(theta_tex))