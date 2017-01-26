#!/usr/bin/env python
# encoding: utf-8

"""Provides the Block class, the main UI container element.

The Block element is a basic container of other elements. The layout of
the block can be changed.
"""

from .renderedobject import *
from .element import *

class Container(Element):
    """Represents a Container Element, the basic container.

    It's designed for provide a simple, easy and ready-to-use container
    with a very simple layout system.
    """


    def __init__(self, *args, **kwargs):
        """Creates the new Container.

        The optional arguments are:

        * \"items\": A list with the block childs.
        * \"style\": the element's style classes (inherited)
        """
        super().__init__(*args, **kwargs)

        # Get the arguments or, it's default values
        self._items = super().register_argument("items", [])

        # Type check
        if not isinstance(self._items, list):
            raise TypeError("items keyword argument should be a list")

    def get_items(self):
        """Gets all container childs in a list."""
        return self._items

    def add(self, *elements):
        """Adds an element to this block."""

        for element in elements:
            self._items.append(element)

    def extend_properties(self, arguments):
        """Overload of UI.Element.extend_properties"""

        arguments = super().extend_properties(arguments)

        return arguments

    def render(self):
        # First: get the RenderedObject arguments:
        arguments = self.extend_properties({})

        # The rendered items of the box
        rendered_items = []

        # Render all items and push their in the list
        for child in self._items:
            rendered_items.append(child.render())

        # Render this block and return
        result = RenderedObject(
            tag_name = "container",
            properties = arguments,
            inner_content = rendered_items
        )
        return result
