class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        for key,value in self.props.items():
            return f" {key}={value}"

    def __repr__(self):
        return f'HTMLNode("{self.tag}","{self.value}","{self.children}","{self.props}")'

class LeafNode(HTMLNode):
    def __init__(self, tag, value: str, props = None):
        super().__init__(tag, value, None, props)
        self.tag = tag
        self.value = value
        self.props = props

    def to_html(self):
        if self.value == None:
            raise ValueError("All leafnodes need a value")
        if self.tag == None:
            return self.value

        attributes = ""
        for prop in self.props:
            attributes += f" {prop}=\"{self.props[prop]}\""

        return f"<{self.tag}{attributes}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)
        self.tag = tag
        self.children = children
        self.props = props

    def to_html(self):
        if self.tag == None:
            raise ValueError("All parentnodes need a tag")
        if self.children == None:
            raise ValueError("All parentnodes need at least one child")

        result = []
        for child in self.children:
            result.append(child.to_html())
        return f'<{self.tag}{self.props_to_html()}>{"".join(result)}</{self.tag}>'
