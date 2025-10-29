from enum import Enum
from htmlnode import LeafNode

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
        self.url_exist = False
        if url != None:
            self.url_exist = True
            self.url = url

    def __eq__(self, node):
        
        if self.url_exist:
            if self.text == node.text and self.type == node.type and self.url == node.url:
                return True
        elif self.text == node.text and self.type == node.type:
            return True

        return False

    def __repr__(self):
        if self.url_exist:
            return f"TextNode({self.text}, {self.type}, {self.url})"
        return f"TextNode({self.text}, {self.type})"



def text_node_to_html(node):
    if node.type is TextType.TEXT:
        return LeafNode(None, node.text)

    if node.type is TextType.BOLD:
        return LeafNode("b", node.text)   

    if node.type is TextType.ITALIC:
        return LeafNode("i", node.text)   

    if node.type is TextType.CODE:
        return LeafNode("code", node.text)   

    if node.type is TextType.LINK:
        return LeafNode("a", node.text, {"href": node.url})   

    if node.type is TextType.IMG:
        src = ""
        if node.url_exist:
            src = node.url
        return LeafNode("img", "", {"src": src, "alt": node.text})   








