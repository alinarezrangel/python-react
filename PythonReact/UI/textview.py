#!/usr/bin/env python3
# encoding: utf-8

"""Provides the TextView container, a read-only text viewer.

It's like a UI.Label, but may have multiline output and rich-text
capabilities.
"""

from PythonReact import UI

class TextView(UI.Container):
    """Represents the TextView container, a read-only text viewer.

    The TextView can be the container of images, text tags and others
    TextViews.

    The formatting of the text may be done using these selectors:

    TEXT_VIEW_NORMAL - The text whitespaces may be collapsed according to
    the rendering engine's whitespace preserving rules.
    TEXT_VIEW_RAW - The text content will be displayed as-is, generally
    with a monospaced font (but this can be overrided).
    TEXT_VIEW_CODE - The text content will be displayed as computer code.
    TEXT_VIEW_HEADING_TITLE - The text content will be displayed as a title,
    with a bolder and bigger font.
    TEXT_VIEW_HEADING_SUBTITLE - Like HEADING_TITLE, but with a smaller font.
    TEXT_VIEW_HEADING_SECTITLE - Like HEADING_SUBTITLE, but witha smaller font.

    These selectors can be used only with raw text sections (the add_text
    method) not with childs.
    """

    TEXT_VIEW_NORMAL = 1
    TEXT_VIEW_RAW = 2
    TEXT_VIEW_CODE = 3
    TEXT_VIEW_HEADING_TITLE = 4
    TEXT_VIEW_HEADING_SUBTITLE = 5
    TEXT_VIEW_HEADING_SECTITLE = 6

    class Node(UI.Element):
        """It's a TextView node

        The TextView.Node represents a node of text with a formatter
        (TEXT_VIEW_*) and a raw text content.
        """

        def __init__(self, *args, **kwargs):
            """Creates a new Node.

            The raw text content is "text"
            and the formatter is "fmt".
            """
            super().__init__(*args, **kwargs)

            self._text = super().register_argument("text", "")
            self._fmt = super().register_argument("fmt", 1)

        def get_text(self):
            """Gets the node's raw text content"""
            return self._text

        def get_format(self):
            """Gets the node's formatter"""
            return self._fmt

        def set_text(self, text):
            """Sets the node's raw text content"""
            self._text = text

        def set_format(self, fmt):
            """Sets the node's formatter"""
            self._fmt = fmt

        def render(self):
            # First: get the RenderedObject arguments:
            arguments = super().extend_properties({})

            tag_map = {
                TextView.TEXT_VIEW_NORMAL: "paragraph",
                TextView.TEXT_VIEW_RAW: "raw-text",
                TextView.TEXT_VIEW_CODE: "code-text",
                TextView.TEXT_VIEW_HEADING_TITLE: "title",
                TextView.TEXT_VIEW_HEADING_SUBTITLE: "subtitle",
                TextView.TEXT_VIEW_HEADING_SECTITLE: "sectiontitle",
            }

            tag = tag_map[self._fmt]

            # Render this block and return
            result = UI.RenderedObject(
                tag_name = tag,
                properties = arguments,
                inner_content = [self._text]
            )
            return result

    def __init__(self, *args, **kwargs):
        """Creates the new TextView."""
        super().__init__(*args, **kwargs)

    def extend_properties(self, arguments):
        """Overload of UI.Container.extend_properties"""

        arguments = super().extend_properties(arguments)

        return arguments

    def add_text(self, text, format):
        """Adds one text section to the TextView.
        
        text is a string with the text content and
        format is one of the TEXT_VIEW_*.
        """
        self.add(TextView.Node(
            text = text,
            fmt = format
        ))

    def render(self):
        # First: get the RenderedObject arguments:
        arguments = self.extend_properties({})

        # The rendered items of the box
        rendered_items = super().get_rendered_items()

        # Render this block and return
        result = UI.RenderedObject(
            tag_name = "text",
            properties = arguments,
            inner_content = rendered_items
        )
        return result
