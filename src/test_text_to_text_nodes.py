import unittest

from markdown import text_to_text_nodes
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):

    def test_node(self):

        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

        new_nodes = text_to_text_nodes(text)

        correct =  [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMG, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
            ]

        # print('\n\nnew nodes... ', new_nodes, '\n\n')
        # print('correct... ', correct, '\n\n')
        self.assertListEqual(correct, new_nodes)

    def test_node_two_links(self):

        text = "This is **text** with an _italic_ word and a `code block` and an [link](https://boot.dev) and another [link](https://boot.dev)"

        new_nodes = text_to_text_nodes(text)

        correct =  [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
            TextNode(" and another ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
            ]

        # print('\n\nnew nodes... ', new_nodes, '\n\n')
        # print('correct... ', correct, '\n\n')
        self.assertListEqual(correct, new_nodes)

    def test_node_two_image(self):

        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and another ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg)"

        new_nodes = text_to_text_nodes(text)

        correct =  [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMG, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and another ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMG, "https://i.imgur.com/fJRm4Vk.jpeg"),
            ]

        # print('\n\nnew nodes... ', new_nodes, '\n\n')
        # print('correct... ', correct, '\n\n')
        self.assertListEqual(correct, new_nodes)

    def test_node_two_image(self):

        text = "This is another paragraph with _italic_ text and `code` here"


        new_nodes = text_to_text_nodes(text)

        correct =  [
            TextNode("This is another paragraph with ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text and ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" here", TextType.TEXT),
            ]

        # print('\n\nnew nodes... ', new_nodes, '\n\n')
        # print('correct... ', correct, '\n\n')
        self.assertListEqual(correct, new_nodes)




if __name__ == "__main__":
    unittest.main()
