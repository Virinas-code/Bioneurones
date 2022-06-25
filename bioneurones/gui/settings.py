#!/usr/bin/env python6
# -*- coding: utf-8 -*-
"""
Bioneurones GUI Settings.

Getters and setters for settings.
"""
import json
import os
import sys


class Settings:
    """Settings."""

    def __init__(self):
        """
        Initialize variables.

        .. note::
            Using @property.
        """
        self.settings: dict[str, str] = self.load_settings()
        self._resolution_x = int(self.settings.get("resolutionX", 600))
        self._resolution_y = int(self.settings.get("resolutionY", 600))

    def load_settings(self) -> dict[str, str]:
        """
        Load Bioneurones settings.

        :return: Settings loaded, empty dict if not set.
        :rtype: dict[str, str]
        """
        path: str = "./"  # Default path is source (not recommended)
        if sys.platform == "win32":
            path = os.environ["AppData"] + "/Bioneurones/"
        elif sys.platform in ("linux", "linux2"):
            path = "/home/" + os.getlogin() + "/.local/share/Bioneurones/"
        if os.path.exists(path):
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
        path: str = "./"  # Default path is source (not recommended)
        if sys.platform == "win32":
            path = os.environ["AppData"] + "/Bioneurones/"
        elif sys.platform in ("linux", "linux2"):
            path = "/home/" + os.getlogin() + "/.local/share/Bioneurones/"
        if not os.path.exists(path):
            os.mkdir(path)
        with open(path + "config.json", "w", encoding="utf-8") as write_file:
            json.dump(self.settings, write_file)

    @property
    def resolution_x(self) -> int:
        """X Resolution."""
        return self._resolution_x

    @resolution_x.setter
    def resolution_x(self, value: int) -> None:
        self._resolution_x = max(600, value)
        self.settings["resolutionX"] = str(self._resolution_x)

    @property
    def resolution_y(self) -> int:
        """Y Resolution."""
        return self._resolution_y

    @resolution_y.setter
    def resolution_y(self, value: int) -> None:
        self._resolution_y = max(600, value)
        self.settings["resolutionY"] = str(self._resolution_y)
