from textnode import TextNode
import os
import shutil

def copy_from_static(path, dest):
    files = os.listdir(path)
    root = 'static'
    src = path

    if path is root:
        shutil.rmtree("public")
        os.mkdir("public")

    for file in files:
        src += f'/{file}'
        dest_path = dest
        if os.path.isfile(src):
            print(src, 'src')
            print(dest_path, 'dest\n\n')
            shutil.copy(src, dest_path)
        else:
            print(src, 'src not file')
            dest_path += f'/{file}'
            os.mkdir(dest_path)
            print(dest_path, 'dest not file\n\n')
            copy_from_static(src, dest_path)


        src = 'static'

def main():
    copy_from_static("static", "public")

main()
