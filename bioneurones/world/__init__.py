#!/usr/bin/env python6
# -*- coding: utf-8 -*-
"""
Bioneurones World.

Where everything live.
"""
import json

import numpy
import pygame

from .. import shared_data


class World:
    """The world."""

    def __init__(self, world_size: tuple[int, int], map: numpy.ndarray):
        """
        Initialize world.

        :param tuple[int, int] world_size: World size.
        :param numpy.ndarray map: World map.
        """
        self.world_size: tuple[int, int] = world_size
        self.map: numpy.ndarray = numpy.full(world_size, [])

    @classmethod
    def new_world(cls):
        """
        Generate a new world.

        Parameters are taken from settings.

        :param tuple[int, int] size: World size in pixels.
        """
        map: numpy.ndarray = numpy.full(
            (
                shared_data.settings.world_width,
                shared_data.settings.world_height,
            ),
            None,
        )

    def save_world(self, filename: str) -> None:
        """
        Save world to file.

        :param str filename: Destination file.
        """
        data: dict[str, str] = {
            "sizeX": str(self.world_size[0]),
            "sizeY": str(self.world_size[1]),
        }
        with open(filename, encoding="utf-8") as file:
            json.dump(data, file)

    @classmethod
    def load_world(cls, filename: str):
        """
        Load world from file.

        :param str filename: File name.
        """
        with open(filename, encoding="utf-8") as file:
            data: dict[str, str] = json.load(file)

        return cls((int(data["sizeX"]), int(data["sizeY"])))

    def add_points(self, feed_count: int, poison_count: int) -> None:
        """
        Add points to map.

        :param int feed_count: Number of feed points.
        :param int poison_count: Number of poison points.
        """
        d1_map: numpy.ndarray = self.map.ravel()
        points_indexes: numpy.ndarray = numpy.random.choice(
            d1_map.shape[0], feed_count
        )
        for point in points_indexes:
            d1_map[point] = FeedPoint()
