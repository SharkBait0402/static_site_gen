import unittest

from htmlnode import HTMLNode

class TestHtmlNode(unittest.TestCase):

    def test_props_to_html(self):
        node = HTMLNode(props= {"href": "https://www.google.com", "target": "_blank",})
        correct = " href=\"https://www.google.com\" target=\"_blank\""

        self.assertEqual(node.props_to_html(), correct)

    def test_props2(self):
        node = HTMLNode(props= {"class": "header",})
        correct = " class=\"header\""

        self.assertEqual(node.props_to_html(), correct)

    def test_props3(self):
        node = HTMLNode()
        correct = ""

        self.assertEqual(node.props_to_html(), correct)




if __name__ == "__main__":
    unittest.main()
