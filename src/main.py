from textnode import TextNode
from generate_page_recursive import generate_page_recursive
import os
import shutil

def copy_from_static(path, dest):
    files = os.listdir(path)
    # print(files, 'files ... ')
    root = 'static'
    src = path
    beginning_path = path

    if path == root:
        shutil.rmtree("public")
        os.mkdir("public")

    for file in files:
        src += f'/{file}'
        dest_path = dest
        # print(dest_path, 'dest...')
        # print('src... ', src)
        if os.path.isfile(src):
            # print(src, 'src')
            # print(dest_path, 'dest\n\n')
            shutil.copy(src, dest_path)
        else:
            # print(src, 'src not file')
            dest_path += f'/{file}'
            os.mkdir(dest_path)
            # print(dest_path, 'dest not file\n\n')
            copy_from_static(src, dest_path)

        src = beginning_path



def main():
    copy_from_static("static", "public")
    generate_page_recursive("content", "template.html", "public")

main()
