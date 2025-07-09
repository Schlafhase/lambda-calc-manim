from manim import *

from vgroup_from_lambda_diagram import vgroup_from_lambda_diagram_file


class ChurchNumerals(MovingCameraScene):
    def construct(self):
        # Define the Church numeral for zero
        zero = MathTex(r"0 = \lambda f.\lambda x.x",
                       substrings_to_isolate=["0 = ", "\lambda f.\lambda x.", "x", r"f \ "])
        zero.set_color_by_tex("0", BLUE)
        
        zero_diagram = vgroup_from_lambda_diagram_file("0.json").scale_to_fit_height(0.7).next_to(zero, UP)

        # Display the numeral
        self.play(Write(zero[0]))
        self.wait()
        self.play(Write(zero[1::]), Create(zero_diagram))
        self.wait()

        # Define the Church numeral for one
        one = MathTex(r"1 = \lambda f.\lambda x.f \ x", substrings_to_isolate=["1 = ", "\lambda f.\lambda x.", "x", r"f \ "])
        one.set_color_by_tex("1", BLUE)
        
        one_diagram = vgroup_from_lambda_diagram_file("1.json").scale_to_fit_height(0.7).next_to(one, UP)

        # Display the numeral
        self.play(TransformMatchingTex(zero, one), ReplacementTransform(zero_diagram, one_diagram))
        self.wait()

        # Define the Church numeral for two
        two = MathTex(r"2 = \lambda f.\lambda x.f \ (f \ x)", substrings_to_isolate=["2 = ", "\lambda f.\lambda x.", "x", r"f \ "])
        two.set_color_by_tex("2", BLUE)

        two_diagram = vgroup_from_lambda_diagram_file("2.json").scale_to_fit_height(0.7).next_to(two, UP)

        # Display the numeral
        self.play(TransformMatchingTex(one, two), ReplacementTransform(one_diagram, two_diagram))
        self.wait()

        # Define the Church numeral for three
        three = MathTex(r"3 = \lambda f.\lambda x.f \ (f \ (f \ x))", substrings_to_isolate=["3 = ", "\lambda f.\lambda x.", "x", r"f \ "]).scale(0.7)
        three.set_color_by_tex("3", BLUE)
        
        three_diagram = vgroup_from_lambda_diagram_file("3.json").scale_to_fit_height(0.7).next_to(three, UP)

        # Display the numeral
        self.play(TransformMatchingTex(two, three), ReplacementTransform(two_diagram, three_diagram))
        self.wait()

        # Clear the scene
        self.play(Unwrite(three), Uncreate(three_diagram))