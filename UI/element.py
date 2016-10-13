#!/usr/bin/env python
# encoding: utf-8

"""Provides the Element class, the main class for all UI elements.

An Element is any UI element, these can have events, layouts, etc.

The ElementsTagsNames dictionary links a tag name with a class or
type. It's used by the main renderer for make new instances of the
classes when their tag is found.
"""

import renderedobject

__author__ = "Alejandro Linarez"
__copyright__ = "Anton Danilchenko"
__credits__ = ["Anton Danilchenko", "Alejandro Linarez"]

__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Alejandro Linarez"
# __email__ = ""
__status__ = "Development"

ElementsTagsNames = {}

def IElement(cls):
    """Decorator used when a new Element is created.

    When you inherits or extends Element, you should use this decorator
    for save your class in the main class dictionary (ElementsTagsNames).

    If is not used, the class will not be rendered using RenderedObject and
    RenderedObject-like classes.
    """
    global ElementsTagsNames

    # Get the class name as an string, using this, we can refer to
    # the class "Button" using the XML "<Button>"
    tagName = cls.__name__
    ElementsTagsNames[tagName] = cls

@IElement
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
        in this Element class, can be void.
        """
        self._props = kwargs
        # Get the class name as an string, using this, we can refer to
        # the class "Button" using the XML "<Button>"
        self._tagName = type(self).__name__

    def _tryToAccess(self, key):
        """Tries to access to a key in the self._props.

        key is a string containing the key name to access.

        This function returns the result.

        If fails, raises a KeyError.
        """
        result = self._props.get(key)
        if result is None:
            raise KeyError("The key " + key + " is required")
        return result

    def render(self):
        # The Component is abstract, so we can't render it
        return renderedobject.NullNode
