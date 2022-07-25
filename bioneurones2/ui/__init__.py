#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bioneurones.

Pygame display.
"""
import pygame


class Display:
    """Screen object."""

    def __init__(self) -> None:
        """
        Initialize display.

        Make surface.
        """
        self.window: pygame.Surface = pygame.display.set_mode(
            (400, 150)
        )  # type: ignore

    def make_main_window(self, size: tuple[int, int]) -> None:
        """
        Create main window.

        :param tuple[int, int] size: Windows size.
        """
        self.window = pygame.display.set_mode(size, pygame.)