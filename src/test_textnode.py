import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
	def test_eq(self):
		node1 = TextNode("This is a text node", TextType.TEXT)
		node2 = TextNode("This is a text node", TextType.TEXT)
		self.assertEqual(node1, node2)


	def test_eq_false(self):
		node1 = TextNode("this is a text node", TextType.TEXT)
		node2 = TextNode("this is a text node", TextType.BOLD)
		self.assertNotEqual(node1, node2)
	

	def test_eq_false2(self):
		node1 = TextNode("This is a text node", TextType.TEXT)
		node2 = TextNode("This a text node2", TextType.TEXT)
		self.assertNotEqual(node1, node2)


	def test_eq_url(self):
		node1 = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
		node2 = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
		self.assertEqual(node1, node2)


	def test_eq_url_false(self):
		node1 = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
		node2 = TextNode("This is a text node", TextType.TEXT, "https://www.google.com")
		self.assertNotEqual(node1, node2)

	def test_eq_url_false2(self):
		node1 = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
		node2 = TextNode("This is a text node", TextType.ITALIC, "http://www.boot.dev")
		self.assertNotEqual(node1, node2)

	def test_repr(self):
		node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
		self.assertEqual("TextNode(This is a text node, bold, https://www.boot.dev)", repr(node))



if __name__ == "__main__":
	unittest.main()
