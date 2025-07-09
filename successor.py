import json

from manim import *

from vgroup_from_lambda_diagram import *


class Successor(Scene):
    def construct(self):
        # Define the successor function
        successor_step1 = MathTex(r"S = \lambda n.f \ n",
                                  substrings_to_isolate=["S = ", "\lambda n."])
        successor_step1.set_color_by_tex("S", BLUE)

        # Display the successor function
        self.play(Write(successor_step1[0]))
        self.wait()
        self.play(Write(successor_step1[1]))
        self.wait()

        example_before = MathTex(r"S \ (\lambda f.\lambda x.f \ (f \ x))").scale(0.5).shift(0.5 * DOWN)
        example_after = MathTex(r"\overset{\mathrm{\scriptscriptstyle \beta}}{=} \lambda f.\lambda x.f \ (f \ (f \ x))",
                                color=GRAY).scale(0.5).shift(0.8 * DOWN)

        self.play(Write(example_before))
        self.wait()
        self.play(ReplacementTransform(example_before.copy(), example_after))
        self.wait()

        self.play(Write(successor_step1[2::]))
        self.wait()

        successor_step2 = MathTex(r"S = \lambda n.\lambda f.f \ n",
                                  substrings_to_isolate=["S = ", "\lambda n.", "f \ n", "\lambda f."])
        successor_step2.set_color_by_tex("S", BLUE)

        self.play(TransformMatchingTex(successor_step1, successor_step2))
        self.wait()

        successor_step2_example = MathTex(r"\lambda f.f \ (\lambda f.\lambda x.f \ x)", color=RED,
                                          substrings_to_isolate=["S = ", "\lambda n.", "\lambda f.",
                                                                 "f \ x"]).set_color_by_tex(
            "S", BLUE).scale(0.5).shift(0.5 * UP)

        self.play(ReplacementTransform(successor_step2.copy(), successor_step2_example))
        self.wait()

        successor_step2_example_step2 = MathTex(r"\lambda f.\lambda x.f \ (f \ x)", color=GREEN,
                                                substrings_to_isolate=["\lambda f.", "f \ x"]).set_color_by_tex(
            "S", BLUE).scale(0.5).shift(0.5 * UP)
        self.play(TransformMatchingTex(successor_step2_example, successor_step2_example_step2))
        self.wait()

        successor_step3 = MathTex(r"S = \lambda n.\lambda f.\lambda x.f \ n",
                                  substrings_to_isolate=["S = ", "\lambda n.", "f \ n", "\lambda f.", "\lambda x."])
        successor_step3.set_color_by_tex("S", BLUE)

        self.play(TransformMatchingTex(successor_step2, successor_step3))
        self.wait()

        successor_final = MathTex(r"S = \lambda n.\lambda f.\lambda x.f \ (n \ f \ x)",
                                  substrings_to_isolate=["S = ", "\lambda n.", "\lambda f.", "\lambda x."]).scale(0.7)
        successor_final.set_color_by_tex("S", BLUE)

        successor_diagram = vgroup_from_lambda_diagram_file("successor.json").scale_to_fit_height(0.7).next_to(
            successor_final, DOWN)

        self.play(TransformMatchingTex(successor_step3, successor_final))
        self.wait()
        self.play(Unwrite(successor_step2_example_step2), Unwrite(example_after), Unwrite(example_before),
                  Create(successor_diagram))

        successor_example = MathTex(r"S \ (\lambda f.\lambda x.f \ (f \ x))", color=GREEN,
                                    substrings_to_isolate=["(\lambda f.\lambda x.f \ (f \ x))"]).scale(0.5).shift(
            0.5 * UP)

        successor_example_diagram_steps = []

        with open("successor_example_steps.json", "r") as file:
            data = json.load(file)
            for step in data:
                group = vgroup_from_lambda_diagram(step["Lines"])
                group.scale_to_fit_width(0.4).next_to(successor_example, UP)
                successor_example_diagram_steps.append(group)

        self.play(Write(successor_example), Create(successor_example_diagram_steps[0]))
        self.wait()
        self.play(TransformMatchingTex(successor_example,
                                       successor_example := MathTex(
                                           r"(\lambda n.\lambda f.\lambda x.f \ (n \ f \ x)) (\lambda f.\lambda x.f \ (f \ x))",
                                           substrings_to_isolate=["(\lambda f.\lambda x.f \ (f \ x))",
                                                                  "\lambda f.\lambda x.f \ (", " \ f \ x)"],
                                           color=GREEN).scale(0.5).shift(0.5 * UP)))
        self.wait()
        self.play(TransformMatchingTex(successor_example,
                                       successor_example := MathTex(
                                           r"\lambda f.\lambda x.f \ ((\lambda f.\lambda x.f \ (f \ x)) \ f \ x)",
                                           substrings_to_isolate=["(\lambda f.\lambda x.f \ (f \ x))",
                                                                  "\lambda f.\lambda x.f \ (", " \ f \ x)", "x)"],
                                           color=GREEN).scale(0.5).shift(0.5 * UP)),
                  ReplacementTransform(successor_example_diagram_steps[0], successor_example_diagram_steps[1]))
        self.wait()
        self.play(TransformMatchingTex(successor_example,
                                       successor_example := MathTex(
                                           r"\lambda f.\lambda x.f \ ((\lambda x.f \ (f \ x)) \ x)",
                                           substrings_to_isolate=["(\lambda f.\lambda x.f \ (f \ x))",
                                                                  "\lambda f.\lambda x.f \ (", "x)", "f \ (f \ x)"],
                                           color=GREEN).scale(0.5).shift(0.5 * UP)),
                  ReplacementTransform(successor_example_diagram_steps[1], successor_example_diagram_steps[2]))
        self.wait()
        self.play(TransformMatchingTex(successor_example,
                                       successor_example := MathTex(
                                           r"\lambda f.\lambda x.f \ (f \ (f \ x))",
                                           substrings_to_isolate=["\lambda f.\lambda x.f \ (", "x)", "f \ (f \ x)"],
                                           color=GREEN).scale(0.5).shift(0.5 * UP)),
                  ReplacementTransform(successor_example_diagram_steps[2], successor_example_diagram_steps[3]))
        self.wait()

        # Clear the scene
        self.play(successor_final.animate.shift(UP).scale(0.5), Unwrite(successor_example, run_time=0.5),
                  Uncreate(successor_example_diagram_steps[3]), Uncreate(successor_diagram))
