import unittest

from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):

    def test_values(self):
        node = LeafNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_to_html(self):
        node = LeafNode(
            "p",
            "This is a paragraph of text."
        )
        self.assertEqual("<p>This is a paragraph of text.</p>", node.to_html())
    
    def test_to_html2(self):
        node = LeafNode(
            "a",
            "Click me!",
            {"href": "https://www.google.com"}
        )
        self.assertEqual('<a href="https://www.google.com">Click me!</a>', node.to_html())

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

if __name__ == "__main__":
    unittest.main()