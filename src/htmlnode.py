

class HTMLNode:
    def __init__(self, tag, value, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        final = f"<{self.tag}>"
        for child in self.children:
            final += child.to_html()

        final += f"</{self.tag}>"
        final = final.replace('\n', ' ')
        return final

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




class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("leafnode must have a value (empty string allowed)")

        if self.tag is None:
            return self.value

        if self.props is not None:
            return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"
        
        return f"<{self.tag}>{self.value}</{self.tag}>"




class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("parent must have a tag")

        if self.children is None:
            raise ValueError("children are not present")

        html = f"<{self.tag}>"
        for child in self.children:
            html += f"{child.to_html()}"

        html += f"</{self.tag}>"
        return html


















































