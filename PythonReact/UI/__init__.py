#!/usr/bin/env python3
# encoding: utf-8

"""The UI module provides the interface for interacting with the user.

The main two classes are RenderedObject and Element. The UI module
implements an abstract tree for manage the GUI, allowing to use
any GUI-frontend for display the GUI, like GTK, Qt, wxWidgets or
directly X.org, Mir or Wayland.
"""

from .renderedobject import *
from .events import *
from .element import *
from .container import *
from .button import *
from .label import *
from .texttag import *
