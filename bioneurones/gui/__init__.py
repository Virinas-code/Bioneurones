#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bioneurones Main GUI.

Main window object.
"""
import tkinter as tk
from tkinter import ttk


class Window:
    """Main window."""

    def __init__(self) -> None:
        """
        Create window.

        Main window base class.
        """
        self.window: tk.Tk = tk.Tk()
        self.window.title("Bioneurones")
        self.window.iconbitmap("data/icon.ico")
