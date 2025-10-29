import unittest

from textnode import text_node_to_html, TextNode, TextType


class TestTextNode(unittest.TestCase):

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")

    def test_img(self):
        node = TextNode("This is a image node", TextType.IMG, "/images/bigbird")
        html_node = text_node_to_html(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "/images/bigbird", "alt": "This is a image node"})

    def test_link(self):
        node = TextNode("This is a link node", TextType.LINK, "www.bigbird.com")
        html_node = text_node_to_html(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link node")
        self.assertEqual(html_node.props, {"href": "www.bigbird.com"})



if __name__ == "__main__":
    unittest.main()
