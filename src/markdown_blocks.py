import re 

from htmlnode import *
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"

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

def block_to_block_type(block_markdown):

    if validate_headings(block_markdown):
        return block_type_heading
    if validate_code(block_markdown):
        return block_type_code
    if validate_quote(block_markdown):
        return block_type_quote
    if validate_unordered_list(block_markdown):
        return block_type_ulist
    if validate_ordered_list(block_markdown):
        return block_type_olist
    return block_type_paragraph

def validate_headings(word):
    p = re.compile(r'#{1,6} [\s\S]{1,}')
    return p.match(word)

def validate_code(word):
    p = re.compile(r"^```[\s\S]*?```$")
    return p.match(word)

def validate_quote(word):
    split_lines = word.split("\n")
    for line in split_lines:
        if ( not line.startswith("> ")):
            return False
    return True

def validate_unordered_list(word):
    split_lines = word.split("\n")
    for line in split_lines:
        if ( not line.startswith("- ") and not line.startswith("* ")):
            return False
    return True

def validate_ordered_list(word):
    split_lines = word.split("\n")
    count  = 1
    for line in split_lines:
        if ( not line.startswith(f"{count}. ")):
            return False
        count+=1
    return True

def markdown_to_html_node(markdown):
    markdown_blocks = markdown_to_blocks(markdown)
    children = []
    for block in markdown_blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)

def block_to_html_node(block):   
    type = block_to_block_type(block)
    match(type):
        case "heading":
            return handle_heading(block) 
        case "code":
            return handle_code(block)
        case "quote":
            return handle_quote(block)
        case "ordered_list":
            return handle_olist(block)
        case "unordered_list":
            return handle_ulist(block)
        case "paragraph":
            return handle_paragraph(block)
        case _:
            raise Exception("invalid block type")
     

def handle_heading(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError(f"invalid heading level: {level}")
    text = block[level + 1 :]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)
    
def handle_paragraph(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    tag = "p"
    children = text_to_children(paragraph)
    return ParentNode(tag, children)

def handle_quote(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children


def handle_code(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("invalid code block")
    text = block[4:-3]
    children = text_to_children(text)
    tag = "pre"
    code_node = ParentNode(tag="code", value=children)
    return ParentNode(tag,[code_node])

def handle_ulist(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)

def handle_olist(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)

def extract_title(markdown):
    blocks =  markdown_to_blocks(markdown)
    for block in blocks:
        type = block_to_block_type(block)
        if(type == block_type_heading):
            if block.startswith("# "):
                return block.lstrip("# ").strip()
    raise Exception("there is not a h1 header")