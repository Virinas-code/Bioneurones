#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bioneurones.

Starts program.
"""
from . import Bioneurones

VERSION: str = "Indev"

if __name__ == "__main__":
    main: Bioneurones = Bioneurones(VERSION)
    main.start()
