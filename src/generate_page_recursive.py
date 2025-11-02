import os
from generate_page import generate_page

def generate_page_recursive(dir_path_content, template_path, dest_dir_path):
    files = os.listdir(dir_path_content)
    root = 'static'
    src = dir_path_content
    beginning_path = dir_path_content
    beginning_dest = dest_dir_path

    for file in files:
        src += f'/{file}'
        dest_path = dest_dir_path
        dest_path = dest_path.replace(".md", ".html")
        # print('dest...', dest_path)
        if os.path.isfile(src):
            # print('src...', src)
            generate_page(src, template_path, dest_path)
        else:
            os.makedirs(dest_path, exist_ok=True)
            generate_page_recursive(dir_path_content, template_path, dest_path)


        src = beginning_path
        dest_path = beginning_dest


