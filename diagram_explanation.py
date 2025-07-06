from manim import *
from vgroup_from_lambda_diagram import *
import json


class Diagrams(MovingCameraScene):
    def construct(self):
        identity = MathTex(r"\lambda x.x", substrings_to_isolate=["\lambda x."]).move_to(0.9 * DOWN)
        identity.set_color_by_tex("x", RED)
        identity.set_color_by_tex("\lambda x.", BLUE)

        self.play(Write(identity))
        self.wait()

        with open("identity.json", "r") as file:
            data = json.load(file)
            identity_diagram = vgroup_from_lambda_diagram(data["Lines"]).move_to(ORIGIN + 0.5 * UP).scale(0.4)

        with open("application.json", "r") as file:
            data = json.load(file)
            application_diagram = vgroup_from_lambda_diagram(data["Lines"]).move_to(ORIGIN + 0.5 * UP).scale(0.3)

        bounding_box = SurroundingRectangle(identity[0])

        self.play(Create(bounding_box))
        self.wait()
        self.play(ReplacementTransform(identity[0].copy(), identity_diagram[0]))
        self.wait()
        self.play(Transform(bounding_box, SurroundingRectangle(identity[1])))
        self.wait()
        self.play(ReplacementTransform(identity[1].copy(), identity_diagram[1]))
        self.wait()

        application = MathTex(r"\lambda x.x \ x", substrings_to_isolate=["\lambda x.", " \ x"]).move_to(
            0.9 * DOWN).set_color_by_tex("x", RED).set_color_by_tex("\lambda x.", BLUE).set_color_by_tex(" \ x", GREEN)

        self.play(TransformMatchingTex(identity,
                                       application),
                  Transform(bounding_box, SurroundingRectangle(application[2])))
        
        self.wait()
        self.play(Transform(identity_diagram[0], application_diagram[0]),
                  Transform(identity_diagram[1], VGroup(application_diagram[1], application_diagram[2])),
                  Transform(application[2].copy(), application_diagram[3::]))
        self.wait()
        self.play(Unwrite(application), Uncreate(bounding_box), Unwrite(identity_diagram))