from html.parser import HTMLParser
from html.entities import name2codepoint

from source.lastance.unified.hast import HastRoot, HastElement, HastText


class HastHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hast_root = HastRoot()
        self.opened_tags = [self.hast_root]

    def handle_starttag(self, tag, attrs):
        hast_element = HastElement(tag)
        self.opened_tags[-1].children.append(hast_element)
        for (attr_key, attr_val) in attrs:
            hast_element.properties[attr_key] = attr_val
        self.opened_tags.append(hast_element)

    def handle_endtag(self, tag):
        self.opened_tags.pop()

    def handle_data(self, data):
        self.opened_tags[-1].children.append(HastText(data))

    def handle_comment(self, data):
        print("Comment  :", data)

    def handle_entityref(self, name):
        c = chr(name2codepoint[name])
        print("Named ent:", c)

    def handle_charref(self, name):
        if name.startswith('x'):
            c = chr(int(name[1:], 16))
        else:
            c = chr(int(name))
        print("Num ent  :", c)

    def handle_decl(self, data):
        print("Decl     :", data)

    def error(self, message):
        pass


def from_html(html):
    parser = HastHTMLParser()
    parser.feed(html)
    return parser.hast_root
