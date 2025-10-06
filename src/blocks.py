from enum import Enum

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
