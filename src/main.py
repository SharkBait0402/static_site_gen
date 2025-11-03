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

# text = """
# In the vast and intricate weave of J.R.R. Tolkien's legendarium, amidst heroes of renown and tales of high adventure, there exists a curious anomaly: Tom Bombadil. This peculiar figure, whimsical and unfettered by the weight of Middle-earth's burdens,
# has long been a point of contention among scholars and enthusiasts. While his character exudes charm and mystery, I, as an ancient **Archmage**, must assert that his inclusion in _The Lord of the Rings_ was, unfortunately, a narrative misstep.
# """
# stripped = text.split("**")

print(stripped)
