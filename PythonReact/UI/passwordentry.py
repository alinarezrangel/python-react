#!/usr/bin/env python3
# encoding: utf-8

"""Provides the PasswordEntry element, a general single-line password input.

Is useful in forms and interactive elements.
"""

from PythonReact import UI

class PasswordEntry(UI.Entry):
    """Represents the PasswordEntry element, a general single-line password input."""

    def __init__(self, *args, **kwargs):
        """Creates the new PasswordEntry."""
        super().__init__(*args, **kwargs)

    def render(self):
        # First: get the RenderedObject arguments:
        arguments = self.extend_properties({})

        # The rendered items of the box
        rendered_items = []

        # Render this block and return
        result = UI.RenderedObject(
            tag_name = "password-entry",
            properties = arguments,
            inner_content = rendered_items
        )
        return result
