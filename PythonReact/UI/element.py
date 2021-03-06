#!/usr/bin/env python3
# encoding: utf-8

"""Provides the Element class, the main class for all UI elements.

An Element is any UI element, these can have events, layouts, etc.
"""

from PythonReact import UI

class Element:
    """Represents an Element, the basic UI element.

    Is very important override the render method when
    extends/inherits this class. When a new class is
    declared, it's tag name is saved in the global
    dictionary ElementsTagsNames.
    """

    # Only accepts keyword arguments because they are more semantic
    # than normal list arguments
    def __init__(self, *args, **kwargs):
        """Creates a new Element, by default, null.

        The arguments keywords object is implemented in sub-classes,
        in this Element class, can be void. The recognized keyword
        arguments are:

        * "style": A list of strings containing the element's class names.
        * "name": A string containing the element's name (or ID).
        """

        self._args = kwargs
        self._kargs = []
        self._styles = self.register_argument("style", [])
        self._name = self.register_argument("name", "")

    def register_argument(self, name, otherwise):
        """Gets and registers a keyword name.

        After register a keyword name, the protected_keyword_name
        function will return True for that name.

        Returns the value of name in self.args() or otherwise if is
        undefined.
        """

        if name not in self._kargs:
            self._kargs.append(name)

        return self.args().get(name, otherwise)

    def protected_keyword_name(self, name):
        """Determines if a keyword name 'name' is used on the constructor.

        Returns True if the keyword 'name' is utilized in the constructor.
        """
        return name in self._kargs

    def class_list_as_css_string(self):
        """Gets the class list as a CSS list.

        Returns a list with all element's class names separated by spaces.
        """

        # style argument is the class list
        css = ""

        # The super().classList() is a list, but we need a CSS-like string:
        for class_ in self.class_list():
            css += " " + str(class_)

        return css[1:]

    def extend_properties(self, arguments):
        """Returns a modified version of arguments with all properties.

        Each element have it's own properties to be passed to the RenderedObject
        constructor. This method receives an arguments dictionary with some
        properties to be passed and adds it's owns. This method should be
        overrided for all Element's subclasses.

        Returns the version of arguments with new properties.
        """

        arguments["style"] = self.class_list_as_css_string()
        arguments["name"] = self.get_name()

        return arguments

    def args(self):
        """Gets the constructor keyword arguments.

        Returns the dictionary with all keyword arguments.
        """
        return self._args

    def add_class(self, class_):
        """Adds a new class style to this element"""
        self._styles.append(str(class_))

    def remove_class(self, class_):
        """Removes a class from the class style of this element

        Returns True if the class was successfull removed.
        """
        try:
            # list.remove raises a ValueError if the removed element
            # is not in the list
            self._styles.remove(str(class_))
        except ValueError:
            return False
        else:
            return True

    def have_class(self, class_):
        """Returns True if the element have the class \"class_\""""
        try:
            # list.index raises a ValueError if the searched element
            # is not in the list
            self._styles.index(str(class_))
        except ValueError:
            return False
        else:
            return True

    def class_list(self):
        """See get_class_list"""
        return self.get_class_list()

    def get_class_list(self):
        """Returns the elements's style classes list"""
        return self._styles

    def get_name(self):
        """Returns the element's name or ID"""
        return self._name

    def set_name(self, name):
        """Sets the element's name or ID"""
        self._name = name

    def set_class_list(self, lst):
        """Sets the element's style classes to lst (a list)"""
        self._styles = lst

    def render(self):
        """Renders the current Element.

        It's important override this method when inherits Element.
        This method should return a RenderedObject
        """
        # The Element is abstract, so we can't render it
        return UI.NULL_NODE

    def emit(self, event_name, *args, **kwargs):
        """Emits the event event_name to this element.

        args and kwargs will be passed to the handler (if any)
        and the handler's returned value will be returned too.

        If no handler is attached to this event, does nothing.

        See the attached handlers using the Element.have_event
        method.

        This method should be overrided for all elements that
        have events.
        """
        return None

    def have_event(self, event_name):
        """Returns True if this element have a handler attached
        to the event event_name.

        Returns False otherwise.
        """
        return False

def get_all_elements():
    """Returns a set containing all subclasses of the Element class.

    With the subclasses set, you tag associate the class name with a tag name.
    """
    # Set containing all subclasses
    subclasses = set()
    subclasses.add(Element);
    # Classes for inspect
    work = [Element]
    while work: # While have at least one class to inspect:
        parent = work.pop() # Select it
        # Iterate over it's direct subclasses (not subsubclasses):
        for child in parent.__subclasses__():
            if child not in subclasses: # If the class is not registered:
                subclasses.add(child) # Register it in the set
                work.append(child) # And select it for inspect.
                # If we not mark child for inspect, the subsubclasses
                # will not be registered
    return subclasses
