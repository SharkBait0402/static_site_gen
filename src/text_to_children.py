from htmlnode import HTMLNode
from markdown import text_to_text_nodes
from textnode import text_node_to_html

def text_to_children(text):
    children = []
    nodes = text_to_text_nodes(text)
    for node in nodes:
        children.append(text_node_to_html(node))

    return children
