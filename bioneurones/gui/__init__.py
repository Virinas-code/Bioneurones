#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bioneurones Main GUI.

Main window object.
"""
import json
import os
import sys

import pygame
import pygame.display
import pygame.image
from pygame_menu import Menu

from .settings import Settings
from .setup_screens import MenuManager


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
        self.settings: Settings = Settings()
        self.menus: MenuManager = MenuManager(
            pygame.display.set_mode((600, 600)),
            self.resolution,
            self.core_reload,
            self.core_new_world,
            self.core_load_world,
        )
        self.window: pygame.Surface = self.make_window()
        self.menus.main_menu()

    def core_reload(self):
        """
        Reload window.

        Used into settings menus.
        """
        self.window = self.make_window()

    def core_new_world():
        return None

    def core_load_world(filenames: str):
        return None

    def make_window(self) -> pygame.Surface:
        """
        Make the window.

        :return: Window surface.
        :rtype: pygame.Surface
        """
        window: pygame.Surface = pygame.display.set_mode(
            (
                self.menus.settings.resolution_x,
                self.menus.settings.resolution_y,
            )
        )
        pygame.display.set_allow_screensaver(False)
        pygame.display.set_caption("Bioneurones", "Simple AI Life Simulation")
        return window
