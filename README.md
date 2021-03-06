# Python implementation of ReactJS

In this project I will try to implement ReactJS solution of incapsulate UI and logic in one component. But will do it in **Python** language.

## Examples

```python
from PythonReact import UI, core


class LoginButton(UI.Element):

    def __init__(self, **kwargs):
        self.args = kwargs

    def render(self):
        btn = UI.Button(
            text=self.args.get('text', 'Login'),
            onclick=self.click,
            style='bs-button bs-button-success'
        )
        return btn.render()
    
    def click(self):
        self.active = False
        self.loadData('api/user/login', success=self.data_loaded)
    
    def data_loaded(self, data):
        self.active = True
        onclick = self.args.get('onclick')
        if onclick:
           onclick(self, data)
 
 
class TopToolbar(UI.Toolbar):

    def __init__(self):
        self.elements = []

    def render(self):
        logo = UI.Label('Website name')
        menu_items = UI.Block(
            items=[
                UI.Button(text='Home'),
                UI.Button(text='About'),
            ]
        )
        btn_login = LoginButton(onclick=self.login)
        self.add(logo, menu_items, btn_login)
        return super().render()
    
    def login(self, data):
        if data.get('success'):
            core.signal('reload-page')
```
