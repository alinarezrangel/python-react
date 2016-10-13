#!/usr/bin/env python3
# encoding: utf-8

"""Provides the Separator element, a content separator.

Generally, the separator is unnecesary (you can split the content in
two containers or make other section). The default separator is
displayed like a solid bar (but this may change with the used engine).
"""

from PythonReact import UI

class Separator(UI.Element):
    """Represents the Separator element, a content separator.

    The separator represents a semantic change in the content of the
    container, the separators come in two forms: the horizontal (default)
    used in containers and the vertical, used in rows (or grids).

    The separator modes are;

    SEPARATOR_H - Horizontal Separator
    SEPARATOR_V - Vertical Separator

    NOTE: The SEPARATOR_* modes depends on the engine used, some
    engines may not support vertical or horizontal separators.
    """

    SEPARATOR_H = 1
    SEPARATOR_V = 2

    def __init__(self, *args, **kwargs):
        """Creates the new Separator.

        The optional arguments are:

        * "mode": any of the SEPARATOR_* values.
        """
        super().__init__(*args, **kwargs)

        self._mode = super().register_argument("mode", Separator.SEPARATOR_H)

    def extend_properties(self, arguments):
        """Overload of UI.Container.extend_properties"""

        arguments = super().extend_properties(arguments)

        arguments["mode"] = self._mode

        return arguments

    def render(self):
        # First: get the RenderedObject arguments:
        arguments = self.extend_properties({})

        # Render this block and return
        result = UI.RenderedObject(
            tag_name = "separator",
            properties = arguments,
            inner_content = []
        )
        return result
