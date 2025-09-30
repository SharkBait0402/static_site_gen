import re
from textnode import TextNode, TextType, text_node_to_html


bold_node = TextNode("This is text with a `code block` word", TextType.TEXT)

def split_delimiter(old_nodes, delimiter, text_type):

    #print(split_node)
    nodes = []

    for node in old_nodes:

        split_node = node.text.split(delimiter)
        if node.type is TextType.TEXT:
            for text in split_node:
                #print(text)
                if text == "":
                    break
                if text.startswith(" ") or text.endswith(" "):
                    nodes.append(TextNode(text, TextType.TEXT))

                elif not text.startswith(" ") and not text.endswith(" "):
                    nodes.append(TextNode(text, text_type))
        else:
            nodes.append(node)

    return nodes


def extract_markdown_images(text):
    images = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return images

def extract_markdown_links(text):
    links = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return links

def split_nodes_link(old_nodes):
    nodes = []

    for node in old_nodes:

        print(extract_markdown_links(node.text))
        split_node = node.text.split(extract_markdown_links(node.text)[0])
        if node.type is TextType.TEXT:
            for text in split_node:
                #print(text)
                if text == "":
                    break
                if text.startswith(" ") or text.endswith(" "):
                    nodes.append(TextNode(text, TextType.TEXT))

                elif not text.startswith(" ") and not text.endswith(" "):
                    nodes.append(TextNode(text, TextType.LINK))
        else:
            nodes.append(node)

    return nodes

def split_nodes_image(old_nodes):
    nodes = []

    for node in old_nodes:

        split_node = node.text.split(extract_markdown_images(node.text))
        if node.type is TextType.TEXT:
            for text in split_node:
                #print(text)
                if text == "":
                    break
                if text.startswith(" ") or text.endswith(" "):
                    nodes.append(TextNode(text, TextType.TEXT))

                elif not text.startswith(" ") and not text.endswith(" "):
                    nodes.append(TextNode(text, TextType.IMG))
        else:
            nodes.append(node)

    return nodes

