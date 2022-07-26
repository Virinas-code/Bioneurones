#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bioneurones.

Starting UI.
"""
from . import Display


class Launcher:
    """Starting UI object."""

    def __init__(self, display: Display, version: str) -> None:
        """
        Initialize game.

        Starts the loading screen.

        :param str version: Current version.
        """
        self.display: Display = display
    
    def stat
    def tick(self) -> None:
        """
        Run one tick.
        
        Displays loading screen.
        """
