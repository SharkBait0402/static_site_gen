
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

        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], new_nodes)

    # def test_extract_markdown_links(self):
    #     matches = extract_markdown_links(
    #         "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    #     )
    #     self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)


if __name__ == "__main__":
    unittest.main()

