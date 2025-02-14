import unittest
from inline import (
    split_nodes_delimiter,
)

from textnode import TextNode, TextType

class TestInlineMarkdown(unittest.TestCase):
    def test_delim_italics(self):
        node = TextNode("This node is *italic* and that's cool.", TextType.NORMAL_TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC_TEXT)
        self.assertEqual(
            [
                TextNode("This node is ", TextType.NORMAL_TEXT),
                TextNode("italic", TextType.ITALIC_TEXT),
                TextNode(" and that's cool.", TextType.NORMAL_TEXT)
                ],
            new_nodes,
        )

    def test_delim_bold(self):
        node = TextNode("This node is **bold** and that's fun.", TextType.NORMAL_TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
        self.assertEqual(
            [
                TextNode("This node is ", TextType.NORMAL_TEXT),
                TextNode("bold", TextType.BOLD_TEXT),
                TextNode(" and that's fun.", TextType.NORMAL_TEXT)
                ],
            new_nodes
        )

