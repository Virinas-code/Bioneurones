#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bioneurones.

Pygame display.
"""
import os
import platform
import pygame


class Display:
    """Screen object."""

    def __init__(self) -> None:
        """
        Initialize display.

        Make surface.
        """
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        pygame.display.init()
        self.window: pygame.Surface = self.make_main_window((600, 600))
        self.setup()

    def setup(self) -> None:
        """
        Setup additional window informations.

        Setup name, icon.
        """
        pygame.display.set_caption("Bioneurones", "Simple AI Life Simulation")
        pygame.display.set_allow_screensaver(False)
        path: str = ""
        if platform.system() == "Linux":
            path = os.path.abspath(
                os.path.join(os.sep, "usr", "share", "bioneurones", "icon.png")
            )
        elif platform.system() == "Windows":
            path = os.path.abspath(
                os.path.join(os.sep, "Programmes", "bioneurones", "icon.png")
            )
        else:
            raise RuntimeError("Unsupported OS {0}".format(platform.system()))
        icon: pygame.Surface = pygame.image.load(path).convert()
        pygame.display.set_icon(icon)

    def make_main_window(self, size: tuple[int, int]) -> pygame.Surface:
        """
        Create main window.

        :param tuple[int, int] size: Windows size.
        :return pygame.Surface: Window surface.
        """
        window = pygame.display.set_mode(size)
        self.setup()
        return window

    def get(self) -> pygame.Surface:
        """
        Get window surface.

        :return pygame.Surface: Window surface object.
        """
        return self.window

    def quit(self) -> None:
        """
        Close window.

        Closes all windows and stops pygame.
        """
        pygame.display.quit()
