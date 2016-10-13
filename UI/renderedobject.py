#!/usr/bin/env python
# encoding: utf-8

"""Provides the RenderedObject class.

The RenderedObject class is the result of the render of a Component, and is
XML-based (not necessary HTML).

The NullNode object represents the result of render an object that is not
renderizable, or it can not be rendered.
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

    def __init__(self, *args, **kwargs):
        """Creates the new RenderedObject from the keywords arguments.

        The arguments should containt these values:

        * \"tagName\": A string containing the XML tag name (should be valid).
        * \"properties\": A dictionary containing the XML attributes.
        * \"innerContent\": A list of strings or RenderedObject. If an item is
          a string, it's parsed as a XML TextNode, if is a RenderedObject,
          is rendered to XML instead.
        """
        self._props = kwargs # Object with all passed properties
        # Try to get the needed attributes:
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
        # dict.get returns None when the key not exist
        result = self._props.get(key)
        if result is None:
            raise KeyError("The key " + key + " is required")
        return result

    def toXMLString(self):
        """Exports this object to a XML string.

        Returns an XML ready-to-parse string representing this
        RenderedObject.
        """
        # First: the <tagName
        xmlstr = "<" + self._tagName + " "
        # For all properties, translate it to a string of the form
        # propertyName=propertyValue and append it to the xmlstr
        for key, value in self._properties.items():
            xmlstr += key + "=\"" + str(value) + "\" "
        # If not have childs (innerContent) return a tag of the form
        # <tagName attributes... /> instead of <tagName attributes...></tagName>
        if len(self._innerContent) == 0:
            xmlstr += "/>"
            return xmlstr
        # If have childs (innerContent) then:
        # Close the start tag
        xmlstr += ">"
        # Iterate over the childrens and stringify them
        for child in self._innerContent:
            if type(child) == str:
                xmlstr += child
            elif type(child) == RenderedObject:
                xmlstr += child.toXMLString()
            else:
                xmlstr += str(child)
        # And close the end tag
        xmlstr += "</" + self._tagName + ">"
        return xmlstr

    def __str__(self):
        """Converts this object to an string.

        Returns a minimalist representation of this object (not XML valid).

        Like toXMLString, but never renders the RenderedObject childrens.
        """
        # Opens the tag (<tagName)
        xmlstr = "<" + self._tagName + " "
        # Add the XML properties
        for key, value in self._properties.items():
            xmlstr += key + "=\"" + str(value) + "\" "
        # If not have childs, close the tag using />
        if len(self._innerContent) == 0:
            xmlstr += "/>"
            return xmlstr
        # If have childs, only display "<...>" for save space
        xmlstr += ">"
        if len(self._innerContent) > 0:
            xmlstr += "<...>"
        xmlstr += "</" + self._tagName + ">"
        return xmlstr

    def innerContent(self):
        """Returns a list of the child elements of this object"""
        return self._innerContent

    def properties(self):
        """Returns a dictionary of all attributes of this object"""
        return self._properties

    def tagName(self):
        """Returns the object's tag name as a string"""
        return self._tagName

# The NullNode is explained at the start of the file
NullNode = RenderedObject(
    tagName = "#Null",
    properties = {},
    innerContent = []
)
