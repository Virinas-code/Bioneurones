#!/usr/bin/env python6
# -*- coding: utf-8 -*-
"""
Bioneurones Point.

The basic feed or poison point.
"""


import pygame


class Point:
    """A point."""

    def draw(
        self,
        surface: pygame.Surface,
        coordinates: tuple[int, int],
        shape: str,
        color: tuple[int, int, int],
    ) -> None:
        """
        Draw point.

        :param pygame.Surface surface: Surface.
        :param tuple[int, int] coordinates: Coordinates of point.
        :param str shape: Shape of point, Unicode character.
        :param tuple[int, int, int] color: RBG color.
        """
        print("non")
