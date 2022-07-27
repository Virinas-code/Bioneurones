#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bioneurones.

Simple AI life simulation.
"""
from multiprocessing import Process
from multiprocessing.managers import BaseManager
import time
from typing import Callable

from .ui.display import Display
from .settings import Settings


class Bioneurones:
    """Main object."""

    def __init__(self, version: str) -> None:
        """
        Initialize game.

        Starts the loading screen.

        :param str version: Current version.
        """
        BaseManager.register("Settings", Settings)
        self.manager: BaseManager = BaseManager()
        self.manager.start()
        self.settings_var: Callable = self.manager.Settings()  # type: ignore
        self.display_var: Display = Display()
        self.display_process: Process = Process(
            target=self.display, args=[self.display_var, self.settings_var]
        )
        self.world_process: Process = Process(
            target=self.world, args=[self.settings_var]
        )

    def display(self, display: Display, settings: Settings) -> None:
        """
        Main display process.

        Manage UI.

        :param Settings settings: Shared settings.
        """
        print(settings.get_variable("resolution_x"))
        settings.set_variable(
            "resolution_x", settings.get_variable("resolution_x") + 100
        )

    def world(self, settings: Settings) -> None:
        """
        Main world process.

        Manage world calculations.

        :param Settings settings: Shared settings.
        """
        time.sleep(3)
        print(settings.get_variable("resolution_x"))

    def start(self) -> None:
        """
        Starts processes.

        Starts the game.
        """
        self.display_process.start()
        self.world_process.start()
        self.display_process.join()
        self.world_process.join()
        self.settings_var.save_settings()  # type: ignore # Shared variable
        self.display_var.quit()
        self.manager.shutdown()
