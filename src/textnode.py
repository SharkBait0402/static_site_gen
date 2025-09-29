from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMG = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.type = text_type
        self.url = url

    def __eq__(self, node):
        if self.text == node.text and self.type == node.type and self.url == node.url:
            return True
        return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.type}, {self.url})"
