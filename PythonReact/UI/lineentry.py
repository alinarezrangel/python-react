#!/usr/bin/env python3
# encoding: utf-8

"""Provides the LineEntry element, a general single-line input method.

Is useful in forms and interactive elements.
"""

from PythonReact import UI

class LineEntry(UI.Entry):
    """Represents the LineEntry element, a general single-line input method."""

    def __init__(self, *args, **kwargs):
        """Creates the new LineEntry."""
        super().__init__(*args, **kwargs)

    def render(self):
        # First: get the RenderedObject arguments:
        arguments = self.extend_properties({})

        # The rendered items of the box
        rendered_items = []

        # Render this block and return
        result = UI.RenderedObject(
            tag_name = "line-entry",
            properties = arguments,
            inner_content = rendered_items
        )
        return result
