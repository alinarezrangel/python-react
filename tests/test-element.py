#!/usr/bin/env python3
# encoding: utf-8

from PythonReact import UI, engines

l1 = UI.Link(label = "First row", href = "#", style = ["link"])
l2 = UI.Label(style = ["label"])
l3 = UI.Label(label = "Third row", style = ["label"])

l2_text = UI.TextTag(type = UI.TextTag.TEXT_TAG_BOLD)
l2_text.mix(UI.TextTag(text = "Second row", type = UI.TextTag.TEXT_TAG_BIG))

l2.add(l2_text)

b1 = UI.Button(label = "Button 1", type = "link", href = "#b1", style = ["button"])
b2 = UI.Button(label = "Button 2", style = ["button", "padding-4"])
b3 = UI.Button(label = "Button 3", style = ["button", "padding-32"])
b4 = UI.Button(label = "Button 4", name="b1", style = ["button"])
b5 = UI.Button(label = "Button 5", style = ["button", "padding-16"])

s1 = UI.Separator(style = ["separator"])

v1 = UI.TextView(style = ["textview"])
v1.add_text("Title!", UI.TextView.TEXT_VIEW_HEADING_TITLE)
v1.add_text(" normal    text", UI.TextView.TEXT_VIEW_NORMAL)
v1.add_text(" raw    text", UI.TextView.TEXT_VIEW_RAW)
v1.add_text(" code    text", UI.TextView.TEXT_VIEW_CODE)

c1 = UI.Container(items=[l2, b1, b2], style = ["container"])
c2 = UI.Container(items=[l1, b3], style = ["container"])
c3 = UI.Container(items=[l3, b4, b5], style = ["container"])
c4 = UI.Container(items=[c1, c3], style = ["container"])

root = UI.Container(items=[c2, c4, s1, v1])

# Basic HTML with some CSS template.
# Uses the test.css file

html_out = """<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />

        <title>Elements test</title>

        <link href="test.css" rel="stylesheet" type="text/css" />
    </head>
    <body>
        {0}
    </body>
</html>
""".format(engines.html.TreeToHTML().toHTML(root.render()))

print(html_out)
