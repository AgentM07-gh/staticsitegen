from enum import Enum
import re


def markdown_to_blocks(markdown):
    split_doc = markdown.split("\n\n")
    block_list = []
    for blocks in split_doc:
        line = blocks.strip()
        if line != "":
            block_list.append(line)
    return block_list

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    lines = block.split("\n")
    pattern = r"(\#)\1{0,5} "
    if lines[0][0] == ">":
        for c in lines:
            if c[0] != ">":
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    elif lines[0][:2] == "- ":
        for c in lines:
            if c[:2] != "- ":
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    elif lines[0][:3] == "1. ":
        counter = 1
        for c in lines:
            if c[:3] != f"{counter}. ":
                return BlockType.PARAGRAPH
            counter += 1
        return BlockType.ORDERED_LIST
    elif re.match(pattern, lines[0]):
        return BlockType.HEADING
    elif lines[0][:3] == "```" and lines[0][-3:] == "```":
        return BlockType.CODE
    else:
        return BlockType.PARAGRAPH