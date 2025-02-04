import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "This is a HTML node", [], {
            "href": "https://www.google.com",
            "target": "_blank",}
            )
        node2 = HTMLNode("p", "This is a HTML node", [], {
            "href": "https://www.google.com",
            "target": "_blank",}
            )
        self.assertEqual(node,node2)

    def test_eq_false(self):
        node = HTMLNode("a", "This is a HTML node", [], {
            "href": "https://www.google.com",
            "target": "_blank",}
            )
        node2 = HTMLNode("p", "This is a HTML node", [], {
            "href": "https://www.google.com",
            "target": "_blank",}
            )
        self.assertNotEqual(node,node2)
    
    def test_eq_false2(self):
        node = HTMLNode("p", "This is a HTML node", [], {
            "href": "https://www.google.com",
            "target": "_blank",}
            )
        node2 = HTMLNode("p", "This is a HTML node2", [], {
            "href": "https://www.google.com",
            "target": "_blank",}
            )
        self.assertNotEqual(node,node2)

    def test_eq_false3(self):
        node = HTMLNode("p", "This is a HTML node", [], {
            "href": "https://www.google.com",
            "target": "_blank",}
            )
        node2 = HTMLNode("p", "This is a HTML node", [node], {
            "href": "https://www.google.com",
            "target": "_blank",}
            )
        self.assertNotEqual(node,node2)

    def test_eq_false4(self):
        node = HTMLNode("p", "This is a HTML node", [], {
            "href": "https://www.google.com",
            "target": "_blank",}
            )
        node2 = HTMLNode("p", "This is a HTML node", [], {
            "href": "https://www.boot.dev.com",
            "target": "_blank",}
            )
        self.assertNotEqual(node,node2)
    
    def test_props_to_html(self):
        node = HTMLNode("p", "This is a HTML node", [], {
            "href": "https://www.google.com",
            "target": "_blank",}
            )
        self.assertEqual(node.props_to_html(),' href="https://www.google.com" target="_blank"')

    def test_rpre(self):
        node = HTMLNode("p", "This is a HTML node", [], {
            "href": "https://www.google.com",
            "target": "_blank",}
            )
        self.assertEqual( 
            repr(node),
            "HTMLNode(p, This is a HTML node, children: [], {'href': 'https://www.google.com', 'target': '_blank'})"
            )
        
    def test_values(self):
        node = HTMLNode(
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

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )


if __name__ == "__main__":
    unittest.main()