import json
from manim import *
from vgroup_from_lambda_diagram import vgroup_from_lambda_diagram

class Addition(Scene):
    def construct(self):
        successor_final = MathTex(r"S = \lambda n.\lambda f.\lambda x.f \ (n \ f \ x)",
                                  substrings_to_isolate=["S = ", "\lambda n.", "\lambda f.", "\lambda x."]).scale(0.35).shift(UP)
        successor_final.set_color_by_tex("S", BLUE)
        
        self.add(successor_final)
        self.wait()
        
        addition = MathTex(r"+ = \lambda m.\lambda n.m \ S \ n)",
                           substrings_to_isolate=["+ = ", r"\lambda m.\lambda n.", r"m \ ", "S \ ", "n"])
        
        addition.set_color_by_tex("+", BLUE)
        addition.set_color_by_tex("S", BLUE)
        
        self.play(Write(addition[0]))
        self.wait()
        self.play(Write(addition[1]))
        self.wait()
        self.play(Write(addition[2]), Write(addition[3]))
        self.wait()
        self.play(Write(addition[4]))
        self.wait()
        
        addition_full = MathTex(r"+ = \lambda m.\lambda n.m \ (\lambda n.\lambda f.\lambda x.f \ (n \ f \ x)) \ n",
                                    substrings_to_isolate=["+ = ", r"\lambda m.\lambda n.", r"m \ ", "n"]).scale(0.5)
        addition_full.set_color_by_tex("+", BLUE)
        
        self.play(TransformMatchingTex(addition, addition_full))
        self.wait()
        self.play(Unwrite(successor_final, run_time=0.5), addition_full.animate.shift(UP).scale(0.7))
        self.wait()
        
        example_steps = []
        
        with open("3+5.json", "r") as file:
            data = json.load(file)
            for step in data:
                group = vgroup_from_lambda_diagram(step["Lines"]).move_to(ORIGIN)
                group.scale_to_fit_width(self.renderer.camera.frame_width - 1.5)
                example_steps.append(group)
                
        self.play(Write(example_steps[0]))
        
        for step in example_steps[1:]:
            self.play(Transform(example_steps[0], step), run_time=0.5)
            self.wait(0.2)
            