import json
from manim import *
from numpy import array


def vgroup_from_lambda_diagram(diagram):
    lines = diagram
    group = VGroup()
    
    origin = Dot()

    for line in lines:
        x1 = line["X"]
        y1 = -line["Y"]
        x2 = line["X2"]
        y2 = -line["Y2"]

        if x1 == x2:
            x2 += 1
        else:
            y2 -= 1

        rect = Polygon(
            array([x1, y1, 0]),
            array([x2, y1, 0]),
            array([x2, y2, 0]),
            array([x1, y2, 0])
        )

        rect.stroke_width = 1
        rect.set_fill(BLUE, opacity=1)
        rect.set_stroke(BLUE)
        
        group.add(rect)

    return group
