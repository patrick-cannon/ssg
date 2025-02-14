from textnode import TextNode, TextType

# list of "old_nodes", return list of "new_nodes"
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.NORMAL_TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter) # split should make an odd number of sections
        if len(sections) % 2 == 0:
            raise Exception("invalid Markdown syntax (missing closing delimiter)")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(
                    TextNode(sections[i], TextType.NORMAL_TEXT)
                )
            else:
                split_nodes.append(
                    TextNode(sections[i], text_type = text_type)
                )

        new_nodes.extend(split_nodes)
    return new_nodes
