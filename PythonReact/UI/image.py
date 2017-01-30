#!/usr/bin/env python3
# encoding: utf-8

"""Provides the Image element, a .

"""

from PythonReact import UI

class Image(UI.Element):
    """Represents the Image element, a display of graphical data.

    The Image element can display a graphical image with format
    specified in the rendering engine. Generally, the image data
    can not be generated at runtime and should be specified on a
    file.

    The image types are:

    IMAGE_TYPE_BASE64 - The image data is a base64 encoded string
    with the image content.
    IMAGE_TYPE_FILE - The image data is a path to a resource (a file)
    containing the image content.
    IMAGE_TYPE_HREF - The image data is a HyperReference (URI/URL) to
    a resource containing the image content.

    The image formats are:

    IMAGE_FORMAT_PNG - PNG image.
    IMAGE_FORMAT_SVG - SVG image.
    IMAGE_FORMAT_JPEG - JPEG image.
    IMAGE_FORMAT_AUTO - Automatic format detection.

    The usage are:

        img = UI.Image(fmt = UI.Image.IMAGE_TYPE_* + UI.Image.IMAGE_FORMAT_*)

    For example:

        UI.Image.IMAGE_TYPE_HREF + UI.Image.IMAGE_FORMAT_AUTO
        UI.Image.IMAGE_TYPE_BASE64 + UI.Image.IMAGE_FORMAT_PNG
        UI.Image.IMAGE_TYPE_FILE _ UI.Image.IMAGE_SVG
    """

    IMAGE_TYPE_BASE64 = "base64."
    IMAGE_TYPE_FILE = "file."
    IMAGE_TYPE_HREF = "href."
    IMAGE_FORMAT_PNG = "png"
    IMAGE_FORMAT_SVG = "svg"
    IMAGE_FORMAT_JPEG = "jpeg"
    IMAGE_FORMAT_AUTO = "auto"

    def __init__(self, *args, **kwargs):
        """Creates the new Image.

        The optional arguments are:

        * "alt": Alternative text to load if the engine can not
        display the image.
        * "title": Name of the image (may be displayed as a tooltip).
        * "data": The image data in the specified format.
        * "fmt": Image data type (one of the IMAGE_TYPE_* + IMAGE_FORMAT_*)
        default to "HREF+AUTO".
        * "width": Width of the image, see below.
        * "height": Height of the image, see below.

        The width and height of the image are specified in the format
        (where ? is the number):

        * "?px" Pixels (15px = 15 pixels)
        * "?em" Font Size (2em = 2 times the font size, e.g.
        1em = 16px => 2em = 32px)
        * "?%" Percent of the container geometry (15% = 15% of the
        container's width or height)
        * "expand" The image width/height is adjusted to the
        image data width/height.
        """
        super().__init__(*args, **kwargs)

        # Get the arguments or, it's default values
        self._alt = super().register_argument("alt", "")
        self._title = super().register_argument("title", "")
        self._data = super().register_argument("data", "")
        self._fmt = super().register_argument("fmt", "href.auto")
        self._width = super().register_argument("width", "expand")
        self._height = super().register_argument("height", "expand")

    def extend_properties(self, arguments):
        """Overload of UI.Container.extend_properties"""

        arguments = super().extend_properties(arguments)

        arguments["alt"] = self._alt
        arguments["title"] = self._title
        arguments["fmt"] = self._fmt
        arguments["width"] = self._width
        arguments["height"] = self._height

        return arguments

    def render(self):
        # First: get the RenderedObject arguments:
        arguments = self.extend_properties({})

        # The rendered items of the box
        rendered_items = [self._data]

        # Render this block and return
        result = UI.RenderedObject(
            tag_name = "image",
            properties = arguments,
            inner_content = rendered_items
        )
        return result
