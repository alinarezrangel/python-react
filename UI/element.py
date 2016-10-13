#!/usr/bin/env python
# encoding: utf-8

"""Provides the Element class, the main class for all UI elements.

An Element is any UI element, these can have events, layouts, etc.
"""

from .renderedobject import *

__author__ = "Alejandro Linarez"
__copyright__ = "Anton Danilchenko"
__credits__ = ["Anton Danilchenko", "Alejandro Linarez"]

__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Alejandro Linarez"
# __email__ = ""
__status__ = "Development"

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
        pass

    def render(self):
        """Renders the current Element.

        It's important override this method when inherits Element.
        This method should return a RenderedObject
        """
        # The Component is abstract, so we can't render it
        return NullNode

def get_all_elements():
    """Returns a set containing all subclasses of the Element class.

    With the subclasses set, you tag associate the class name with a tag name.
    """
    subclasses = set()
    subclasses.add(Element);
    work = [Element]
    while work:
        parent = work.pop()
        for child in parent.__subclasses__():
            if child not in subclasses:
                subclasses.add(child)
                work.append(child)
    return subclasses
