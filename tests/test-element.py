#!/usr/bin/env python3
# encoding: utf-8

from PythonReact import UI, engines

b1 = UI.Button(label = "Button 1", style = ["button"])
b2 = UI.Button(label = "Button 2", style = ["button", "padding-4"])
b3 = UI.Button(label = "Button 3", style = ["button", "padding-32"])
b4 = UI.Button(label = "Button 4", style = ["button"])
b5 = UI.Button(label = "Button 5", style = ["button", "padding-16"])

c1 = UI.Container(items=[b1, b2], style = ["container"])
c2 = UI.Container(items=[b3], style = ["container"])
c3 = UI.Container(items=[b4, b5], style = ["container"])
c4 = UI.Container(items=[c1, c3], style = ["container"])

root = UI.Container(items=[c2, c4])

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
