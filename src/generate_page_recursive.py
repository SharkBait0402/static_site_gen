import os
from generate_page import generate_page

def generate_page_recursive(dir_path_content, template_path, dest_dir_path):
    files = os.listdir(dir_path_content)
    root = 'static'
    src = dir_path_content
    beginning_path = dir_path_content
    beginning_dest = dest_dir_path

    for file in files:
        current = src + f'/{file}'
        dest_path = dest_dir_path
        dest_path = dest_path.replace(".md", ".html")
        # print('dest...', dest_path)
        new_dest = dest_path + f'/{file}'
        new_dest = new_dest.replace('.md', '.html')

        if os.path.isfile(current):
            # print('src...', src)
            generate_page(current, template_path, new_dest)
        else:
            os.makedirs(dest_path + f'/{file}', exist_ok=True)
            generate_page_recursive(current, template_path, new_dest)




