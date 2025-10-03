
def markdown_to_blocks(text):
    blocks = []
    tmp = text.split("\n\n")
    
    for block in tmp:
        if block is "":
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
    pass
