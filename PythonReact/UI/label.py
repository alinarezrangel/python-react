#!/usr/bin/env python3
# encoding: utf-8

"""Provides the Label container, a single line text output.

The Label element was designed for a non-changing (or sinple status)
text output, spawning only one line (optionally you can add more lines).
"""

from PythonReact import UI

class Label(UI.Container):
    """Represents the Label container, a single line text output.

    The Label is a container (and not an element) because you can
    add images, text tags and others to a label.

    NOTE: The label element should be only used as a container of
    text tags, never of other elements.
    """

    def __init__(self, *args, **kwargs):
        """Creates the new Label.

        The optional arguments are:

        * "form": True if the label is the label of a input element, False
        otherwise.
        * "label" (changeable): Label inner text.
        """
        super().__init__(*args, **kwargs)

        # Get the arguments or, it's default values
        self._form = super().register_argument("form", False)
        self._label = super().register_argument("label", "")

    def extend_properties(self, arguments):
        """Overload of UI.Container.extend_properties"""

        arguments = super().extend_properties(arguments)

        arguments["form"] = self._form

        return arguments

    def set_label(self, text):
        """Sets the label's inner text"""
        self._label = text

    def get_label(self):
        """Gets the label's inner text"""
        return self._label

    def render(self):
        # First: get the RenderedObject arguments:
        arguments = self.extend_properties({})

        # The rendered items of the box
        rendered_items = [self._label] + super().get_rendered_items()

        # Render this block and return
        result = UI.RenderedObject(
            tag_name = "label",
            properties = arguments,
            inner_content = rendered_items
        )
        return result
