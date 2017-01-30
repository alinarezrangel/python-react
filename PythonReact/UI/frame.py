#!/usr/bin/env python3
# encoding: utf-8

"""Provides the Frame container, a container with a title.

The Frame container is useful in forms, when you need to group
a set of entries in the same category.
"""

from PythonReact import UI

class Frame(UI.Container):
    """Represents the Frame container, a container with a title.

    The title of the frame it's centered and generally, the frame
    displays a border around it's childs.
    """

    def __init__(self, *args, **kwargs):
        """Creates the new Frame.

        The optional arguments are:

        * "title": The title of the Frame.
        """
        super().__init__(*args, **kwargs)

        # Get the arguments or, it's default values
        self._title = super().register_argument("title", "")

    def extend_properties(self, arguments):
        """Overload of UI.Container.extend_properties"""

        arguments = super().extend_properties(arguments)

        arguments["title"] = self._title

        return arguments

    def render(self):
        # First: get the RenderedObject arguments:
        arguments = self.extend_properties({})

        # The rendered items of the box
        rendered_items = super().get_rendered_items()

        # Render this block and return
        result = UI.RenderedObject(
            tag_name = "frame",
            properties = arguments,
            inner_content = rendered_items
        )
        return result
