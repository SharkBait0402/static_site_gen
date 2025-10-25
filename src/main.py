from textnode import TextNode
import os
import shutil

def copy_from_public():
    files = os.listdir("static")

    shutil.rmtree("public")
    os.mkdir("public")

def main():
    copy_from_public()

main()
