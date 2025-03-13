import sys
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

    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    html_node = markdown_to_html_node(markdown_content)
    html_string = html_node.to_html()

    title = extract_title(markdown_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html_string)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_dir_path, "w")
    to_file.write(template)

def generate_pages_recursively(dir_path_content, template_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        if os.path.isfile(from_path):
            if filename.endswith(".md"):
                to_path = os.path.join(dest_dir_path, filename.replace(".md", ".html"))
                from_file = open(from_path, "r")
                markdown_content = from_file.read()
                from_file.close()

                template_file = open(template_path, "r")
                template = template_file.read()
                template_file.close()

                html_node = markdown_to_html_node(markdown_content)
                html_string = html_node.to_html()

                title = extract_title(markdown_content)
                template = template.replace("{{ Title }}", title)
                template = template.replace("{{ Content }}", html_string)
                
                to_file = open(to_path, "w")
                to_file.write(template)
            else:
                to_path = os.path.join(dest_dir_path, filename)

        else:
            to_path = os.path.join(dest_dir_path, filename)
            generate_pages_recursively(from_path, template_path, to_path)
            