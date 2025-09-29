

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError


    def props_to_html(self):

        if self.props == None:
            return ""
        
        keys = self.props.keys()

        str = ""
        for key in keys:
            str += f" {key}=\"{self.props[key]}\""

        return str

    def __repr__(self):
        return f"HtmlNode({self.tag}, {self.value}, {self.children}, {self.props}"
