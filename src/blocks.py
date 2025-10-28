from enum import Enum
from htmlnode import HTMLNode, ParentNode
from textnode import TextNode, text_node_to_html, TextType
from text_to_children import text_to_children

def markdown_to_blocks(text):
    blocks = []
    tmp = text.split("\n\n")
    
    for block in tmp:
        if block == "":
            continue
        blocks.append(block.strip())
    return blocks

class BlockType(Enum):
    P = "paragragh"
    H = "heading"
    CODE = "code"
    QUOTE = "quote"
    UL = "unordered list"
    OL = "ordered list"

def block_to_block_type(block):
    lines = block.split("\n")

    is_quote = True
    is_ul = True
    is_ol = True
    i = 1

    if '# ' in block:
        text = block.split('# ')
        num = len(text[0]) + 1
        if num <= 6:
            return BlockType.H
        else:
            return BlockType.P

    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE

    for line in lines:
        if not line.startswith(">"):
            is_quote = False
        if not line.startswith("- "):
            is_ul = False
        if not line.startswith(f"{i}. "):
            is_ol = False
        i += 1

    if is_quote:
        return BlockType.QUOTE
    if is_ul:
        return BlockType.UL
    if is_ol:
        return BlockType.OL
    return BlockType.P


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    new_nodes = []

    for block in blocks:

        if block == '':
            continue

        type = block_to_block_type(block)

        if type == BlockType.P:
            new_nodes.append(HTMLNode("p", block, text_to_children(block)))
        elif type == BlockType.H:
            text = block.split('# ')
            num = len(text[0]) + 1
            new_nodes.append(HTMLNode(f"h{num}", text[1], text_to_children(text[1])))
        elif type == BlockType.QUOTE:
            new_nodes.append(HTMLNode("blockquote", block, text_to_children(block)))
        elif type == BlockType.UL:
            new_nodes.append(HTMLNode("ul", block, text_to_children(block)))
        elif type == BlockType.OL:
            new_nodes.append(HTMLNode("ol", block, text_to_children(block)))
        elif type == BlockType.CODE:
            block = block.replace("```", "")
            if block.startswith("\n"):
                block = block[1::]
            code_node = TextNode(block, TextType.CODE)
            html = text_node_to_html(code_node)
            new_nodes.append(HTMLNode("pre", None, [html]))

    return ParentNode("div", new_nodes)

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block.startswith("# "):
            block = block[1::]
            return block.strip()
    raise Exception("no h1 in markdown")

