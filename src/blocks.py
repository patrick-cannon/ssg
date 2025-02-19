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
