#!/usr/bin/env python
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
* `text-tag`: Converted to `span`
* `link (to=HREF)`: Converted to `a (href=HREF)`
* `form (to=ACTION method=MTH)`: Converted to `form (action=ACTION method=MTH)`
* `frame (title=TTL)`: Converted to `fieldset` if inside a form or styled `div`
otherwise.
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

import UI

class TreeToHTML:
    """The TreeToHTML class exports a AbstractTree to a HTML ready-to-parse
    string.
    """

    def __init__(self):
        """Construct a empty TreeToHTML parser."""
        pass

    def toHTML(self, tree):
        #
