import unittest

from textnode import TextNode, TextType
from markdown import split_delimiter


class TestTextNode(unittest.TestCase):

    def test_single(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_delimiter([node], "`", TextType.CODE)

        correct = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]

        self.assertEqual(new_nodes, correct)

    def test_double(self):

        nodes = [
            TextNode("Head **bold** tail", TextType.TEXT),
            TextNode("unchanged", TextType.BOLD),
            TextNode("foo **bar** baz **qux**", TextType.TEXT),
            ]

        new_nodes = split_delimiter(nodes, "**", TextType.BOLD)

        correct = [
            TextNode("Head ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" tail", TextType.TEXT),
            TextNode("unchanged", TextType.BOLD),
            TextNode("foo ", TextType.TEXT),
            TextNode("bar", TextType.BOLD),
            TextNode(" baz ", TextType.TEXT),
            TextNode("qux", TextType.BOLD)
        ]

        self.assertEqual(new_nodes, correct)

    def test_one(self):
        node = TextNode("foo **bar** baz **qux**", TextType.TEXT)
        new_nodes = split_delimiter([node], "**", TextType.BOLD)

        correct = [
            TextNode("foo ", TextType.TEXT),
            TextNode("bar", TextType.BOLD),
            TextNode(" baz ", TextType.TEXT),
            TextNode("qux", TextType.BOLD)
        ]

        self.assertEqual(new_nodes, correct)

    def test_single(self):
        node = TextNode("This is text without a bolded word", TextType.TEXT)
        new_nodes = split_delimiter([node], "**", TextType.BOLD)

        correct = [
            TextNode("This is text without a bolded word", TextType.TEXT),
        ]

        self.assertEqual(new_nodes, correct)


if __name__ == "__main__":
    unittest.main()
