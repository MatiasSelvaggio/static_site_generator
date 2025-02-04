from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i %2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))                    
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches


def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        images = extract_markdown_images(old_node.text)

        if not images:
            new_nodes.append(old_node)
            continue
        
        current_text = old_node.text
        split_nodes = []
        for alt_text, url in images:
            image_markdown = f"![{alt_text}]({url})"
            parts = current_text.split(image_markdown, 1)
            if(parts[0] != ""):
                split_nodes.append(TextNode(parts[0], TextType.TEXT))
            split_nodes.append(TextNode(alt_text,TextType.IMAGE, url))
            current_text = parts[1]
        if current_text != "":
             split_nodes.append(TextNode(current_text, TextType.TEXT))
        new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        links = extract_markdown_links(old_node.text)

        if not links:
            new_nodes.append(old_node)
            continue

        current_text = old_node.text
        split_nodes = []
        for text, url in links:
            image_markdown = f"[{text}]({url})"
            parts = current_text.split(image_markdown, 1)
            if(parts[0] != ""):
                split_nodes.append(TextNode(parts[0], TextType.TEXT))
            split_nodes.append(TextNode(text,TextType.LINK, url))
            current_text = parts[1]
        if current_text != "":
             split_nodes.append(TextNode(current_text, TextType.TEXT))
        new_nodes.extend(split_nodes)
    return new_nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes