#!/usr/bin/env python
# encoding: utf-8

"""Provides the RenderedObject class.

The RenderedObject class is the result of the render of a Component, and is
XML-based (not necessary HTML).

The NULL_NODE object represents the result of render an object that is not
renderizable, or it can not be rendered.
"""

class RenderedObject:
    """Represents the result of render a component.

    This class can be exported to XML and XHTML.
    """

    def __init__(self, *args, **kwargs):
        """Creates the new RenderedObject from the keywords arguments.

        The arguments should containt these values:

        * \"tag_name\": A string containing the XML tag name (should be valid).
        * \"properties\": A dictionary containing the XML attributes.
        * \"inner_content\": A list of strings or RenderedObject. If an item is
          a string, it's parsed as a XML TextNode, if is a RenderedObject,
          is rendered to XML instead.
        """
        self._props = kwargs # Object with all passed properties
        # Try to get the needed attributes:
        self._tag_name = self._try_to_access("tag_name")
        self._properties = self._try_to_access("properties")
        self._inner_content = self._try_to_access("inner_content")

        # Type checks
        if type(self._tag_name) != str:
            raise ValueError("The tag_name attribute should be a string")
        if type(self._properties) != dict:
            raise ValueError("The properties attribute should be a dictionary")
        if type(self._inner_content) != list:
            raise ValueError("the inner_content attribute should be a list")

    def _try_to_access(self, key):
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

    def to_xml_string(self):
        """Exports this object to a XML string.

        Returns an XML ready-to-parse string representing this
        RenderedObject.
        """
        # First: the <tagName
        xmlstr = "<" + self._tag_name + " "
        # For all properties, translate it to a string of the form
        # propertyName=propertyValue and append it to the xmlstr
        for key, value in self._properties.items():
            xmlstr += key + "=\"" + str(value) + "\" "
        # If not have childs (innerContent) return a tag of the form
        # <tagName attributes... /> instead of <tagName attributes...></tagName>
        if len(self._inner_content) == 0:
            xmlstr += "/>"
            return xmlstr
        # If have childs (innerContent) then:
        # Close the start tag
        xmlstr += ">"
        # Iterate over the childrens and stringify them
        for child in self._inner_content:
            if type(child) == str:
                xmlstr += child
            elif type(child) == RenderedObject:
                xmlstr += child.to_xml_string()
            else:
                xmlstr += str(child)
        # And close the end tag
        xmlstr += "</" + self._tag_name + ">"
        return xmlstr

    def __str__(self):
        """Converts this object to a string.

        Returns a minimalist representation of this object (not XML valid).

        Like to_xml_string, but never renders the RenderedObject childrens.
        """
        # Opens the tag (<tagName)
        xmlstr = "<" + self._tag_name + " "
        # Add the XML properties
        for key, value in self._properties.items():
            xmlstr += key + "=\"" + str(value) + "\" "
        # If not have childs, close the tag using />
        if len(self._inner_content) == 0:
            xmlstr += "/>"
            return xmlstr
        # If have childs, only display "<...>" for save space
        xmlstr += ">"
        if len(self._inner_content) > 0:
            xmlstr += "<...>"
        xmlstr += "</" + self._tag_name + ">"
        return xmlstr

    def to_tree_string(self, indentchar = "    "):
        """Converts this object to a string.

        The difference between to_xml_string and to_tree_string is that
        toTreeString returns a Tree-based representation, instead of
        a ready-to-parse XML string.
        """
        # The format of the TreeString is:
        #    tagName(attributes):
        #        childs....
        # Starts with the tagName:
        treestr = self._tag_name + " ("
        # Append all attributes using the key="value" format:
        for key, value in self._properties.items():
            treestr += key + "=\"" + str(value) + "\" "
        # Close the parentesis of the attributes
        treestr += ")"
        # If not have childs, return the string
        if len(self._inner_content) == 0:
            return treestr
        # Else, append a colon
        treestr += ":"
        # And start to iterate over the childs
        for child in self._inner_content:
            # If we append the newline at the start of the loop,
            # we can avoid trailing newlines
            treestr += "\n"
            # Now, stringify the child (like toXMLString):
            if type(child) == str:
                treestr += indentchar + "\"" + child + "\""
            elif type(child) == RenderedObject:
                treestr += indentchar + child.to_tree_string(indentchar * 2)
            else:
                treestr += indentchar + str(child)
        # Done (return)
        return treestr

    def inner_content(self):
        """Returns a list of the child elements of this object"""
        return self._inner_content

    def properties(self):
        """Returns a dictionary of all attributes of this object"""
        return self._properties

    def tag_name(self):
        """Returns the object's tag name as a string"""
        return self._tag_name

# The NULL_NODE is explained at the start of the file
NULL_NODE = RenderedObject(
    tag_name = "None",
    properties = {},
    inner_content = []
)
