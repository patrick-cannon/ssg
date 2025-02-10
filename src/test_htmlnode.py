import unittest

from htmlnode import HTMLNode, LeafNode

# HTMLNode Tests

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "test paragraph", props={"<a>": "https://www.google.com"})
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "test paragraph")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, {"<a>": "https://www.google.com"})

    def test_uneq(self):
        node = HTMLNode("p", "test paragraph", props={"<a>": "https://www.google.com"})
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "test paragraph")
        self.assertNotEqual(node.children, [HTMLNode])
        self.assertEqual(node.props, {"<a>": "https://www.google.com"})

    def test_props_to_html(self):
        node = HTMLNode("p", "test paragraph", [HTMLNode, HTMLNode], {"<a>": "https://www.google.com"})
        output = node.props_to_html()
        self.assertEqual(output, " <a>=https://www.google.com")

# LeafNode tests

class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode("p", "test paragraph", props={"<a>": "https://www.google.com"})
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "test paragraph")
        self.assertEqual(node.props, {"<a>": "https://www.google.com"})

if __name__ == "__main__":
    unittest.main()
