#!/usr/bin/env python
# encoding: utf-8

"""Provides the Block class, the main UI container element.

The Block element is a basic container of other elements. The layout of
the block can be changed.
"""

from .renderedobject import *
from .element import *

class Block(Element):
    """Represents a Block Element, the basic container.

    It's designed for provide a simple, easy and ready-to-use container
    with a very simple layout system.

    Constansts:

    ALIGN_ROW: Align constant, align the block items in a row.
    ALIGN_COLUMN: Align constant, align the block items in a column.
    """

    # Align modes
    ALIGN_ROW = 1
    ALIGN_COLUMN = 2

    def __init__(self, *args, **kwargs):
        """Creates the new Block.

        The optional arguments are:

        * \"items\": A list with the block childs.
        * \"align\": the align mode (see the Block.ALIGN_*)
        * \"style\": the element's style classes
        """
        super().__init__()

        # Get the arguments or, it's default values
        self._items = kwargs.get("items", [])
        self._align = kwargs.get("align", Block.ALIGN_ROW)
        self._args = kwargs
        super().set_class_list(kwargs.get("style", []))

        # Type check
        if type(self._items) != list:
            raise TypeError("items keyword argument is should be a list")
        if type(self._align) != int:
            raise TypeError("align keyword argument is should be an integer")

    def add(self, element):
        """Adds an element to this block."""
        self._items.append(element)

    def render(self):
        # TODO: These values should be changed according to
        # the rendering engine.

        # First: get the RenderedObject arguments:
        arguments = {}
        # style argument is the class list
        arguments["style"] = ""
        # The super().classList() is a list, but we need a CSS-like string:
        for class_ in super().class_list():
            arguments["style"] += " " + str(class_)
        # align is the align mode (ROW or COLUMN)
        if self._align == Block.ALIGN_COLUMN:
            arguments["align"] = "column"
        else:
            arguments["align"] = "row"

        # Pass to RenderedObject all arguments except
        # style, items and align
        for key, value in self._args.items():
            if (key != "style") and (key != "align") and (key != "items"):
                arguments[key] = value

        # The rendered items of the box
        rendered_items = []

        # Render all items and push their in the list
        for child in self._items:
            rendered_items.append(child.render())

        # Render this block and return
        result = RenderedObject(
            tag_name = "box",
            properties = arguments,
            inner_content = rendered_items
        )
        return result
