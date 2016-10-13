#!/usr/bin/env python3
# encoding: utf-8

"""Provides the TreeToHTML class.

This class converts a RenderedObject tree to a HTML ready-to-parse string.

Not all RenderedObject tags can be used, the recognized tags are:

* `container`: Converted to a `div`.
* `row`: Converted to a `div (class=ROW_CLASS)`.
* `column`: Converted to a `div (class=COLUMN_CLASS)`.
* `button (type="link")`: Converted to `a (class=BUTTON_CLASS)`
* `button (type="button")`: Converted to `button (type="button")`
* `label (form=True)`: Converted to `label`
* `label (form=False)`: Converted to `span (class=LABEL_CLASS)`
* `paragraph`: Converted to `p`
* `text`: Converted to `div` with only `p` as childs
* `text-tag` (type=TYPE): Converted to `span`
* `link (href=HREF)`: Converted to `a (href=HREF)`
* `form (act=ACTION method=MTH)`: Converted to `form (action=ACTION method=MTH)`
* `frame (title=TTL)`: Converted to `fieldset` if inside a form or styled `div`
otherwise.
* `image`: Converted to `img`
* `block`: Converted to `div`
* `separator`: Converted to `hr`
* `line-entry`: Converted to `input (type="text")`
* `text-entry`: Converted to `textarea`
* `password-entry`: Converted to `input (type="password")`
* `file-entry`: Converted to `input (type="file")`
* `radio-button (group=GP)`: Converted to `input (type="radio" name=GP)`
* `check-button (group=GP)`: Converted to `input (type="check" name=GP)`
* `entry`: Converted to `input`
* `heading (level=L)`: Converted to `h L`
* `title`: Converted to `h1`
* `subtitle`: Converted to `h2`
* `sectiontitle`: Converted to `h3`
* `raw-text`: Converted to `pre`
* `code-text`: Converted to `code`

Others tags will be not parsed.
"""

from PythonReact import UI

class TreeToHTML:
    """The TreeToHTML class exports a AbstractTree to a HTML ready-to-parse
    string.
    """

    def __init__(self):
        """Construct a empty TreeToHTML parser."""

        self.tag_dict = {
            "container": "div",
            "row": "div",
            "column": "div",
            "text": "div",
            "block": "div",
            "raw-text": "pre",
            "code-text": "code",
            "paragraph": "p",
            "link": "a",
            "form": "form",
            "separator": "hr",
            "line-entry": "input",
            "text-entry": "textarea",
            "password-entry": "input",
            "file-entry": "input",
            "number-entry": "input",
            "hidden-entry": "input",
            "radio-button": "input",
            "check-button": "input",
            "entry": "input",
            "title": "h1",
            "subtitle": "h2",
            "sectiontitle": "h3",
            "image": "img"
        }

    def get_tag_name(self, tag_name):
        return self.tag_dict[tag_name]

    def convert_node(self, node, data):
        if isinstance(node, str):
            return node

        ntg = node.tag_name()
        pp = node.properties()
        class_list = pp.get("style", "")
        expp = {}

        if(ntg == "form"):
            data["iform"] = True;

        childs = [self.convert_node(i, data) for i in node.inner_content()]

        if(ntg == "form"):
            data["iform"] = False;

        if ntg == "button":
            if pp.get("type", "button") == "link":
                tag = "a"
                expp["href"] = pp.get("href", "#")
            else:
                tag = "button"
                expp["type"] = pp.get("type", "button")
        elif ntg == "label":
            if data["iform"]:
                tag = "label"
            else:
                tag = "span"
        elif ntg == "frame":
            if data["iform"]:
                tag = "fieldset"
                childs = [
                    UI.RenderedObject(
                        tag_name = "legend",
                        properties = {},
                        inner_content = [pp.get("title", "")]
                    )
                ] + childs
            else:
                tag = "div"
                childs = [
                    UI.RenderedObject(
                        tag_name = "div",
                        properties = {"align": "center"},
                        inner_content = [pp.get("title", "")]
                    )
                ] + childs
        elif ntg == "heading":
            tag = "h" + str(pp.get("level", "1"))
        elif ntg == "text-tag":
            if pp.get("type", "none") == "bold":
                tag = "b"
            elif pp.get("type", "none") == "italic":
                tag = "i"
            elif pp.get("type", "none") == "underline":
                tag = "u"
            elif pp.get("type", "none") == "strike":
                tag = "s"
            elif pp.get("type", "none") == "small":
                tag = "small"
            elif pp.get("type", "none") == "big":
                tag = "big"
            elif pp.get("type", "none") == "quote":
                tag = "q"
            elif pp.get("type", "none") == "subscript":
                tag = "sub"
            elif pp.get("type", "none") == "superscript":
                tag = "sup"
            elif pp.get("type", "none") == "custom":
                tag = "span"
            elif pp.get("type", "none") == "normal":
                tag = "span"
            elif pp.get("type", "none") == "link":
                tag = "a"
                expp["href"] = pp.get("href", "#")
            else:
                tag = "span"
        else:
            tag = self.get_tag_name(ntg)
            entry_type = False

            if ntg == "link":
                expp["href"] = pp.get("href", "#")
            elif (ntg == "button") and (pp.get("type", "button") == "link"):
                expp["href"] = pp.get("href", "#")
            elif ntg == "form":
                expp["action"] = pp.get("act", "#")
                expp["method"] = pp.get("method", "#")
            elif ntg == "line-entry":
                expp["type"] = "text"
                entry_type = True
            elif ntg == "password-entry":
                expp["type"] = "password"
                entry_type = True
            elif ntg == "file-entry":
                expp["type"] = "file"
                entry_type = True
            elif ntg == "number-entry":
                expp["type"] = "number"
                entry_type = True
            elif ntg == "hidden-entry":
                expp["type"] = "hidden"
                entry_type = True
            elif ntg == "radio-button":
                expp["type"] = "radio"
                entry_type = True
                if pp.get("group") is not None:
                    expp["name"] = pp.get("group")
            elif ntg == "check-button":
                expp["type"] = "checkbox"
                entry_type = True
                if pp.get("group") is not None:
                    expp["name"] = pp.get("group")
            elif ntg == "entry":
                entry_type = True
            elif ntg == "image":
                expp["width"] = pp.get("width")
                expp["height"] = pp.get("height")
                expp["alt"] = pp.get("alt")
                expp["title"] = pp.get("title")
                expp["src"] = node.inner_content()[0]
                childs = []

            if entry_type:
                if pp.get("form_name") is not None:
                    expp["name"] = pp.get("form_name")
                if pp.get("required") is not None:
                    expp["required"] = pp.get("required")
                if pp.get("placeholder") is not None:
                    expp["placeholder"] = pp.get("placeholder")

        if (pp.get("style") is not None) and (pp.get("style").strip() != ""):
            expp["class"] = class_list

        if (pp.get("name") is not None) and (pp.get("name").strip() != ""):
            expp["id"] = pp.get("name")
        if (pp.get("css") is not None) and (pp.get("css").strip() != ""):
            expp["style"] = pp.get("css")

        return UI.RenderedObject(
            tag_name = tag,
            properties = expp,
            inner_content = childs
        )

    def toHTML(self, tree):
        return self.convert_node(tree, {"iform": False}).to_xml_string()
