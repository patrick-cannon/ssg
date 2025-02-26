from textnode import TextNode, TextType
import re

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

# extract links
def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches


def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

# split TextNode objects
def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.NORMAL_TEXT:
            new_nodes.append(old_node) # other type of text
            continue

        old_text = old_node.text
        images = extract_markdown_images(old_text)
        if len(images) == 0:
            new_nodes.append(old_node) # no images present
            continue

        for image in images:
            sections = old_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("image section not complete")
            if sections[0] != '':
                new_nodes.append(TextNode(sections[0], TextType.NORMAL_TEXT))
            new_nodes.append(
                TextNode(
                    image[0],
                    TextType.IMAGES,
                    image[1]
                )
            )
            old_text = sections[1]

        if old_text != '':
            new_nodes.append(TextNode(old_text, TextType.NORMAL_TEXT))

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.NORMAL_TEXT:
            new_nodes.append(old_node) # other type of text
            continue
        old_text = old_node.text
        links = extract_markdown_links(old_text)
        if len(links) == 0:
            new_nodes.append(old_node) # no links present
            continue

        for link in links:
            sections = old_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("link section not complete")
            if sections[0] != '':
                new_nodes.append(TextNode(sections[0], TextType.NORMAL_TEXT))
            new_nodes.append(
                TextNode(
                    link[0],
                    TextType.LINKS,
                    link[1]
                )
            )
            old_text = sections[1]

        if old_text != '':
            new_nodes.append(TextNode(old_text, TextType.NORMAL_TEXT))

    return new_nodes


def text_to_textnodes(text):
    final_nodes = [TextNode(text, TextType.NORMAL_TEXT)]

    bold_words = split_nodes_delimiter(final_nodes, "**", TextType.BOLD_TEXT)

    italic_words = split_nodes_delimiter(bold_words, "*", TextType.ITALIC_TEXT)

    code_words = split_nodes_delimiter(italic_words, "`", TextType.CODE_TEXT)

    images = split_nodes_image(code_words)

    links = split_nodes_link(images)

    final_nodes.extend(links)

    return final_nodes
