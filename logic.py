from manim import *
from vgroup_from_lambda_diagram import *


class Logic(MovingCameraScene):
    def construct(self):
        curry = MathTex(r"\lambda a.\lambda b.a \ b", substrings_to_isolate=["\lambda a.", "\lambda b.a \ b"])
        currying_text = Text("Currying", color=BLUE).next_to(curry, UP, buff=0.3)

        self.play(Write(curry[0]))
        self.wait()
        self.play(Write(curry[1]))
        self.wait()
        self.play(Write(currying_text))
        self.wait()

        self.play(Unwrite(curry), Unwrite(currying_text))

        true_lambda = MathTex(r"T = \lambda a.\lambda b.a", color=GREEN,
                              substrings_to_isolate=["\lambda a.", "\lambda b.a"]).move_to(ORIGIN + 0.5 * UP)
        true_diagram =vgroup_from_lambda_diagram_file("true.json").scale_to_fit_width(0.4).next_to(true_lambda, LEFT)
        
        false_lambda = MathTex(r"F = \lambda a.\lambda b.b", color=RED).move_to(ORIGIN + 0.5 * DOWN)
        false_diagram = vgroup_from_lambda_diagram_file("false.json").scale_to_fit_width(0.4).next_to(false_lambda, LEFT)

        self.play(Write(true_lambda), Write(false_lambda), Create(true_diagram), Create(false_diagram))
        self.wait()

        true_example = MathTex(r"(\lambda a.\lambda b.a) x \ y",
                               substrings_to_isolate=["\lambda a.", "\lambda b.a", "x", "y", "(", ")"]).move_to(
            ORIGIN + 0.5 * UP)
        
        true_example_diagrams = []
        with open("true_example_steps.json", "r") as file:
            data = json.load(file)
            for step in data:
                group = vgroup_from_lambda_diagram(step["Lines"]).move_to(true_diagram)
                group.scale_to_fit_width(0.4)
                true_example_diagrams.append(group)

        self.play(TransformMatchingTex(true_lambda, true_example), Transform(true_diagram, true_example_diagrams[0]))
        self.wait()
        self.play(TransformMatchingTex(true_example,
                                       true_step1 := MathTex(r"((\lambda a.\lambda b.a) x ) y",
                                                             substrings_to_isolate=["\lambda a.", "\lambda b.a", "x",
                                                                                    "y", "(", ")"])
                                       .move_to(ORIGIN + 0.5 * UP)))
        self.wait()
        self.play(TransformMatchingTex(true_step1,
                                       true_step2 := MathTex(r"(\lambda b.x) y",
                                                             substrings_to_isolate=["\lambda b.a", "x", "y", "(", ")"])
                                       .move_to(ORIGIN + 0.5 * UP)),
                  Transform(true_diagram, true_example_diagrams[1]))
        self.wait()
        self.play(TransformMatchingTex(true_step2,
                                       true_step3 := MathTex(r"x").move_to(ORIGIN + 0.5 * UP)),
                  Transform(true_diagram, true_example_diagrams[2]))
        self.wait()

        self.play(ReplacementTransform(true_step3, true_lambda.move_to(ORIGIN + 0.8 * DOWN).scale(0.5)),
                  false_lambda.animate.move_to(ORIGIN + 1 * DOWN).scale(0.5), Uncreate(true_diagram), Uncreate(false_diagram))

        not_lambda = (
            MathTex(r"NOT = \lambda x.x \ F \ T", substrings_to_isolate=["NOT = ", "\lambda x.x", " \ F", " \ T"]))
        not_lambda.set_color_by_tex(" \ T", GREEN)
        not_lambda.set_color_by_tex(" \ F", RED)
        
        not_diagram = vgroup_from_lambda_diagram_file("not.json").scale_to_fit_height(0.7).next_to(not_lambda, UP)

        self.play(Write(not_lambda[0]))
        self.wait()
        self.play(Write(not_lambda[1]))
        self.wait()
        self.play(Write(not_lambda[2]))
        self.wait()
        self.play(Write(not_lambda[3]))
        self.wait()

        not_lambda_full = (MathTex(r"NOT = \lambda x.x \ (\lambda a.\lambda b.b) \ (\lambda a.\lambda b.a)",
                                   substrings_to_isolate=["NOT = ", "\lambda x.x", "\lambda a.\lambda b.b",
                                                          "\lambda a.\lambda b.a"]))
        not_lambda_full.set_color_by_tex("\lambda a.\lambda b.a", GREEN)
        not_lambda_full.set_color_by_tex("\lambda a.\lambda b.b", RED)

        true_cp = MathTex(r"\lambda a.\lambda b.a", color=GREEN,
                          substrings_to_isolate=["\lambda a.\lambda b.a"]).move_to(
            ORIGIN + 0.8 * DOWN).scale(0.5).align_to(true_lambda, RIGHT)
        false_cp = MathTex(r"\lambda a.\lambda b.b", color=RED,
                           substrings_to_isolate=["\lambda a.\lambda b.b"]).move_to(
            ORIGIN + 1 * DOWN).scale(0.5).align_to(false_lambda, RIGHT)

        self.play(TransformMatchingTex(VGroup(not_lambda,
                                              true_cp,
                                              false_cp),
                                       not_lambda_full.scale(0.5)), Create(not_diagram))
        self.wait()

        self.play(Unwrite(not_lambda_full), Unwrite(true_lambda), Unwrite(false_lambda), Uncreate(not_diagram))

        and_lambda = MathTex(r"AND = \lambda p.\lambda q.p \ q \ F",
                             substrings_to_isolate=["AND = ", "\lambda p.\lambda q.", "p \ ", "q", " \ F"]).scale(0.5)
        and_lambda.set_color_by_tex("AND = ", BLUE)
        and_lambda.set_color_by_tex("F", RED)
        
        and_diagram = vgroup_from_lambda_diagram_file("and.json").scale_to_fit_height(0.7).next_to(and_lambda, UP)

        self.play(Write(and_lambda[0]))
        self.wait()
        self.play(Write(and_lambda[1]))
        self.wait()
        self.play(Write(and_lambda[2]))
        self.wait()
        self.play(Write(and_lambda[3]))
        self.wait()
        self.play(Write(and_lambda[4]), Create(and_diagram))
        self.wait()

        or_lambda = MathTex(r"OR = \lambda p.\lambda q.p \ T \ q",
                            substrings_to_isolate=["OR = ", "\lambda p.\lambda q.", "p \ ", "T \ ", "q"]).scale(0.5)
        or_lambda.set_color_by_tex("OR = ", BLUE)
        or_lambda.set_color_by_tex("T", GREEN)
        
        or_diagram = vgroup_from_lambda_diagram_file("or.json").scale_to_fit_height(0.7).next_to(or_lambda, UP)

        self.play(TransformMatchingTex(and_lambda, or_lambda), ReplacementTransform(and_diagram, or_diagram))
        self.wait()

        xor_lambda = MathTex(r"XOR = \lambda p.\lambda q.p \ (NOT \ q) \ q",
                             substrings_to_isolate=["XOR = ", "\lambda p.\lambda q.", "p \ ", "NOT", "q"]).scale(0.5)
        xor_lambda.set_color_by_tex("XOR = ", BLUE)
        xor_lambda.set_color_by_tex("NOT", BLUE)
        
        xor_diagram = vgroup_from_lambda_diagram_file("xor.json").scale_to_fit_height(0.7).next_to(xor_lambda, UP)

        xor_lambda_full = MathTex(
            r"XOR = \lambda p.\lambda q.p \ ((\lambda x.x \ (\lambda a.\lambda b.b) \ (\lambda a.\lambda b.a)) \ q) \ q",
            substrings_to_isolate=["XOR = ", "(lambda x.x \ (\lambda a.\lambda b.b) \ (\lambda a.\lambda b.a))", "\lambda p.\lambda q.", "p \ ", "q"]).scale(0.4)
        xor_lambda_full.set_color_by_tex("XOR = ", BLUE)

        self.play(TransformMatchingTex(or_lambda, xor_lambda), ReplacementTransform(or_diagram, xor_diagram))
        self.wait()
        self.play(TransformMatchingTex(xor_lambda, xor_lambda_full))
        self.wait()
        self.play(Unwrite(xor_lambda_full), Uncreate(xor_diagram))