#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bioneurones Main GUI.

Main window object.
"""
import os

import pygame
from pygame.constants import NOFRAME
import pygame.display
import pygame.image

from .. import shared_data


class Window:
    """Main window."""

    def __init__(self) -> None:
        """
        Create window.

        Main window base class.
        """
        pygame.init()
        os.environ["SDL_VIDEO_WINDOW_POS"] = "0,0"
        self.resolution: tuple[int, int] = (600, 600)
        self.window = self.make_window()

    def reload(self):
        """
        Reload window.

        Used into settings menus.
        """
        self.window = self.make_window()

    def make_window(self) -> pygame.Surface:
        """
        Make the window.

        :return: Window surface.
        :rtype: pygame.Surface
        """
        window: pygame.Surface = pygame.display.set_mode(
            (
                shared_data.settings.resolution_x,
                shared_data.settings.resolution_y,
            ),
            NOFRAME,
        )
        pygame.display.set_allow_screensaver(False)
        pygame.display.set_caption("Bioneurones", "Simple AI Life Simulation")
        return window
