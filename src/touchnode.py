from enum import Enum
from importlib.resources import contents
from pip._vendor.urllib3.util import Url

class TextType(Enum):
    NORMAL_TEXT = 'normal'
    BOLD_TEXT = '**text**'
    ITALIC_TEXT = '_text_'
    CODE_TEXT = '```code```'
    LINKS = '[link text](link address)'
    IMAGES = '![alt text](image address)'

class TextNode(self, text, T, url):
    self.text = text
    self.text_type = TextType
    self.url = Url

    def __eg__():
        pass

    def __repr__():
        return TextNode(TEXT, TEXT_TYPE, URL)
