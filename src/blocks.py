def markdown_to_blocks(markdown):
    substring = "\n\n"
    block_strings = markdown.split(substring)

    cleaned_block_strings = []
    for block in block_strings:
        if len(block) == 0:
            continue
        stripped_block = block.strip()
        cleaned_block_strings.append(stripped_block)

    return cleaned_block_strings

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(markdown):
    if
