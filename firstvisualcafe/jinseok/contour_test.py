#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 16:27:40 2021

@author: jinseok
"""

from manim import *
from typing import *
from colour import Color
class Surface_with_contour(Surface):
    def __init__(self, contour_func : Callable[[float, float], np.ndarray],
                 func: Callable[[float, float], np.ndarray],
                 u_range: Sequence[float] = [0, 1],
                 v_range: Sequence[float] = [0, 1],
                 resolution: Sequence[int] = 32,
                 surface_piece_config: dict = {},
                 fill_color: "Color" = BLUE_D,
                 fill_opacity: float = 1.0,
                 checkerboard_colors: Sequence["Color"] = [BLUE_D, BLUE_E],
                 stroke_color: "Color" = LIGHT_GREY,
                 stroke_width: float = 0.5,
                 should_make_jagged: bool = False,
                 pre_function_handle_to_anchor_scale_factor: float = 0.00001,
                 **kwargs):
        super().__init__(func,u_range,
        v_range,
        resolution,
        surface_piece_config,
        fill_color,
        fill_opacity,
        checkerboard_colors,
        stroke_color,
        stroke_width,
        should_make_jagged,
        pre_function_handle_to_anchor_scale_factor)
        self.contour_func = contour_func
        
    def set_contour_color(self, axes: "Mobject", colors: Union[Iterable[Color], Color]):
        if type(colors[0]) is tuple:
            new_colors, pivots = [[i for i, j in colors], [j for i, j in colors]]
        else:
            new_colors = colors

            pivot_min = axes.z_range[0]
            pivot_max = axes.z_range[1]
            pivot_frequency = (pivot_max - pivot_min) / (len(new_colors) - 1)
            pivots = np.arange(
                start=pivot_min, stop=pivot_max + pivot_frequency, step=pivot_frequency
            )

        for mob in self.family_members_with_points():
            z_value = axes.point_to_coords(mob.get_midpoint())[2]
            if z_value <= pivots[0]:
                mob.set_color(new_colors[0])
            elif z_value >= pivots[-1]:
                mob.set_color(new_colors[-1])
            else:
                for i, pivot in enumerate(pivots):
                    if pivot > z_value:
                        color_index = (z_value - pivots[i - 1]) / (
                                pivots[i] - pivots[i - 1]
                        )
                        color_index = min(color_index, 1)
                        mob_color = interpolate_color(
                            new_colors[i - 1], new_colors[i], color_index
                        )
                        if config.renderer == "opengl":
                            mob.set_color(mob_color, recurse=False)
                        else:
                            mob.set_color(mob_color, family=False)
                        mob.set_z(0)
                        break

            mob.set_z(0)

        return self


class FillByValueExample(ThreeDScene):
    def construct(self):
        resolution_fa = 42
        self.set_camera_orientation(phi=75 * DEGREES, theta=-120 * DEGREES)
        axes = ThreeDAxes(x_range=(0, 5, 1), y_range=(0, 5, 1), z_range=(-1, 1, 0.5))

        def param_surface(u, v):
            x = u
            y = v
            z = np.sin(x) * np.cos(y)
            return z
        def zero(u, v):
            return 0
        surface_plane = Surface_with_contour(
            contour_func = lambda u, v: axes.c2p(u, v, zero(u, v)),
            func = lambda u, v: axes.c2p(u, v, param_surface(u, v)),
            resolution=(resolution_fa, resolution_fa),
            v_range=[0, 5],
            u_range=[0, 5])
        surface_plane.set_style(fill_opacity=1)
        surface_plane.set_fill_by_value(axes=axes, colors=[(RED, -0.4), (YELLOW, 0), (GREEN, 0.4)])
        surface_plane.set_contour_color(axes=axes, colors=[(RED, -0.4), (YELLOW, 0), (GREEN, 0.4)])
        self.add(axes, surface_plane)

scene = FillByValueExample()
scene.render()