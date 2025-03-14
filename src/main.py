import os
import shutil
import sys

from copystatic import copy_files_recursive, generate_pages_recursively

if len(sys.argv) > 1:
    basepath = sys.argv[1]
else:
    basepath = "/"

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
dir_path_docs = "./docs"
dir_path_template = "./template.html"

def main():
    print("Deleting docs directory...")
    if os.path.exists(dir_path_docs):
        shutil.rmtree(dir_path_docs)

    print("Copying static files to docs directory...")
    copy_files_recursive(dir_path_static, dir_path_docs)

    print("Generating page from content using template.html and write to docs")
    generate_pages_recursively(
        dir_path_content, 
        dir_path_template, 
        dir_path_docs,
        basepath
        )

main()
