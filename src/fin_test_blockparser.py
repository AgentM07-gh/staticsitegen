import unittest
from markdownparser import *
from textnode import TextNode, TextType
from blockparser import *


'''
class TestBlocks(unittest.TestCase):
    
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks2(self):
        md = """
This is **bolded** paragraph
Some more stuff here



This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line
what if we had three lines

- This is a list
- with items
- more items

            and even more stuff here       
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph\nSome more stuff here",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line\nwhat if we had three lines",
                "- This is a list\n- with items\n- more items",
                "and even more stuff here"
            ],
        )

'''

class TestBlockTypes(unittest.TestCase):
    def test_blocktype_header(self):
        md = "## This is Heading block"
        heading_test = block_to_block_type(md)
        self.assertEqual(heading_test, BlockType.HEADING)
    
    def test_blocktype_paragraph(self):
        md = "this is just plain old paragrpah block"
        para_text = block_to_block_type(md)
        self.assertEqual(para_text, BlockType.PARAGRAPH)
    
    def test_blocktype_code(self):
        md = "```this is code block```"
        code_text = block_to_block_type(md)
        self.assertEqual(code_text, BlockType.CODE)
    
    def test_blocktype_onequote(self):
        md = ">this is single quote line"
        one_quote_text = block_to_block_type(md)
        self.assertEqual(one_quote_text, BlockType.QUOTE)

    def test_blocktype_multiplequote(self):
        md = ">this is single quote line\n>with extra quoteline\n>third quoteline"
        multi_quote_text = block_to_block_type(md)
        self.assertEqual(multi_quote_text, BlockType.QUOTE)
    
    def test_blocktype_notaquote(self):
        md = ">this is single quote line\n>with extra quoteline\nthird quoteline"
        nota_quote_text = block_to_block_type(md)
        self.assertEqual(nota_quote_text, BlockType.PARAGRAPH)

    def test_blocktype_ordered_list(self):
        md = "1. this is single quote line\n2. with extra quoteline\n3. third quoteline"
        ordered_list_text = block_to_block_type(md)
        self.assertEqual(ordered_list_text, BlockType.ORDERED_LIST)
    
    def test_blocktype_unordered_list(self):
        md = "- this is single quote line\n- with extra quoteline\n- third quoteline"
        unordered_list_text = block_to_block_type(md)
        self.assertEqual(unordered_list_text, BlockType.UNORDERED_LIST)  



if __name__ == "__main__":
    unittest.main()
