import unittest

from markdown import split_nodes_link, split_nodes_image, extract_markdown_links
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):

    def test_link(self):
        node = TextNode(
        "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
        TextType.TEXT,
        )

        new_nodes = split_nodes_link([node])

        correct =  [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode(
                "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
            ),
            ]

        # print('new_nodes... ', new_nodes)
        self.assertListEqual(correct, new_nodes)

    def test_link_in_text(self):
        node = TextNode(
        "This is text with a link [to boot dev](https://www.boot.dev) in the middle of some text",
        TextType.TEXT,
        )

        new_nodes = split_nodes_link([node])

        correct =  [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" in the middle of some text", TextType.TEXT),
            ]

        # print('new_nodes... ', new_nodes)
        self.assertListEqual(correct, new_nodes)

    def test_image(self):
        node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
        )

        new_nodes = split_nodes_image([node])

        correct =  [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMG, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode(
                "second image", TextType.IMG, "https://i.imgur.com/3elNhQu.png"
            ),
            ]

        self.assertListEqual(correct, new_nodes)

    def test_two_links_same(self):
        node = TextNode(
        "This is text with a link [to boot dev](https://www.boot.dev) and [to boot dev](https://www.boot.dev)",
        TextType.TEXT,
        )

        new_nodes = split_nodes_link([node])

        correct =  [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode(
                "to boot dev", TextType.LINK, "https://www.boot.dev"
            ),
            ]

        # print('new_nodes... ', new_nodes)
        self.assertListEqual(correct, new_nodes)

    def test_link_end(self):
        node = TextNode(
            "Want to get in touch? [Contact me here](/contact).",
        TextType.TEXT,
        )

        new_nodes = split_nodes_link([node])

        correct =  [
            TextNode("Want to get in touch? ", TextType.TEXT),
            TextNode("Contact me here", TextType.LINK, "/contact"),
            TextNode(".", TextType.TEXT),
            ]

        # print('new_nodes... ', new_nodes)
        self.assertListEqual(correct, new_nodes)

    def test_link_extract_end(self):
        node = TextNode(
        "Want to get in touch? [Contact me here](/contact).",
        TextType.TEXT,
        )

        text = extract_markdown_links(node.text)
        split_node = node.text.split("[Contact me here](/contact)")
        # print(text)

        self.assertEqual(text, [("Contact me here", "/contact")])



if __name__ == "__main__":
    unittest.main()

