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
            The :attr:settings attribute is only used for default values.
        """
        settings: dict[str, str] = self.load_settings()
        self.resolution_x = int(settings.get("resolutionX", 600))
        self.resolution_y = int(settings.get("resolutionY", 600))
        self.background_color: str = settings.get("backgroundColor", "#000000")

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
        exported_settings: dict[str, str] = {
            "resolutionX": str(self.resolution_x),
            "resolutionY": str(self.resolution_y),
            "backgroundColor": self.background_color,
        }
        path: str = "./"  # Default path is source (not recommended)
        if sys.platform == "win32":
            path = os.environ["AppData"] + "/Bioneurones/"
        elif sys.platform in ("linux", "linux2"):
            path = "/home/" + os.getlogin() + "/.local/share/Bioneurones/"
        if not os.path.exists(path):
            os.mkdir(path)
        with open(path + "config.json", "w", encoding="utf-8") as write_file:
            json.dump(exported_settings, write_file)
