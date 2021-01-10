from .unist import UnistParent, UnistLiteral, UnistNode


class HastProperties(dict):
    pass


class HastDoctype(UnistNode):
    def __init__(self):
        self._name = None
        self._type = "doctype"
        self._public = None
        self._system = None
        self._data = None
        self._position = None

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, value):
        print("Type of HastDoctype can not be changed")

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def public(self) -> str:
        return self._public

    @public.setter
    def public(self, value):
        self._public = value

    @property
    def system(self) -> str:
        return self._system

    @system.setter
    def system(self, value):
        self._system = value

    @property
    def data(self) -> str:
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    @property
    def position(self) -> str:
        return self._position

    @position.setter
    def position(self, value):
        self._position = value


class HastParent(UnistParent):
    def __init__(self, children=None):
        if children is None:
            children = []
        self._children = children
        self._type = "doctype"
        self._data = None
        self._position = None

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    @property
    def data(self) -> str:
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    @property
    def position(self) -> str:
        return self._position

    @position.setter
    def position(self, value):
        self._position = value

    @property
    def children(self) -> []:
        return self._children

    @children.setter
    def children(self, value):
        self._children = value


class HastRoot(HastParent):
    def __init__(self, children=None):
        super().__init__(children)
        self.type = "root"


class HastElement(HastParent):
    def __init__(self, tag_name, properties=None, content=None, children=None):
        super().__init__(children)
        if properties is None:
            properties = HastProperties()
        self._type = "element"
        self._tag_name = tag_name
        self._properties = properties
        self._content = content

    @property
    def type(self) -> str:
        return self._type

    @property
    def tag_name(self) -> str:
        return self._tag_name

    @property
    def properties(self) -> HastProperties:
        return self._properties

    @property
    def content(self) -> HastRoot:
        return self._content


class HastLiteral(UnistLiteral):
    def __init__(self, value):
        self._value = value
        self._type = "doctype"
        self._data = None
        self._position = None

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    @property
    def data(self) -> str:
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    @property
    def position(self) -> str:
        return self._position

    @position.setter
    def position(self, value):
        self._position = value

    @property
    def value(self) -> str:
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


class HastText(HastLiteral):
    def __init__(self, value):
        super().__init__(value)
        self._type = "text"


class HastComment(HastLiteral):
    def __init__(self, value):
        super().__init__(value)
        self._type = "comment"
