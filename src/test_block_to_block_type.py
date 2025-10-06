import unittest

from blocks import block_to_block_type, BlockType


class TestBlockToBlockType(unittest.TestCase):

    def test_head(self):
        block = "# this is a heading"
        block_type = block_to_block_type(block)

        self.assertEqual(BlockType.H, block_type)

    def test_quote(self):
        block = ">this is a quote\n>and another"
        block_type = block_to_block_type(block)

        self.assertEqual(BlockType.QUOTE, block_type)

    def test_ul(self):
        block = "- this is a list item\n- and another"
        block_type = block_to_block_type(block)

        self.assertEqual(BlockType.UL, block_type)

    def test_ol(self):
        block = "1. this is a list item\n2. and another"
        block_type = block_to_block_type(block)

        self.assertEqual(BlockType.OL, block_type)

    def test_code(self):
        block = "```this is some code that i have written```"
        block_type = block_to_block_type(block)

        self.assertEqual(BlockType.CODE, block_type)

    def test_paragraph(self):
        block = "this is just a normal paragraph"
        block_type = block_to_block_type(block)

        self.assertEqual(BlockType.P, block_type)


if __name__ == "__main__":
    unittest.main()
