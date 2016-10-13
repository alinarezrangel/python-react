#!/usr/bin/env python3
# encoding: utf-8

"""Provides the Container class, the main UI container element.

The Container element is a basic container of other elements. The layout of
the container can not be changed.
"""

from PythonReact import UI

class Container(UI.Element):
    """Represents a Container Element, the basic container.

    It's designed for provide a simple, easy and ready-to-use container
    with a very simple layout system.
    """


    def __init__(self, *args, **kwargs):
        """Creates the new Container.

        The optional arguments are:

        * "items": A list with the block childs.
        * "style": the element's style classes (inherited)
        """
        super().__init__(*args, **kwargs)

        # Get the arguments or, it's default values
        self._items = super().register_argument("items", [])

    def get_items(self):
        """Gets all container childs in a list."""
        return self._items

    def add(self, *elements):
        """Adds an element to this block."""

        for element in elements:
            self._items.append(element)

    def get_rendered_items(self):
        """Like get_items, but the returned list contains the rendered items"""
        return [i.render() for i in self._items]

    def render(self):
        # First: get the RenderedObject arguments:

        # Element recommends to override extend_properties,
        # but this method will not do anything in this specific
        # container, because this, I prefer to not override
        # it now.
        arguments = super().extend_properties({})

        # The rendered items of the box
        rendered_items = self.get_rendered_items()

        # Render this block and return
        result = UI.RenderedObject(
            tag_name = "container",
            properties = arguments,
            inner_content = rendered_items
        )
        return result
