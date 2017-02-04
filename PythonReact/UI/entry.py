#!/usr/bin/env python3
# encoding: utf-8

"""Provides the Entry element, a general (but abstract) input method.

The entries can receive text, multiline text, dates, times and others,
but this element is abstract and can not be used.
"""

from PythonReact import UI

class Entry(UI.Element):
    """Represents the Entry element, a general input method."""

    def __init__(self, *args, **kwargs):
        """Creates the new Entry.

        The optional arguments are:

        * "form_name": The name of the entry in the form data.
        * "onvaluechanged": Event emitted when the input value
        it's changed.
        * "placeholder": The text showed in the entries before
        any text is entered (not all entries support this).
        * "required": True if this entry is required for send
        the form, False otherwise.
        * "value": Value of the entry.
        """
        super().__init__(*args, **kwargs)

        # Get the arguments or, it's default values
        self._form_name = super().register_argument("form_name", "")
        self._onvaluechanged = super().register_argument("onvaluechanged", None)
        self._placeholder = super().register_argument("placeholder", "")
        self._required = super().register_argument("required", False)
        self._value = super().register_argument("value", "")

    def extend_properties(self, arguments):
        """Overload of UI.Container.extend_properties"""

        arguments = super().extend_properties(arguments)

        arguments["form_name"] = self._form_name
        arguments["placeholder"] = self._placeholder
        arguments["required"] = self._required
        arguments["onvaluechanged"] = self._onvaluechanged
        arguments["value"] = self._value

        return arguments

    def get_value(self):
        """Gets the entry's value"""
        return self._value

    def set_value(self, value):
        """Sets the entry's value"""
        self._value = value

    def set_value_changed_event(self, onclick):
        """Sets the entry's onvaluechanged event."""
        self._onclick = onclick

    def emit_value_changed_event(self, *args, **kwargs):
        """Calls the entry's onvaluechanged event"""
        return self._onvaluechanged(*args, **kwargs)

    def emit(self, event_name, *args, **kwargs):
        """Override of UI.Element.emit"""
        if event_name == UI.EVENT_NAME_VALUE_CHANGED:
            return self.emit_value_changed_event(*args, **kwargs)

        return super().emit(event_name, *args, **kwargs)

    def have_event(self, event_name):
        """Override of UI.Element.have_event"""
        if event_name == UI.EVENT_NAME_VALUE_CHANGED:
            return self._onvaluechanged is not None

        return super().have_event(event_name)

    def render(self):
        # First: get the RenderedObject arguments:
        arguments = self.extend_properties({})

        # The rendered items of the box
        rendered_items = []

        # Render this block and return
        result = UI.RenderedObject(
            tag_name = "entry",
            properties = arguments,
            inner_content = rendered_items
        )
        return result
