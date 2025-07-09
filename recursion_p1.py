from manim import *


class RecursionIntro(Scene):
    def construct(self):
        fac_tex = MathTex(r"fac = \lambda n.(\text{IST\_0} \ n) \ &1 \\ &(* \ n \ (fac \ (pred \ n)))",
                          substrings_to_isolate=["fac = ", "fac", r"\text{IST\_0}", "*", "pred", "1"])
        fac_tex.set_color_by_tex("fac", RED)
        fac_tex.set_color_by_tex("fac = ", BLUE)
        fac_tex.set_color_by_tex("IST_0", BLUE)
        fac_tex.set_color_by_tex("*", BLUE)
        fac_tex.set_color_by_tex("pred", BLUE)
        fac_tex.set_color_by_tex("1", BLUE)
        
        self.play(Write(fac_tex))
        self.wait()
        self.play(Unwrite(fac_tex))
        