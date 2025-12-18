from enum import Enum


class TextType(Enum):
	TEXT = "text"
	BOLD = "bold"
	ITALIC = "italic"
	CODE = "code"
	LINK = "link"
	IMAGE = "image"

class TextNode:
	def __init__(self, text, text_type, url=None):
		# Checking if text_type is a member of TextType enum
		if not isinstance(text_type, TextType):
			raise TypeError("text_type must be a member of the TextType enum!")

		self.text = text
		self.text_type = text_type
		self.url = url

	def __eq__(self, other):
		if not isinstance(other, TextNode):
			return NotImplemented

		return (
			self.text == other.text and
			self.text_type == other.text_type and
			self.url == other.url
		)
	def __repr__(self):
		return f"TextNode({self.text!r}, {self.text_type.value!r}, {self.url!r})"


