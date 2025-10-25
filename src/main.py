from textnode import TextNode
import os
import shutil

def copy_from_public():
    files = os.listdir("static")
    path = "static"

    shutil.rmtree("public")
    os.mkdir("public")

    for file in files:
        path += f'/{file}'
        print(os.path.isfile(path), '\n')
        path = 'static'

def main():
    copy_from_public()

main()
