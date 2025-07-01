from manim import *

class Conversions(MovingCameraScene):
    def construct(self):
        self.camera.frame.set_width(10)
        # Create the equation
        equation_lambda = MathTex(r"(\lambda x.x)y",
                                  substrings_to_isolate=["\lambda x", "x", "y"])
        equation = MathTex(r"\\ & f(x) \mapsto x \\ & f(y)",
                           substrings_to_isolate=["f(x)", "x", "f(y)"])


        equation_lambda.set_color_by_tex("x", RED)
        equation_lambda.set_color_by_tex("\lambda x", BLUE)
        equation_lambda.set_color_by_tex("y", GREEN)

        equation.set_color_by_tex("x", RED)
        equation.set_color_by_tex("f(x)", BLUE)
        equation.set_color_by_tex("f(y)", GREEN)

        abstraction_label = MathTex(r"\text{Abstraktion}", color=BLUE).next_to(equation_lambda, 8*UP)
        body_label = MathTex(r"\text{Funktionswert}", color=RED).next_to(abstraction_label, DOWN)
        application_label = MathTex(r"\text{Applikation}", color=GREEN).next_to(body_label, DOWN)

        labels = VGroup(abstraction_label, body_label, application_label).arrange(DOWN, aligned_edge=LEFT)
        equations = VGroup(equation_lambda, equation).arrange(DOWN, aligned_edge=LEFT)
        group = VGroup(labels, equations).arrange(DOWN, aligned_edge=LEFT, buff=1.5).move_to(3*RIGHT)

        abstraction_box = SurroundingRectangle(equation_lambda[1:3])
        body_box = SurroundingRectangle(equation_lambda[3])
        application_box = SurroundingRectangle(equation_lambda)

        lambda_brace = BraceLabel(equation_lambda, r"\text{Lambda Kalkül}", LEFT)
        math_brace = BraceLabel(equation, r"\text{Mathematische Notation}", LEFT)

        self.add(equations, labels, application_box, lambda_brace, math_brace)
        
        self.play(Unwrite(equation), Unwrite(math_brace), Unwrite(labels), Uncreate(application_box), Unwrite(lambda_brace), Unwrite(math_brace),
                  equation_lambda.animate.move_to(ORIGIN).scale(2), run_time=1)
        
        self.wait()
        
        lambda_y = MathTex(r"y", color=GREEN).move_to(ORIGIN).scale(2)
        
        self.play(TransformMatchingTex(equation_lambda, lambda_y))
        self.wait()
        
        lambda_example1 = MathTex(r"(\lambda x.x)(\lambda y.y)", substrings_to_isolate=["(\lambda y.y)"]).move_to(ORIGIN).scale(2)
        
        self.play(ReplacementTransform(lambda_y, lambda_example1))
        self.wait()
        
        lambda_example1_solution = MathTex(r"(\lambda y.y)").move_to(ORIGIN).scale(2)
        
        self.play(TransformMatchingTex(lambda_example1, lambda_example1_solution))
        self.wait()
        
        lambda_example2 = MathTex(r"(\lambda x.(x (y \ x))(f \ f)", substrings_to_isolate=["(f \ f)"]).move_to(ORIGIN).scale(2)
        
        self.play(ReplacementTransform(lambda_example1_solution, lambda_example2))
        self.wait()
        
        lambda_example2_solution = MathTex(r"(f \ f) (y (f \ f)", substrings_to_isolate=["(f \ f)"]).move_to(ORIGIN).scale(2)
        
        self.play(TransformMatchingTex(lambda_example2, lambda_example2_solution))
        self.wait()
        self.play(Unwrite(lambda_example2_solution))