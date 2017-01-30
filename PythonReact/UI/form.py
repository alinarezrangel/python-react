#!/usr/bin/env python3
# encoding: utf-8

"""Provides the Frame container, a container with a title.

The Frame container is useful in forms, when you need to group
a set of entries in the same category.
"""

from PythonReact import UI

class Form(UI.Container):
    """Represents the Form container, a method for sending data
    across resources.

    All entries in this container will be submited to a resource
    when the engine emit the submit event. The submit action
    can be canceled returning False on the submit event handler.
    """

    def __init__(self, *args, **kwargs):
        """Creates the new Form.

        The optional arguments are:

        * "act": The HyperReference (URI/URL) to the resource that
        will handle the submited data (set to "" if the data will
        be handled on this resource).
        * "method": The HTTP (or protocol-based) method to be used
        for submit the data.
        * "onsubmit": Event handler used on the submit event.
        """
        super().__init__(*args, **kwargs)

        # Get the arguments or, it's default values
        self._act = super().register_argument("act", "")
        self._method = super().register_argument("method", "GET")
        self._onsubmit = super().register_argument("onsubmit", None)

    def extend_properties(self, arguments):
        """Overload of UI.Container.extend_properties"""

        arguments = super().extend_properties(arguments)

        arguments["act"] = self._act
        arguments["method"] = self._method

        return arguments

    def set_submit_event(self, onsubmit):
        """Sets the form's onsubmit event."""
        self._onsubmit = onsubmit

    def emit_submit_event(self, *args, **kwargs):
        """Calls the form's onsubmit event"""
        return self._onsubmit(*args, **kwargs)

    def emit(self, event_name, *args, **kwargs):
        """Override of UI.Element.emit"""
        if event_name == UI.EVENT_NAME_SUBMIT:
            return self.emit_onsubmit_event(*args, **kwargs)

        return super().emit(event_name, *args, **kwargs)

    def have_event(self, event_name):
        """Override of UI.Element.have_event"""
        if event_name == UI.EVENT_NAME_SUBMIT:
            return True

        return super().have_event(event_name)

    def render(self):
        # First: get the RenderedObject arguments:
        arguments = self.extend_properties({})

        # The rendered items of the box
        rendered_items = super().get_rendered_items()

        # Render this block and return
        result = UI.RenderedObject(
            tag_name = "form",
            properties = arguments,
            inner_content = rendered_items
        )
        return result
