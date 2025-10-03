def markdown_to_blocks(text):
    blocks = []
    tmp = text.split("\n\n")
    
    for block in tmp:
        if block is "":
            continue
        blocks.append(block.strip())
    return blocks
