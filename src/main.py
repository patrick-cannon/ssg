from textnode import TextType, TextNode

def main():
    test = TextNode("text", TextType.BOLD_TEXT, "https://www.boot.dev")

    print(test.__repr__())

main()
