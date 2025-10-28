import unittest

from blocks import extract_title


class TestTextNode(unittest.TestCase):

    def test_no_title(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""

        try:
            header = extract_title(md)
        except Exception:
            self.assertRaises(Exception)


    def test_h1_beginning(self):
        md = """
# this is a h1 header

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""

        header = extract_title(md)

        self.assertEqual(header, "this is a h1 header")

    def test_h1_middle(self):
        md = """
## this is a h2 header

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

# this is a title in the middle

- This is a list
- with items
"""

        header = extract_title(md)

        self.assertEqual(header, "this is a title in the middle")

if __name__ == "__main__":
    unittest.main()
