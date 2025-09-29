import unittest

from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf2(self):
        node = LeafNode(None, "Howdy folks")
        self.assertEqual(node.to_html(), "Howdy folks")

    def test_leaf3(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_leaf4(self):
        node = LeafNode("a", "Click", {"href": "https://x.com"})
        self.assertIn('href="https://x.com"', node.to_html())

if __name__ == "__main__":
    unittest.main()
