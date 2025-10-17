from textnode import TextNode
import os
import shutil

def copy_from_public():
    shutil.rmtree("public")
    os.mkdir("public")

def main():
    pass

main()
