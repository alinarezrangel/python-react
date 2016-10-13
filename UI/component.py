#!/usr/bin/env python
# encoding: utf-8

"""Provides the Component class, the main class for all UI components.

"""

__author__ = "Alejandro Linarez"
__copyright__ = "Anton Danilchenko"
__credits__ = ["Anton Danilchenko", "Alejandro Linarez"]

__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Alejandro Linarez"
# __email__ = ""
__status__ = "Development"

class Component:

    # Only accepts keyword arguments because they are more semantic
    # than normal list arguments
    def __init__(self, **kwargs):
        self._props = kwargs

    def render(self):
        return 

