from manim import *

class DefaultTemplate(MovingCameraScene):
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
        
        self.play(Write(equation_lambda), Write(lambda_brace))
        self.wait(1)
        
        self.play(Create(abstraction_box), Write(abstraction_label), Transform(equation_lambda[1:3].copy(), equation[1:3]), Write(math_brace, run_time=1))
        self.wait(1)
        self.play(Transform(abstraction_box, body_box), Write(body_label), Transform(equation_lambda[3].copy(), equation[3]))
        self.wait(1)
        self.play(Transform(abstraction_box, application_box), Write(application_label), Transform(equation_lambda[4::].copy(), equation[4::]))
