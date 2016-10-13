#!/usr/bin/env python
# encoding: utf-8

"""Provides the RenderedObject class.

The RenderedObject class is the result of the render of a Component, and is
XML-based (not necessary HTML).
"""

__author__ = "Alejandro Linarez"
__copyright__ = "Anton Danilchenko"
__credits__ = ["Anton Danilchenko", "Alejandro Linarez"]

__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Alejandro Linarez"
# __email__ = ""
__status__ = "Development"

class RenderedObject:
    """Represents the result of render a component.

    This class can be exported to XML and XHTML.
    """

    def __init__(self, **kwargs):
        """Creates the new RenderedObject from the keywords arguments.

        The arguments should containt these values:

        * \"tagName\": A string containing the XML tag name (should be valid).
        * \"properties\": A dictionary containing the XML attributes.
        * \"innerContent\": A list of strings or RenderedObject. If an item is
          a string, it's parsed as a XML TextNode, if is a RenderedObject,
          is rendered to XML instead.
        """
        self._props = kwargs
        self._tagName = self._tryToAccess("tagName")
        self._properties = self._tryToAccess("properties")
        self._innerContent = self._tryToAccess("innerContent")

        # Type checks
        if type(self._tagName) != str:
            raise ValueError("The tagName attribute should be a string")
        if type(self._properties) != dict:
            raise ValueError("The properties attribute should be a dictionary")
        if type(self._innerContent) != list:
            raise ValueError("the innerContent attribute should be a list")

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

    def toXMLString(self):
        """Exports this object to a XML string.

        Returns an XML ready-to-parse string representing this
        RenderedObject.
        """
        xmlstr = "<" + self._tagName + " "
        for key, value in self._properties.items():
            xmlstr += key + "=\"" + str(value) + "\" "
        if len(self._innerContent) == 0:
            xmlstr += "/>"
            return xmlstr
        xmlstr += ">"
        for child in self._innerContent:
            if type(child) == str:
                xmlstr += child
            elif type(child) == RenderedObject:
                xmlstr += child.toXMLString()
            else:
                xmlstr += str(child)
        xmlstr += "</" + self._tagName + ">"
        return xmlstr

    def __str__(self):
        """Converts this object to an string.

        Returns a minimalist representation of this object (not XML valid).

        Like toXMLString, but never renders the RenderedObject childrens.
        """
        xmlstr = "<" + self._tagName + " "
        for key, value in self._properties.items():
            xmlstr += key + "=\"" + str(value) + "\" "
        if len(self._innerContent) == 0:
            xmlstr += "/>"
            return xmlstr
        xmlstr += ">"
        if len(self._innerContent) > 0:
            xmlstr += "<...>"
        xmlstr += "</" + self._tagName + ">"
        return xmlstr
