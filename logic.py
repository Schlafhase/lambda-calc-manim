from manim import *


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
        false_lambda = MathTex(r"F = \lambda a.\lambda b.b", color=RED).move_to(ORIGIN + 0.5 * DOWN)

        self.play(Write(true_lambda), Write(false_lambda))
        self.wait()

        true_example = MathTex(r"(\lambda a.\lambda b.a) x \ y",
                               substrings_to_isolate=["\lambda a.", "\lambda b.a", "x", "y", "(", ")"]).move_to(
            ORIGIN + 0.5 * UP)

        self.play(TransformMatchingTex(true_lambda, true_example))
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
                                       .move_to(ORIGIN + 0.5 * UP)))
        self.wait()
        self.play(TransformMatchingTex(true_step2,
                                       true_step3 := MathTex(r"x").move_to(ORIGIN + 0.5 * UP)))
        self.wait()

        self.play(ReplacementTransform(true_step3, true_lambda.move_to(ORIGIN + 0.8 * DOWN).scale(0.5)),
                  false_lambda.animate.move_to(ORIGIN + 1 * DOWN).scale(0.5))

        not_lambda = (
            MathTex(r"NOT = \lambda x.x \ F \ T", substrings_to_isolate=["NOT = ", "\lambda x.x", " \ F", " \ T"]))
        not_lambda.set_color_by_tex(" \ T", GREEN)
        not_lambda.set_color_by_tex(" \ F", RED)

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
                                       not_lambda_full.scale(0.5)))
        self.wait()

        self.play(Unwrite(not_lambda_full), Unwrite(true_lambda), Unwrite(false_lambda))

        and_lambda = MathTex(r"AND = \lambda p.\lambda q.p \ q \ F",
                             substrings_to_isolate=["AND = ", "\lambda p.\lambda q.", "p \ ", "q", " \ F"]).scale(0.5)
        and_lambda.set_color_by_tex("AND = ", BLUE)
        and_lambda.set_color_by_tex("F", RED)

        self.play(Write(and_lambda[0]))
        self.wait()
        self.play(Write(and_lambda[1]))
        self.wait()
        self.play(Write(and_lambda[2]))
        self.wait()
        self.play(Write(and_lambda[3]))
        self.wait()
        self.play(Write(and_lambda[4]))
        self.wait()

        or_lambda = MathTex(r"OR = \lambda p.\lambda q.p \ T \ q",
                            substrings_to_isolate=["OR = ", "\lambda p.\lambda q.", "p \ ", "T \ ", "q"]).scale(0.5)
        or_lambda.set_color_by_tex("OR = ", BLUE)
        or_lambda.set_color_by_tex("T", GREEN)

        self.play(TransformMatchingTex(and_lambda, or_lambda))
        self.wait()

        xor_lambda = MathTex(r"XOR = \lambda p.\lambda q.p \ (NOT \ q) \ q",
                             substrings_to_isolate=["XOR = ", "\lambda p.\lambda q.", "p \ ", "NOT", "q"]).scale(0.5)
        xor_lambda.set_color_by_tex("XOR = ", BLUE)
        xor_lambda.set_color_by_tex("NOT", BLUE)

        xor_lambda_full = MathTex(
            r"XOR = \lambda p.\lambda q.p \ ((\lambda x.x \ (\lambda a.\lambda b.b) \ (\lambda a.\lambda b.a)) \ q) \ q",
            substrings_to_isolate=["XOR = ", "(lambda x.x \ (\lambda a.\lambda b.b) \ (\lambda a.\lambda b.a))", "\lambda p.\lambda q.", "p \ ", "q"]).scale(0.4)
        xor_lambda_full.set_color_by_tex("XOR = ", BLUE)

        self.play(TransformMatchingTex(or_lambda, xor_lambda))
        self.wait()
        self.play(TransformMatchingTex(xor_lambda, xor_lambda_full))
        self.wait()
        self.play(Unwrite(xor_lambda_full))