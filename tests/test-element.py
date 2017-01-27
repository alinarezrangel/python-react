from PythonReact import UI, engines

b1 = UI.Button(label="Button 1")
b2 = UI.Button(label="Button 2")
b3 = UI.Button(label="Button 3")
b4 = UI.Button(label="Button 4")
b5 = UI.Button(label="Button 5")

c1 = UI.Container(items=[b1, b2])
c2 = UI.Container(items=[b3])
c3 = UI.Container(items=[b4, b5])
c4 = UI.Container(items=[c1, c3])

root = UI.Container(items=[c2, c4])

print(engines.html.TreeToHTML().toHTML(root.render()))
