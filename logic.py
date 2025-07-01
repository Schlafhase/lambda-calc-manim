from manim import *

class Logic(MovingCameraScene):
    def construct(self):
        curry = MathTex(r"\lambda a.\lambda b.a \ b", substrings_to_isolate=["\lambda a.", "\lambda b.a \ b"])
        
        self.play(Write(curry[0]))
        self.wait()
        self.play(Write(curry[1]))
        self.wait()        
        
        self.play(Unwrite(curry))
        
        true_lambda = MathTex(r"\lambda a.\lambda b.a", color=GREEN, substrings_to_isolate=["\lambda a.", "\lambda b.a"]).move_to(ORIGIN + 0.5*UP)
        false_lambda = MathTex(r"\lambda a.\lambda b.b", color=RED).move_to(ORIGIN + 0.5*DOWN)
        
        self.play(Write(true_lambda), Write(false_lambda))
        self.wait()
        
        true_example = MathTex(r"(\lambda a.\lambda b.a) x \ y", substrings_to_isolate=["\lambda a.", "\lambda b.a", "x", "y", "(", ")"]).move_to(ORIGIN + 0.5*UP)
        
        self.play(TransformMatchingTex(true_lambda, true_example))
        self.wait()
        self.play(TransformMatchingTex(true_example, 
                                       true_step1 := MathTex(r"((\lambda a.\lambda b.a) x ) y", substrings_to_isolate=["\lambda a.", "\lambda b.a", "x", "y", "(", ")"])
                                       .move_to(ORIGIN + 0.5*UP)))
        self.wait()
        self.play(TransformMatchingTex(true_step1,
                                       true_step2 := MathTex(r"(\lambda b.x) y", substrings_to_isolate=["\lambda b.a", "x", "y", "(", ")"])
                                       .move_to(ORIGIN + 0.5*UP)))
        self.wait()
        self.play(TransformMatchingTex(true_step2,
                                       MathTex(r"x").move_to(ORIGIN + 0.5*UP)))
        self.wait()