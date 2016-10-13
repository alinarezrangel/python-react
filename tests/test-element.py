import UI

class Button(UI.Element):
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.args = kwargs

        # We can use super().args().get(key) and is
        # not needed save the kwargs in a variable
        self.label = self.args.get("label")

        if type(self.label) != str:
            raise TypeError('The button label is not a string')

    def render(self):
        res = UI.renderedobject.RenderedObject(
            tag_name = "button",
            properties = {
                "type": "button",
                "class": "button"
            },
            inner_content = [
                self.label
            ]
        )
        return res

b1 = Button(label="Button 1")
b2 = Button(label="Button 2")
b3 = Button(label="Button 3")
b4 = Button(label="Button 4")
b5 = Button(label="Button 5")

c1 = UI.Block(items=[b1, b2])
c2 = UI.Block(items=[b3])
c3 = UI.Block(items=[b4, b5])
c4 = UI.Block(items=[c1, c3])

root = UI.Block(items=[c2, c4])

print(root.render().to_tree_string())
print(UI.get_all_elements())
