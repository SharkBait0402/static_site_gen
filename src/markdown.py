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
                if text == "":
                    break
                if text.startswith(" ") or text.endswith(" "):
                    nodes.append(TextNode(text, TextType.TEXT))

                elif not text.startswith(" ") and not text.endswith(" "):
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

        for link in chunks:
            # print('link... ', link)
            anchor = link[0]
            url = link[1]
            
            split_node = txt.split(f"[{anchor}]({url})")
            # print('split... ', split_node)
            txt = split_node[1]
            links.append(split_node[0])
            links.append(f"[{anchor}]({url})")
        if txt is not None:
            links.append(txt)
            # print("node", links)
            
        # print('links... ', links)

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
                    info = extract_markdown_links(text)[0]
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
        

        if chunks == []:
            nodes.append(node)
            continue


        txt = node.text

        links = []

        for link in chunks:
            # print('link... ', link)
            anchor = link[0]
            url = link[1]
            
            split_node = txt.split(f"![{anchor}]({url})")
            # print('split... ', split_node)
            txt = split_node[1]
            links.append(split_node[0])
            links.append(f"[{anchor}]({url})")
        if txt is not None:
            links.append(txt)
            # print("node", links)
            
        # print(links)

        if node.type is TextType.TEXT:
            # print('chunks... ', chunks)
            if chunks == []:
                nodes.append(node)
            for text in links:
                # print('text...', f"\'{text}\'")
                if text == "":
                    continue
                if text.startswith(" ") or text.endswith(" "):
                    # print("ran")
                    nodes.append(TextNode(text, TextType.TEXT))
                    # print('temp_nodes...', nodes)

                elif not text.startswith(" ") and not text.endswith(" "):
                    info = extract_markdown_links(text)[0]
                    # print('info... ', info)
                    nodes.append(TextNode(info[0], TextType.IMG, info[1]))
                # print('nodes... ', nodes)
                
        else:
            nodes.append(node)

    # print(nodes)
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


















































