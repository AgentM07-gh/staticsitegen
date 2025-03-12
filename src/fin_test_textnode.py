import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_neq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a a different text node", TextType.TEXT)
        self.assertNotEqual(node, node2)
    
    def test_text_neq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertNotEqual(node, node2)
    
    def test_url_eq(self):
        node = TextNode("This is a link node", TextType.LINK, "www.web.com")
        node2 = TextNode("This is a link node", TextType.LINK, "www.web.com")
        self.assertEqual(node, node2)
    
    def test_url_neq(self):
        node = TextNode("This is a image node", TextType.IMAGE, "www.image.com")
        node2 = TextNode("This is a link node", TextType.LINK, "www.web.com")
        self.assertNotEqual(node, node2)
    
    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual("TextNode(This is a text node, text, https://www.boot.dev)", repr(node))


if __name__ == "__main__":
    unittest.main()