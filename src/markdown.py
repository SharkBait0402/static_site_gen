import re
from textnode import TextNode, TextType, text_node_to_html





def split_delimiter(old_nodes, delimiter, text_type):

    #print(split_node)
    nodes = []

    for node in old_nodes:

        split_node = node.text.split(delimiter)
        if node.type is TextType.TEXT:
            for text in split_node:
                #print(text)
                strip_text = text.strip(",!.?:")
                if text == "":
                    continue
                if strip_text.startswith(" ") or strip_text.endswith(" ") or strip_text == node.text:
                    nodes.append(TextNode(text, TextType.TEXT))

                elif not strip_text.startswith(" ") and not strip_text.endswith(" "):
                    nodes.append(TextNode(text, text_type))
        else:
            nodes.append(node)

    return nodes




def extract_markdown_images(text):
    images = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return images

def extract_markdown_links(text):
    links = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return links

def is_link(text):
    arr = extract_markdown_links(text)
    if arr == []:
        return False
    return True

def split_nodes_link(old_nodes):
    nodes = []


    for node in old_nodes:

        chunks = extract_markdown_links(node.text)
        # print('node...', node)

        txt = node.text

        links = []

        # print('txt... ', txt)

        if chunks == []:
            nodes.append(node)
            continue

        i = 0
        for link in chunks:
            # print('link... ', link)
            anchor = link[0]
            url = link[1]
            
            split_node = txt.split(f"[{anchor}]({url})")
            # print('split... ', split_node)
            if len(split_node) > 1:
                txt = split_node[1]
                links.append(split_node[0])
                i += 1
            links.append(f"[{anchor}]({url})")
            # print('links... ', links)
            if txt is not None and not txt in links and extract_markdown_links(txt) == []:
                links.append(txt)


        if node.type is TextType.TEXT:
            # print('chunks... ', chunks)

            for text in links:

                if len(links) == 1:
                    break

                # print('text...', f"\'{text}\'")
                if text == "":
                    continue
                if not is_link(text):
                    # print("ran")
                    nodes.append(TextNode(text, TextType.TEXT))
                    # print('temp_nodes...', nodes)

                elif is_link(text):
                    info = extract_markdown_links(text)[0]
                    # print('text... ', text)
                    # print('info... ', info)
                    nodes.append(TextNode(info[0], TextType.LINK, info[1]))

        else:
            nodes.append(node)

    # print('\n\n\nnodes', nodes)
    return nodes

def split_nodes_image(old_nodes):
    nodes = []


    for node in old_nodes:

        chunks = extract_markdown_images(node.text)
        # print('node...', node)

        txt = node.text

        links = []

        # print('txt... ', txt)

        if chunks == []:
            nodes.append(node)
            continue

        i = 0
        for link in chunks:
            # print('link... ', link)
            anchor = link[0]
            url = link[1]
            
            split_node = txt.split(f"![{anchor}]({url})")
            # print('split... ', split_node)
            if len(split_node) > 1:
                txt = split_node[1]
                links.append(split_node[0])
                i += 1
            links.append(f"![{anchor}]({url})")
            # print('links... ', links)
            if txt is not None and not txt in links and extract_markdown_images(txt) == []:
                links.append(txt)


        if node.type is TextType.TEXT:
            # print('chunks... ', chunks)
            for text in links:
                # print('text...', f"\'{text}\'")
                if text == "":
                    continue
                if text.startswith(" ") or text.endswith(" "):
                    # print("ran")
                    nodes.append(TextNode(text, TextType.TEXT))
                    # print('temp_nodes...', nodes)

                elif not text.startswith(" ") and not text.endswith(" "):
                    info = extract_markdown_images(text)[0]
                    # print('info... ', info)
                    nodes.append(TextNode(info[0], TextType.IMG, info[1]))

        else:
            nodes.append(node)

    # print('\n\n\nnodes', nodes)
    return nodes

# This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)

def text_to_text_nodes(text):
    node = TextNode(text, TextType.TEXT)

    new_nodes = split_delimiter([node], "**", TextType.BOLD)
    new_nodes = split_delimiter(new_nodes, "`", TextType.CODE)
    new_nodes = split_delimiter(new_nodes, "_", TextType.ITALIC)
    new_nodes = split_nodes_image(new_nodes)
    new_nodes = split_nodes_link(new_nodes)

    return new_nodes


















































