from typing import Callable

from manim import *


class FixPoint(Scene):
    def construct(self):
        # Explain fix points
        function_tex = (MathTex(r"f(x) = \frac{1}{x}", color=BLUE, substrings_to_isolate=["f(x) ="])
                        .shift(3 * UP + 5 * LEFT))
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            x_length=7,
            y_length=7,
            axis_config={"color": WHITE},
        )

        labels = axes.get_axis_labels(x_label="x", y_label="f(x)")

        f = lambda x: 1 / x

        graph_positive = axes.plot(f, color=BLUE, x_range=[0.01, 5], use_smoothing=False)
        graph_negative = axes.plot(f, color=BLUE, x_range=[-5, -0.01], use_smoothing=False)
        graph = VGroup(graph_positive, graph_negative)

        fix_point_tex = (MathTex(r"c = f(c)", color=YELLOW, substrings_to_isolate=["= f(c)"])
                         .next_to(function_tex, DOWN, buff=0.2)).align_to(function_tex, LEFT)
        example_tex = (MathTex(r"1 = f(1)", color=YELLOW_E, substrings_to_isolate=["= f("])
                       .next_to(fix_point_tex, DOWN, buff=0.2)).align_to(fix_point_tex, LEFT)

        line = axes.plot(lambda x: x, color=GREEN, x_range=[-5, 5, 1], use_smoothing=False)
        intersections = VGroup(*find_intersections(axes, f, lambda x: x))

        self.play(Write(function_tex), Write(labels), Create(axes), Create(graph))
        self.wait()
        self.play(Write(fix_point_tex[0]))
        self.wait()
        self.play(Write(fix_point_tex[1]))
        self.wait()
        self.play(Create(line), Create(intersections))
        self.wait()
        self.play(Write(example_tex))
        self.wait()

        sine_tex = MathTex(r"f(x) = \sin(x)", color=BLUE, substrings_to_isolate=["f(x) ="]).move_to(
            function_tex).align_to(function_tex, LEFT)
        sine = axes.plot(np.sin, color=BLUE, x_range=[-5, 5], use_smoothing=False)
        sine_intersections = [Dot(axes.c2p(0, 0), color=YELLOW)]

        self.play(Transform(function_tex, sine_tex), Transform(graph, sine),
                  Transform(intersections, VGroup(*sine_intersections)),
                  Transform(example_tex, (MathTex(r"0 = f(0)", color=YELLOW_E, substrings_to_isolate=["= f("])
                                          .next_to(fix_point_tex, DOWN, buff=0.2)).align_to(fix_point_tex, LEFT)))
        self.wait()

        parabola_tex = MathTex(r"f(x) = x^2 + 2", color=BLUE, substrings_to_isolate=["f(x) ="]).move_to(
            function_tex).align_to(function_tex, LEFT)
        parabola = axes.plot(lambda x: x ** 2 + 2, color=BLUE, x_range=[-5, 5], use_smoothing=False)
        parabola_intersections = []

        self.play(Transform(function_tex, parabola_tex), Transform(graph, parabola),
                  Transform(intersections, VGroup(*parabola_intersections)), Unwrite(example_tex))
        self.wait()
        self.play(Unwrite(function_tex), Unwrite(labels), Unwrite(fix_point_tex), Uncreate(axes), Uncreate(graph),
                  Uncreate(line))


def find_intersections(axes: Axes, f: Callable[[float], float], g: Callable[[float], float]) -> list[Dot]:
    intersections = []
    x_range = axes.x_range
    for x in np.linspace(x_range[0], x_range[1], 1000):
        if np.isclose(f(x), g(x), atol=0.01):
            intersections.append(Dot(axes.c2p(x, f(x)), color=YELLOW))
    return intersections
