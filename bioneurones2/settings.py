#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bioneurones.

Settings storage.
"""
import json
import os
import platform
import sys
from typing import Any


class Settings:
    """Settings."""

    def __init__(self):
        """
        Initialize variables.

        .. note::
            The :attr:settings attribute is only used for default values.
        """
        settings: dict[str, str] = self.load_settings()
        self.resolution_x = int(settings.get("resolutionX", 600))
        """Window width."""
        self.resolution_y = int(settings.get("resolutionY", 600))
        """Window height."""
        self.background_color: tuple[int, int, int] = tuple(
            (
                int(color)
                for color in settings.get("backgroundColor", "0,0,0").split(
                    ","
                )
            )
        )
        """World background color."""
        self.world_width: int = int(settings.get("worldWidth", 600))
        """World width for new worlds."""
        self.world_height: int = int(settings.get("worldHeight", 600))
        """World height for new worlds."""

    def load_settings(self) -> dict[str, str]:
        """
        Load Bioneurones settings.

        :return: Settings loaded, empty dict if not set.
        :rtype: dict[str, str]
        """
        path: str = "./"  # Default path is source (not recommended)
        if platform.system() == "Windows":
            path = os.environ["AppData"] + "/Bioneurones/"
        elif platform.system() == "Linux":
            path = "/home/" + os.getlogin() + "/.local/share/Bioneurones/"
        if os.path.isdir(path):
            with open(path + "config.json", encoding="utf-8") as file:
                settings: dict[str, str] = json.load(file)
            return settings
        os.mkdir(path)
        with open(path + "config.json", "w", encoding="utf-8") as write_file:
            write_file.write("{}")
        return {}

    def save_settings(self) -> None:
        """
        Save settings.

        .. note::
            Settings are saved in AppData on Windows,
            in /home/user/.local/share on Linux,
            and in the source path by default
            (not recommended, unknown behavior).
        """
        exported_settings: dict[str, str] = {
            "resolutionX": str(self.resolution_x),
            "resolutionY": str(self.resolution_y),
            "backgroundColor": ",".join(
                (str(color) for color in self.background_color)
            ),
            "worldWidth": str(self.world_width),
            "worldHeight": str(self.world_height),
        }
        path: str = "./"  # Default path is source (not recommended)
        if platform.system() == "Windows":
            path = os.environ["AppData"] + "/Bioneurones/"
        elif platform.system() == "Linux":
            path = "/home/" + os.getlogin() + "/.local/share/Bioneurones/"
        if not os.path.isdir(path):
            os.mkdir(path)
        with open(path + "config.json", "w", encoding="utf-8") as write_file:
            json.dump(exported_settings, write_file)

    def get_variable(self, variable: str) -> Any:
        """
        Get a variable.

        Used for multiprocessing.

        :param str variable: The name of the variable to get.
        :return Any: The value of the variable.
        """
        return getattr(self, variable)

    def set_variable(self, variable: str, value: Any) -> None:
        """
        Set a varaible.

        Used for multiprocessing.

        :param str variable: The name of the variable to get.
        :param Any value: The new value of the variable.
        """
        return setattr(self, variable, value)
