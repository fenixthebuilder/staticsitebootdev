import unittest

from html_parser import get_h1_from_html, get_first_paragraph_from_html

html_test_1 = '<html><body><h1>Test Title</h1></body></html>'
html_test_2_no_h1 = '<html><body></body></html>'
html_test_3_multiple_h1 = '<html><body><h1>Test Title</h1><h1>Test Title 2</h1></body></html>'
html_test_4_empty = ''
html_test_5_whitespaces = '\n\t'
p_test_1_multiple = '<html><body><p>Outside paragraph.</p><main><p>Main paragraph.</p></main></body></html>'
p_test_2_single = '<html><body><p>Outside paragraph.</p></body></html>'
p_test_3_empty = '<html><body></body></html>'


class TestHtmlParser(unittest.TestCase):
	def test_html_single_h1(self):
		input = get_h1_from_html(html_test_1)
		output = "Test Title"
		self.assertEqual(input, output)
	def test_html_no_h1(self):
		input = get_h1_from_html(html_test_2_no_h1)
		output = ""
		self.assertEqual(input, output)
	def test_html_multiple_h1(self):
		input = get_h1_from_html(html_test_3_multiple_h1)
		output = "Test Title"
		self.assertEqual(input, output)
	def test_html_empty(self):
		input = get_h1_from_html(html_test_4_empty)
		output = ""
		self.assertEqual(input, output)
	def test_html_whitespaces(self):
		input = get_h1_from_html(html_test_5_whitespaces)
		output = ""
		self.assertEqual(input, output)
	def test_paragraph_html_multiple(self):
		input = get_first_paragraph_from_html(p_test_1_multiple)
		output = "Outside paragraph."
		self.assertEqual(input, output)
	def test_paragraph_html_single(self):
		input = get_first_paragraph_from_html(p_test_2_single)
		output = "Outside paragraph."
		self.assertEqual(input, output)
	def test_paragraph_html_empty(self):
		input = get_first_paragraph_from_html(p_test_3_empty)
		output = ""
		self.assertEqual(input, output)


if __name__ == "__main__":
	unittest.main()
