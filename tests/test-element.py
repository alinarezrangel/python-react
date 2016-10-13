import UI

class Button(UI.Element):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.args = kwargs

        # We can use super().args().get(key) and is
        # not needed save the kwargs in a variable
        self.label = self.args.get("label")

        if type(self.label) != str:
            raise TypeError('The button label is not a string')

    def render(self):
        res = UI.renderedobject.RenderedObject(
            tagName = "button",
            properties = {
                "type": "button",
                "class": "button"
            },
            innerContent = [
                self.label
            ]
        )
        return res

btn = Button(label="Hello World")
print(btn.render().toXMLString())
print(UI.get_all_elements())
