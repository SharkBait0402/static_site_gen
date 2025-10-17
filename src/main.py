from textnode import TextNode
import os
import shutil

def main():
    shutil.rmtree("public")

    os.mkdir("public")

main()
