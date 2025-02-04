def markdown_to_blocks_hard_way(markdown):
    new_block = []
    
    split_markdown = markdown.split("\n\n", 1)
    while len(split_markdown) == 2:
        if (split_markdown[0]==""):
            split_markdown = split_markdown[1].split("\n\n", 1)
            continue
        text = split_markdown[0].strip()
        new_block.append(text)
        split_markdown = split_markdown[1].split("\n\n", 1)
    if  (split_markdown[0]!=""):
        text = split_markdown[0].strip()
        new_block.append(text)
    return new_block    

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks