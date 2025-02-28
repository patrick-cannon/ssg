import os
import shutil
from blocks import markdown_to_html_node
from title import extract_title

def copy_files_recursive(source_directory_path, destination_directory_path):
    if not os.path.exists(destination_directory_path):
        os.mkdir(destination_directory_path)

    for filename in os.listdir(source_directory_path):
        from_path = os.path.join(source_directory_path, filename)
        to_path = os.path.join(destination_directory_path, filename)
        print(f" * {from_path} -> {to_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, to_path)
        else:
            copy_files_recursive(from_path, to_path)

def generate_page(from_path, template_path, dest_path):
    print(f' Generating page from {from_path} to {dest_path} using {template_path}')

    original_file = os.open(from_path)
    original_markdown = read(file)

    template_file = os.open(template_path)
    template_markdwon = read(template_file)

    html_string = markdown_to_html_node(original_markdown).to_html()

    title = extract_title(html_string)
