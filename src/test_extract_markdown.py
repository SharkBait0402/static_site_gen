
import unittest

from markdown import split_nodes_link, split_nodes_image
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

        self.assertListEqual(correct, new_nodes)

    def test_image(self):
        node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
        )

        new_nodes = split_nodes_link([node])

        correct =  [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMG, "https://www.boot.dev"),
            TextNode(" and another ", TextType.TEXT),
            TextNode(
                "to youtube", TextType.IMG, "https://www.youtube.com/@bootdotdev"
            ),
            ]

        self.assertListEqual(correct, new_nodes)




if __name__ == "__main__":
    unittest.main()

