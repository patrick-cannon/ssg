def extract_title(markdown):

    if not markdown.startswith("# "):
        raise Exception("no h1 header")
    else:
        return markdown.lstrip("# ").rstrip()
