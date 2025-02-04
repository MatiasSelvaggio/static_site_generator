import shutil
import os

from markdown_blocks import (
    markdown_to_html_node,
    extract_title
    )

def copy_all(source, destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)

    os.mkdir(destination)

    list_dir = os.listdir(source)
    for item in list_dir:

        source_path = os.path.join(source, item)
        dest_path = os.path.join(destination, item)

        if ( os.path.isfile(source_path)):
            print(f"Copying file: {source_path} -> {dest_path}")
            shutil.copy(source_path, dest_path)

        else:
            print(f"Copying directory: {source_path} -> {dest_path}")
            copy_all(source_path, dest_path)

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    if not os.path.exists(from_path) and not os.path.isfile(from_path):
        raise Exception("invalid from path")
    if not os.path.exists(template_path) and not os.path.isfile(template_path):
        raise Exception("invalid template path")
    
    with open(from_path, 'r', encoding='utf-8') as f:
        from_file = f.read()
    with open(template_path, 'r', encoding='utf-8') as f:
        template_file = f.read()
    

    html_string = markdown_to_html_node(from_file)
    title = extract_title(html_string)
    final_html = template_file.replace("{{ Title }}", title).replace("{{ Content }}", html_string)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, 'w', encoding='utf-8') as f:
        f.write(final_html)

    print(f"Page successfully generated at {dest_path}")

