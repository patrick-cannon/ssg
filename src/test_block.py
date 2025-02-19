import unittest
from blocks import markdown_to_blocks

class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"

        block = markdown_to_blocks(markdown)
        self.assertEqual(
            [
                "# This is a heading",
                "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
                ],
            block,
        )

    def test_markdown_to_blocks_whitespace(self):
        markdown = "# This is a heading  \n\n This is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n * This is the first list item in a list block\n* This is a list item\n* This is another list item  "

        block = markdown_to_blocks(markdown)
        self.assertEqual(
            [
                "# This is a heading",
                "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
                ],
            block,
        )

    def test_markdown_to_blocks_many_newlines(self):
        markdown = "# This is a heading  \n\n\n\n\n This is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n * This is the first list item in a list block\n* This is a list item\n* This is another list item  "

        block = markdown_to_blocks(markdown)
        self.assertEqual(
            [
                "# This is a heading",
                "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
                ],
            block,
        )
