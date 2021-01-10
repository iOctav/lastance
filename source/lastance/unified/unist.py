from abc import abstractmethod


class UnistData:
    pass


class UnistPoint:
    @property
    @abstractmethod
    def line(self) -> int:
        pass

    @line.setter
    @abstractmethod
    def line(self, value):
        pass

    @property
    @abstractmethod
    def column(self) -> int:
        pass

    @column.setter
    @abstractmethod
    def column(self, value):
        pass

    @property
    @abstractmethod
    def offset(self) -> int:
        pass

    @offset.setter
    @abstractmethod
    def offset(self, value):
        pass


class UnistPosition:
    @property
    @abstractmethod
    def start(self) -> UnistPoint:
        pass

    @start.setter
    @abstractmethod
    def start(self, value):
        pass

    @property
    @abstractmethod
    def end(self) -> UnistPoint:
        pass

    @end.setter
    @abstractmethod
    def end(self, value):
        pass

    @property
    @abstractmethod
    def indent(self) -> int:
        pass

    @indent.setter
    @abstractmethod
    def indent(self, value):
        pass


class UnistNode(object):
    @property
    @abstractmethod
    def type(self):
        pass

    @type.setter
    @abstractmethod
    def type(self, value):
        pass

    @property
    @abstractmethod
    def data(self) -> UnistData:
        pass

    @data.setter
    @abstractmethod
    def data(self, value):
        pass

    @property
    @abstractmethod
    def position(self) -> UnistPosition:
        pass

    @position.setter
    @abstractmethod
    def position(self, value):
        pass


class UnistLiteral(UnistNode):
    @property
    @abstractmethod
    def value(self):
        pass

    @value.setter
    @abstractmethod
    def value(self, value):
        pass


class UnistParent(UnistNode):
    @property
    @abstractmethod
    def children(self):
        pass

    @children.setter
    @abstractmethod
    def children(self, value):
        pass
