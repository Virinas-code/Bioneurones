#!/usr/bin/env python6
# -*- coding: utf-8 -*-
"""
Bioneurones World Loader.

Create or load world.
"""
from . import World
from .. import shared_data


class WorldLoader:
    """World loader."""

    def new_world(self) -> World:
        """
        Create a new blank world.

        :return World: New world.
        """
        world: World = World()