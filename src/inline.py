from textnode import TextNode, TextType

# list of "old_nodes", return list of "new_nodes"
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node != TextType.NORMAL_TEXT:
            new_nodes.append(node)
            continue
        split_node = []
        section = node.text.split(delimiter)
        if len(section) % 2 == 0:
            raise Exception("invalid Markdown syntax (missing closing delimiter)")
        for i in range(len(section)):
            if section[i] == "":
                continue

            if i % 2 == 0:
                split_node.append(
                    TextNode(text = section[i], text_type = TextType.NORMAL_TEXT)
                )
            else:
                split_node.append(
                    TextNode(text = section[i], text_type = text_type)
                )

        new_nodes.extend(split_node)
    return new_nodes
