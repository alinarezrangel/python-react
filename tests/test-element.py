import UI
import engines.html

class Button(UI.Container):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # We can use super().args().get(key) and is
        # not needed save the kwargs in a variable
        self.label = super().register_argument("label", "")

        if type(self.label) != str:
            raise TypeError('The button label is not a string')

        super().add(self.label)

    def render(self):
        args = super().extend_properties({})
        args["type"] = "button"

        res = UI.renderedobject.RenderedObject(
            tag_name = "button",
            properties = args,
            inner_content = super().get_items()
        )
        return res

b1 = Button(label="Button 1")
b2 = Button(label="Button 2")
b3 = Button(label="Button 3")
b4 = Button(label="Button 4")
b5 = Button(label="Button 5")

c1 = UI.Container(items=[b1, b2])
c2 = UI.Container(items=[b3])
c3 = UI.Container(items=[b4, b5])
c4 = UI.Container(items=[c1, c3])

root = UI.Container(items=[c2, c4])

print(engines.html.TreeToHTML().convert_node(root.render(), {"iform": False}).to_xml_string())
