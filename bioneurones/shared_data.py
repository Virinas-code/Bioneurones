#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bioneurones Shared Data.

Main window surface and settings.
"""
from typing import Optional

from .gui import Window
from .gui.settings import Settings
from .world import World

__all__: list[str] = ["settings", "window"]

settings: Settings = Settings()
window: Window = Window()
world: Optional[
    World
] = None  # TODO: Add type verification to shared_data.world
