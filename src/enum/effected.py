from enum import Enum


class Effected(Enum):
    AS_NONE = 0
    AS_SINGLE_QUOTE_STRING = 1
    AS_DOUBLE_QUOTE_STRING = 2
    AS_COMMENT = 3
    AS_DOC_STRING = 4
