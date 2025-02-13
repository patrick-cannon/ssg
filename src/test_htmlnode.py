import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType

# HTMLNode Tests

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(
            "p",
            "test paragraph",
            props={"<a>": "https://www.google.com"}
        )
        self.assertEqual(
            node.tag,
            "p"
        )
        self.assertEqual(
            node.value,
            "test paragraph"
        )
        self.assertEqual(
            node.children,
            None
        )
        self.assertEqual(
            node.props,
            {"<a>": "https://www.google.com"}
        )

    def test_uneq(self):
        node = HTMLNode(
            "p",
            "test paragraph",
            props={"<a>": "https://www.google.com"}
        )
        self.assertEqual(
            node.tag,
            "p"
        )
        self.assertEqual(
            node.value,
            "test paragraph"
        )
        self.assertNotEqual(
            node.children,
            [HTMLNode]
        )
        self.assertEqual(
            node.props,
            {"<a>": "https://www.google.com"}
        )

    def test_props_to_html(self):
        node = HTMLNode(
            "p",
            "test paragraph",
            [HTMLNode, HTMLNode],
            {"<a>": "https://www.google.com"}
        )
        self.assertEqual(
            node.props_to_html(),
            ' <a>="https://www.google.com"'
        )

    def test_repr(self):
        node = HTMLNode(
            "h1",
            "Send a birthday note!",
            None,
            {"class": "hero"}
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(h1, Send a birthday note!, children: None, {'class': 'hero'})"
        )

# LeafNode tests

class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode(
            "p",
            "test paragraph",
            props={"<a>": "https://www.google.com"}
        )
        self.assertEqual(
            node.tag,
            "p"
        )
        self.assertEqual(
            node.value,
            "test paragraph"
        )
        self.assertEqual(
            node.props,
            {"<a>": "https://www.google.com"}
        )

    def test_uneq(self):
        node = LeafNode(
            "style",
            "morphg",
            props={"<a>": "https://www.google.com"}
        )
        self.assertEqual(
            node.tag,
            "style"
        )
        self.assertEqual(
            node.value,
            "morphg"
        )
        self.assertEqual(
            node.children,
            None
        )
        self.assertEqual(
            node.props,
            {"<a>": "https://www.google.com"}
        )

    def test_to_html_no_children(self):
        node = LeafNode("li", "oh no")
        self.assertEqual(node.to_html(), "<li>oh no</li>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "here we go again")
        self.assertEqual(node.to_html(), "here we go again")

# ParentNode tests
class TestParentNode(unittest.TestCase):
    def test_html_with_children(self):
        child = LeafNode("p", "something")
        parent = ParentNode("p", [child])
        self.assertEqual(parent.to_html(), "<p><p>something</p></p>")

    def test_html_with_grandchildren(self):
        grandchild = LeafNode("b", "lovely day Wilson!")
        child = ParentNode("p", [grandchild])
        parent = ParentNode("div", [child])
        self.assertEqual(
            parent.to_html(),
            "<div><p><b>lovely day Wilson!</b></p></div>"
        )

    def test_html_multiple_children(self):
        node = ParentNode(
            "h3",
            [
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
                LeafNode("p", "Paragraph text"),
                LeafNode("b", "Bold text"),
                LeafNode(None, "More normal TEXT")
            ]
        )
        self.assertEqual(
            node.to_html(),
            "<h3><i>italic text</i>Normal text<p>Paragraph text</p><b>Bold text</b>More normal TEXT</h3>"
        )


if __name__ == "__main__":
    unittest.main()
