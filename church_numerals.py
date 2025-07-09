from manim import *


class ChurchNumerals(MovingCameraScene):
    def construct(self):
        # Define the Church numeral for zero
        zero = MathTex(r"0 = \lambda f.\lambda x.x",
                       substrings_to_isolate=["0 = ", "\lambda f.\lambda x.", "x", r"f \ "])
        zero.set_color_by_tex("0", BLUE)

        # Display the numeral
        self.play(Write(zero[0]))
        self.wait()
        self.play(Write(zero[1::]))
        self.wait()

        # Define the Church numeral for one
        one = MathTex(r"1 = \lambda f.\lambda x.f \ x", substrings_to_isolate=["1 = ", "\lambda f.\lambda x.", "x", r"f \ "])
        one.set_color_by_tex("1", BLUE)

        # Display the numeral
        self.play(TransformMatchingTex(zero, one))
        self.wait()

        # Define the Church numeral for two
        two = MathTex(r"2 = \lambda f.\lambda x.f \ (f \ x)", substrings_to_isolate=["2 = ", "\lambda f.\lambda x.", "x", r"f \ "])
        two.set_color_by_tex("2", BLUE)

        # Display the numeral
        self.play(TransformMatchingTex(one, two))
        self.wait()

        # Define the Church numeral for three
        three = MathTex(r"3 = \lambda f.\lambda x.f \ (f \ (f \ x))", substrings_to_isolate=["3 = ", "\lambda f.\lambda x.", "x", r"f \ "]).scale(0.7)
        three.set_color_by_tex("3", BLUE)

        # Display the numeral
        self.play(TransformMatchingTex(two, three))
        self.wait()

        # Clear the scene
        self.play(Unwrite(three))