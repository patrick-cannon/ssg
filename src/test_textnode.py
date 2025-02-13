import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    def test_uneq(self):
        node3 = TextNode("This is a text node", TextType.BOLD_TEXT)
        node4 = TextNode("This is a text node", TextType.ITALIC_TEXT)
        self.assertNotEqual(node3, node4)

    def test_url(self):
        node5 = TextNode("Test", TextType.BOLD_TEXT, None)
        node6 = TextNode("Test", TextType.BOLD_TEXT, None)
        self.assertEqual(node5, node6)

    def test_repr(self):
        node = TextNode("self here", TextType.NORMAL_TEXT, "https://qwant.com")
        self.assertEqual(
            "TextNode(self here, text, https://qwant.com)", repr(node)
        )

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("textnode", TextType.NORMAL_TEXT)
        htmlnode = text_node_to_html_node(node)
        self.assertEqual(htmlnode.tag, None)
        self.assertEqual(htmlnode.value, "textnode")

    def test_image(self):
        node = TextNode("image", TextType.IMAGES, "https://en.wikipedia.org")
        htmlnode = text_node_to_html_node(node)
        self.assertEqual(htmlnode.tag, "img")
        self.assertEqual(htmlnode.value, "")
        self.assertEqual(
            htmlnode.props,
            {"src": "https://en.wikipedia.org", "alt": "image"}
        )

    def test_bold(self):
        node = TextNode("bold", TextType.BOLD_TEXT)
        htmlnode = text_node_to_html_node(node)
        self.assertEqual(htmlnode.tag, "b")
        self.assertEqual(htmlnode.value, "bold")

if __name__ == "__main__":
    unittest.main()
