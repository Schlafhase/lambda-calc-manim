from manim import *
from vgroup_from_lambda_diagram import *
import json

class DiagramScene(MovingCameraScene):
    def construct(self):
        
        diagrams = []
        
        with open("/home/Linus/Downloads/steps(3).json", "r") as file:
            data = json.load(file)
            for step in data:
                diagrams.append(vgroup_from_lambda_diagram(step["Lines"]))
        
        self.camera.frame.set_width(diagrams[0].get_width() * 1.2).move_to(diagrams[0].get_center())
        self.play(Write(diagrams[0]))

        
        for diagram in diagrams:
            # self.play(self.camera.frame.animate.set_width(diagram.get_width() * 1.2).move_to(diagram.get_center()), run_time=1)
            self.play(Transform(diagrams[0], diagram), self.camera.frame.animate.set_width(diagram.get_width() * 1.2).move_to(diagram.get_center()), run_time=2)
            self.wait(0.5)
        
        self.wait(2)