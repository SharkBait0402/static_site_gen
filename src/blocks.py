from enum import Enum
from htmlnode import HTMLNode
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

    if block.startswith("#"):
        return BlockType.H

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

    for block in blocks:
        type = block_to_block_type(block)
        new_node = None

        if type == BlockType.P:
            new_node = HTMLNode("p", block, text_to_children(block))
        elif type == BlockType.H:
            new_node = HTMLNode("h", block, text_to_children(block))
        elif type == BlockType.QUOTE:
            new_node = HTMLNode("p", block, text_to_children(block))
        elif type == BlockType.UL:
            new_node = HTMLNode("p", block, text_to_children(block))
        elif type == BlockType.OL:
            new_node = HTMLNode("p", block, text_to_children(block))
        elif type == BlockType.CODE:
            new_node = None #create text node and ignore children
    
        #TODO:I need to find a way to add the children to a parent node and print it out as one html file... have it printing one block good for now need it to combine them


        return new_node
