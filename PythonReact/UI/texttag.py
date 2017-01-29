#!/usr/bin/env python3
# encoding: utf-8

"""Provides the TextTag element, a text-section formatter.

Most of text-output elements supports this kind of child.
"""

from PythonReact import UI

class TextTag(UI.Element):
    """Represents the TextTag element, a single line text output.

    The TextTag can't contain childs, for formatting a text with more
    that one text tag, use the "mix" method.

    The TEXT_TAG_* are:

    TEXT_TAG_NONE - Not changes the text style/format
    TEXT_TAG_NORMAL - Sets the text to the default style & format
    TEXT_TAG_CUSTOM - The text style/format is defined by the classes
    TEXT_TAG_LINK - The text tag is a link (similar to a link element)
    TEXT_TAG_BOLD - The text is displayed in a bold font
    TEXT_TAG_ITALIC - The text is displayed in a italic font
    TEXT_TAG_UNDERLINE - The text is displayed with a underline
    TEXT_TAG_STRIKE - The text is displayed with a strike
    TEXT_TAG_SUPERLINE - The text is displayed with a superline
    TEXT_TAG_QUOTE - The text is a quote or a cite to a resource
    TEXT_TAG_SUBSCRIPT - The text is displayed like a subscript
    TEXT_TAG_SUPERSCRIPT - The text is displayed like a superscript
    TEXT_TAG_SMALL - Like NORMAL, but with a smaller font size
    TEXT_TAG_BIG - Like NORMAL, but with a bigger font size
    TEXT_TAG_SERIF - Tries to use a serif font
    TEXT_TAG_SANS_SERIF - Tries to use a sans-serif font
    TEXT_TAG_MONOSPACE - Tries to use a monospaced font

    There is no warranty of the rendering engine to support
    all of these text tags, in any case, if the text can not be
    formatted, it will be displayed like TEXT_TAG_NONE.
    """

    TEXT_TAG_NONE = "none"
    TEXT_TAG_NORMAL = "normal"
    TEXT_TAG_CUSTOM = "custom"
    TEXT_TAG_LINK = "link"
    TEXT_TAG_BOLD = "bold"
    TEXT_TAG_ITALIC = "italic"
    TEXT_TAG_UNDERLINE = "underline"
    TEXT_TAG_STRIKE = "strike"
    TEXT_TAG_SUPERLINE = "superline"
    TEXT_TAG_QUOTE = "quote"
    TEXT_TAG_SUBSCRIPT = "subscript"
    TEXT_TAG_SUPERSCRIPT = "superscript"
    TEXT_TAG_SMALL = "small"
    TEXT_TAG_BIG = "big"
    TEXT_TAG_SERIF = "serif"
    TEXT_TAG_SANS_SERIF = "sans-serif"
    TEXT_TAG_MONOSPACE = "monospace"

    def __init__(self, *args, **kwargs):
        """Creates the new TextTag.

        The optional arguments are:

        * "type": One of the TEXT_TAG_* tags.
        * "text": The text to format.
        * "href" (if type if TEXT_TAG_LINK): HyperReference (URI/URL) to the
        resource.

        NOTE: The TextTag element can NOT contains childs, but in rendering,
        the mix method does some similar to nesting TexTags.
        """
        super().__init__(*args, **kwargs)

        # Get the arguments or, it's default values
        self._type = super().register_argument("type", TextTag.TEXT_TAG_NONE)
        self._text = super().register_argument("text", "")
        self._href = super().register_argument("href", "#")
        self._mixed = False

    def extend_properties(self, arguments):
        """Overload of UI.Container.extend_properties"""

        arguments = super().extend_properties(arguments)

        arguments["type"] = self._type
        arguments["href"] = self._href

        return arguments

    def set_text(self, text):
        """Sets the texttag's inner text"""
        self._text = text

    def get_text(self):
        """Gets the texttag's inner text"""
        return self._text

    def mix(self, tag):
        """Mixes this and "tag" text tags.

        In the mix, this tag's text content will be destroyed and
        the "tag" text tag will be used instead. The get_text
        method will return tag.
        """

        self._text = tag
        self._mixed = True

    def render(self):
        # First: get the RenderedObject arguments:
        arguments = self.extend_properties({})

        # The rendered items of the box
        txt = self._text
        if self._mixed:
            txt = txt.render()
        rendered_items = [txt]

        # Render this block and return
        result = UI.RenderedObject(
            tag_name = "text-tag",
            properties = arguments,
            inner_content = rendered_items
        )
        return result
