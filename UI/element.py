#!/usr/bin/env python
# encoding: utf-8

"""Provides the Element class, the main class for all UI elements.

An Element is any UI element, these can have events, layouts, etc.
"""

from .renderedobject import *

class Element:
    """Represents an Element, the basic UI element.

    Is very important override the render method when
    extends/inherits this class. When a new class is
    declared, it's tag name is saved in the global
    dictionary ElementsTagsNames.
    """

    # Only accepts keyword arguments because they are more semantic
    # than normal list arguments
    def __init__(self):
        """Creates a new Element, by default, null.

        The arguments keywords object is implemented in sub-classes,
        in this Element class, can be void.
        """
        self._styles = []

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
        except ValueError as err:
            return False
        else:
            return True

    def have_class(self, class_):
        """Returns True if the element have the class \"class_\""""
        try:
            # list.index raises a ValueError if the searched element
            # is not in the list
            self._styles.index(str(class_))
        except ValueError as err:
            return False
        else:
            return True

    def class_list(self):
        """Returns the elements's style classes list"""
        return self._styles

    def set_class_list(self, lst):
        """Sets the element's style classes to lst (a list)"""
        if type(lst) != list:
            raise TypeError("The ClassList should be a list")
        self._styles = lst

    def render(self):
        """Renders the current Element.

        It's important override this method when inherits Element.
        This method should return a RenderedObject
        """
        # The Component is abstract, so we can't render it
        return NULL_NODE

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
