#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bioneurones Launcher.

Starts Bioneurones.
"""
from . import shared_data
from .gui.setup_screens import MenuManager


if __name__ == "__main__":
    print(dir(shared_data))
    MenuManager().main_menu()
