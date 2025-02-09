import unittest

from textnode import TextNode, TextType


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


if __name__ == "__main__":
    unittest.main()
