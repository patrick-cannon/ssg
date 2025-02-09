from enum import Enum

class TextType(Enum):
    NORMAL_TEXT = ""
    BOLD_TEXT = "**"
    ITALIC_TEXT = "_"
    CODE_TEXT = "`"
    LINKS = ""
    IMAGES = ""

class TextNode:
    def __init__(self, text, text_type, url):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, TextNode):
        return (self.text == TextNode.text and self.text_type == TextNode.text_type and self.url == TextNode.url)

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
