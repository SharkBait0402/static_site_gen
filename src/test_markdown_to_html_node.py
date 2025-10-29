import unittest

from blocks import markdown_to_html_node


class TestTextNode(unittest.TestCase):

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        # print(html)
        # print(node)
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        # print(html)
        # print("<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>")
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_header(self):
        md = """
# This is **bolded** header
text in an h
tag here

This is a paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        # print(html)
        # print(node)
        self.assertEqual(
            html,
            "<div><h1>This is <b>bolded</b> header text in an h tag here</h1><p>This is a paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_h6(self):
        md = """
###### This is **bolded** header
text in an h
tag here

This is a paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        # print(html)
        # print(node)
        self.assertEqual(
            html,
            "<div><h6>This is <b>bolded</b> header text in an h tag here</h6><p>This is a paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_h7(self):
        md = """
####### This is **bolded** header
text in an h
tag here

This is a paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        # print(html)
        # print(node)
        self.assertEqual(
            html,
            "<div><p>####### This is <b>bolded</b> header text in an h tag here</p><p>This is a paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_img(self):
        md = """
![JRR Tolkien sitting](/images/tolkien.png)
"""

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(html,
            "<div><img src=/images/tolkien.png alt=JRR Tolkien sitting></div>",
            )


if __name__ == "__main__":
    unittest.main()
