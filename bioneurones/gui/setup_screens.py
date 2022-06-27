#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bioneurones Settings GUI.

COnfiguration windows object.
"""
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from typing import Callable

import pygame
import pygame_menu
import pygame_menu.events
import pygame_menu.font
import pygame_menu.locals
import pygame_menu.themes
import pygame_menu.widgets
from bioneurones.gui import settings

from bioneurones.gui.settings import Settings


class MenuManager:
    """Setup screens."""

    def __init__(
        self,
        surface: pygame.Surface,
        resolution: tuple[int, int],
        core_reload: Callable[[], None],
        core_new_world: Callable[[], None],
        core_load_world: Callable[[str], None],
    ) -> None:
        """
        Initialize screens.

        :param surface: Window.
        :type surface: pygame.Surface
        :param resolution: Window size.
        :type resolution: tuple[int, int]
        """
        self.core_reload: Callable[[], None] = core_reload
        self.core_new_world: Callable[[], None] = core_new_world
        self.core_load_world: Callable[[str], None] = core_load_world
        self.surface: pygame.Surface = surface
        self.menu: pygame_menu.Menu = pygame_menu.Menu("", 1, 56)
        self.menu.disable()
        self.settings: Settings = Settings()
        self.resolution: tuple[int, int] = (
            self.settings.resolution_x,
            self.settings.resolution_y,
        )
        self.theme: pygame_menu.themes.Theme = pygame_menu.themes.Theme(
            background_color=(34, 40, 44),
            border_width=0,
            cursor_color=(255, 255, 255),
            cursor_selection_color=(128, 128, 255, 128),
            cursor_switch_ms=500,
            focus_background_color=(50, 50, 50, 255),
            fps=0,
            readonly_color=(128, 128, 128),
            readonly_selected_color=(200, 200, 200),
            scrollarea_outer_margin=(0, 0),
            scrollbar_color=(34, 40, 44),
            scrollbar_cursor=None,
            scrollbar_shadow=False,
            scrollbar_slider_color=(128, 128, 128),
            scrollbar_slider_hover_color=(200, 200, 200),
            scrollbar_slider_pad=5,
            scrollbar_thick=15,
            selection_color=(255, 255, 255),
            title=True,
            title_background_color=(128, 128, 128),
            title_bar_modify_scrollarea=False,
            title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_ADAPTIVE,
            title_close_button=False,
            title_fixed=False,
            title_floating=False,
            title_font=pygame_menu.font.FONT_FIRACODE,
            title_font_antialias=True,
            title_font_shadow=False,
            title_font_size=30,
            widget_alignment=pygame_menu.locals.ALIGN_CENTER,
            widget_background_color=(34, 40, 44),
            widget_font=pygame_menu.font.FONT_FIRACODE,
            widget_font_antialias=True,
            widget_font_size=20,
        )

    def disable(self) -> None:
        """
        Disable current menu.

        Use at every new screen.
        """
        self.menu.disable()

    def main_menu(self):
        """
        Main menu.

        Create a new game, load game and settings buttons.
        """
        self.disable()
        self.menu = pygame_menu.Menu(
            "Bioneurones",
            self.settings.resolution_x,
            self.settings.resolution_y,
            theme=self.theme,
        )
        self.menu.add.button("New World", action=self.core_new_world)
        self.menu.add.button("Load World", action=self.load_screen)
        self.menu.add.button("Settings", action=self.settings_screen)
        self.menu.add.button("Quit", action=pygame_menu.events.EXIT)
        self.menu.mainloop(self.surface)

    def load_screen(self):
        """
        Load World menu.

        File chooser.
        """
        Tk().withdraw()
        filename: str = askopenfilename()
        self.core_load_world(filename)

    def settings_screen(self) -> None:
        """
        Settings screen.

        :param save_settings: Callback to save settings.
        :type save_settings: function
        """
        self.disable()
        self.menu = pygame_menu.Menu(
            "Settings",
            self.resolution[0],
            self.resolution[1],
            theme=self.theme,
        )
        self.menu.add.button("Interface", action=self.configure_ui)
        self.menu.add.button("Save", action=self.settings_leave)
        self.menu.add.button("Quit", action=pygame_menu.events.EXIT)
        self.menu.mainloop(self.surface)

    def configure_ui(self) -> None:
        """
        UI Configuration screen.

        Sets colors and shapes.
        """
        self.disable()
        self.menu = pygame_menu.Menu(
            "Interface Configuration",
            self.resolution[0],
            self.resolution[1],
            theme=self.theme,
            columns=2,
            rows=3,
        )
        self.menu.add.text_input(
            "X Resolution: ",
            default=self.settings.resolution_x,
            input_type=pygame_menu.locals.INPUT_INT,
            onchange=lambda value: setattr(
                self.settings, "resolution_x", value
            ),
        )
        self.menu.add.color_input(
            "Background Color",
            color_type="hex",
            default=self.settings.background_color,
            onchange=lambda value: setattr(
                self.settings, "background_color", value
            ),
        )
        self.menu.add.none_widget()
        self.menu.add.text_input(
            "Y Resolution: ",
            default=self.settings.resolution_y,
            input_type=pygame_menu.locals.INPUT_INT,
            onchange=lambda value: setattr(
                self.settings, "resolution_y", value
            ),
        )
        self.menu.add.none_widget()
        self.menu.add.button("OK", action=self.settings_screen)
        self.menu.mainloop(self.surface)

    def settings_leave(self) -> None:
        """
        Leave settings screen.

        Save parameters and reload window.
        """
        print(f"{self.settings.resolution_x=}")
        self.settings.save_settings()
        self.core_reload()
        self.resolution = (
            self.settings.resolution_x,
            self.settings.resolution_y,
        )
        self.main_menu()
