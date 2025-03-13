import os
import shutil

from copystatic import copy_files_recursive, generate_pages_recursively


dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
dir_path_template = "./template.html"

def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating page from content/index.md using template.html and write to public/index.html")
    generate_pages_recursively(
        dir_path_content, 
        dir_path_template, 
        dir_path_public
        )

main()
