#!/usr/bin/env python3
# encoding: utf-8

"""Provides the Link container, a single line hyperlink.

The Link element it's a label with a href attribute.
"""

from PythonReact import UI

class Link(UI.Label):
    """Represents the Link container, a single line hyperlink.

    The Link is a container (and not an element) because you can
    add images, text tags and others to a link.

    NOTE: The link element should be only used as a container of
    text tags, never of other elements.
    """

    def __init__(self, *args, **kwargs):
        """Creates the new Link.

        The optional arguments are:

        * All of UI.Label
        * "href": HyperReference (URI/URL) to the resource.
        """
        super().__init__(*args, **kwargs)

        # Get the arguments or, it's default values
        self._href = super().register_argument("href", "#")

    def extend_properties(self, arguments):
        """Overload of UI.Container.extend_properties"""

        arguments = super().extend_properties(arguments)

        arguments["href"] = self._href

        return arguments

    def set_href(self, href):
        """Sets the label's hyperreference"""
        self._href = href

    def get_href(self):
        """Gets the label's hyperreference"""
        return self._href

    def render(self):
        # First: get the RenderedObject arguments:
        arguments = self.extend_properties({})

        # The rendered items of the box
        rendered_items = [self._label] + super().get_rendered_items()

        # Render this block and return
        result = UI.RenderedObject(
            tag_name = "link",
            properties = arguments,
            inner_content = rendered_items
        )
        return result
