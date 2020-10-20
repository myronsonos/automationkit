

class Error(Exception):
    pass


class IncomingDecodeError(Error):
    pass


class NonUniqueNameException(Error):
    pass


class NamePartTooLongException(Error):
    pass


class AbstractMethodException(Error):
    pass


class BadTypeInNameException(Error):
    pass
