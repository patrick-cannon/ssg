import unittest
from inline import (
    split_nodes_delimiter,
    extract_markdown_links,
    extract_markdown_images,
    split_nodes_image,
    split_nodes_link
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

    def test_delim_bold_double(self):
        node = TextNode("This sentence **has** two **bold** words.", TextType.NORMAL_TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
        self.assertEqual(
            [
                TextNode("This sentence ", TextType.NORMAL_TEXT),
                TextNode("has", TextType.BOLD_TEXT),
                TextNode(" two ", TextType.NORMAL_TEXT),
                TextNode("bold", TextType.BOLD_TEXT),
                TextNode(" words.", TextType.NORMAL_TEXT)
                ],
            new_nodes
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This sentence has **multiple bolded words** and **stuff**", TextType.NORMAL_TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
        self.assertListEqual(
            [
                TextNode("This sentence has ", TextType.NORMAL_TEXT),
                TextNode("multiple bolded words", TextType.BOLD_TEXT),
                TextNode(" and ", TextType.NORMAL_TEXT),
                TextNode("stuff", TextType.BOLD_TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** then *italic*", TextType.NORMAL_TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
        new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC_TEXT)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD_TEXT),
                TextNode(" then ", TextType.NORMAL_TEXT),
                TextNode("italic", TextType.ITALIC_TEXT),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This sentence has `code block` words", TextType.NORMAL_TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE_TEXT)
        self.assertListEqual(
            [
                TextNode("This sentence has ", TextType.NORMAL_TEXT),
                TextNode("code block", TextType.CODE_TEXT),
                TextNode(" words", TextType.NORMAL_TEXT),
            ],
            new_nodes,
        )

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev)"
        )
        self.assertListEqual(
            [
                ("link", "https://boot.dev"),
                ("another link", "https://blog.boot.dev"),
            ],
            matches,
        )

    def test_split_nodes_image(self):
        node = TextNode("This is a node with an image ![to Python](https://i.imgur.com/zjjcJKZ.png)", TextType.NORMAL_TEXT
        )
        new_node = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is a node with an image ", TextType.NORMAL_TEXT),
                TextNode("to Python", TextType.IMAGES, "https://i.imgur.com/zjjcJKZ.png")
            ],
            new_node,
        )


    def test_split_only_image(self):
        node = TextNode(
            "![image](https://cdn.kde.org/screenshots/kdevelop/kdevelop.png)",
            TextType.NORMAL_TEXT,
        )
        new_node = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGES, "https://cdn.kde.org/screenshots/kdevelop/kdevelop.png"),
            ],
            new_node,
        )

    def test_split_multiple_images(self):
        node = TextNode(
            "This is text with an ![image](https://cdn.kde.org/screenshots/kdevelop/kdevelop.png) and another ![second image](https://cdn.kde.org/screenshots/kmail/kmail.png)",
            TextType.NORMAL_TEXT,
        )
        new_node = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.NORMAL_TEXT),
                TextNode("image", TextType.IMAGES, "https://cdn.kde.org/screenshots/kdevelop/kdevelop.png"),
                TextNode(" and another ", TextType.NORMAL_TEXT),
                TextNode(
                    "second image", TextType.IMAGES, "https://cdn.kde.org/screenshots/kmail/kmail.png"
                ),
            ],
            new_node,
        )

    def test_split_nodes_link(self):
        node = TextNode("This is a node with a link [to Python](https://www.python.org/downloads/)", TextType.NORMAL_TEXT
        )
        new_node = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is a node with a link ", TextType.NORMAL_TEXT),
                TextNode("to Python", TextType.LINKS, "https://www.python.org/downloads/")
            ],
            new_node
        )
