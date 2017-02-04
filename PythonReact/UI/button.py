#!/usr/bin/env python3
# encoding: utf-8

"""Provides the Button container, a clickeable element.

The Button element is one of the most simple and minimal user-interaction
methods, the button can be clicked to send one event (the "click" event).
"""

from PythonReact import UI

class Button(UI.Container):
    """Represents the Button container, a simple input method.

    The Button is a container (and not an element) because you can
    add images, text tags and others to a button.
    """

    def __init__(self, *args, **kwargs):
        """Creates the new Button.

        The optional arguments are:

        * "label": If the button contains only a text (a label), this
        attribute sets it's textual value.
        * "onclick" (also see Button.set_click_event): The callback that
        will be called when the button is pressed.
        * "type": The type of the button, "button" if not specified.
        * "href" (if "type" is "link"): HyperReference (URI/URL) to the
        resource.

        The button type can be:

        * "button": A button.
        * "submit": A button that submits a form (only works inside a form).
        * "reset": A button that reset the forms entries to their default values
        (only works inside a form).

        NOTE: A button without href (type is not "link") will have an href of
        "#". It's like an element without name will have a name of "".
        """
        super().__init__(*args, **kwargs)

        # Get the arguments or, it's default values
        self._label = super().register_argument("label", "")
        self._onclick = super().register_argument("onclick", None)
        self._type = super().register_argument("type", "button")
        self._href = super().register_argument("href", "#")

    def extend_properties(self, arguments):
        """Overload of UI.Container.extend_properties"""

        arguments = super().extend_properties(arguments)

        arguments["type"] = self._type
        arguments["onclick"] = self._onclick
        arguments["href"] = self._href

        return arguments

    def set_click_event(self, onclick):
        """Sets the button's onclick event."""
        self._onclick = onclick

    def emit_click_event(self, *args, **kwargs):
        """Calls the button's onclick event"""
        return self._onclick(*args, **kwargs)

    def emit(self, event_name, *args, **kwargs):
        """Override of UI.Element.emit"""
        if event_name == UI.EVENT_NAME_CLICK:
            return self.emit_click_event(*args, **kwargs)

        return super().emit(event_name, *args, **kwargs)

    def have_event(self, event_name):
        """Override of UI.Element.have_event"""
        if event_name == UI.EVENT_NAME_CLICK:
            return self._onclick is not None

        return super().have_event(event_name)

    def render(self):
        # First: get the RenderedObject arguments:
        arguments = self.extend_properties({})

        # The rendered items of the box
        rendered_items = [self._label] + super().get_rendered_items()

        # Render this block and return
        result = UI.RenderedObject(
            tag_name = "button",
            properties = arguments,
            inner_content = rendered_items
        )
        return result
