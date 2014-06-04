"""List of known values for the CoAP "Code" field.

The values in this module correspond to the IANA registry "`CoRE Parameters`_",
subregistries "CoAP Method Codes" and "CoAP Response Codes".

The codes come with methods that can be used to get their rough meaning, see
the :class:`Code` class for details.

.. _`CoRE Parameters`: https://www.iana.org/assignments/core-parameters/core-parameters.xhtml
"""

from ..util import ExtensibleIntEnum

class Code(ExtensibleIntEnum):
    """Value for the CoAP "Code" field.

    As the number range for the code values is separated, the rough meaning of
    a code can be determined using the :meth:`is_request`, :meth:`is_response` and
    :meth:`is_successful` methods."""

    EMPTY = 0
    GET = 1
    POST = 2
    PUT = 3
    DELETE = 4
    CREATED = 65
    DELETED = 66
    VALID = 67
    CHANGED = 68
    CONTENT = 69
    CONTINUE = 95
    BAD_REQUEST = 128
    UNAUTHORIZED = 129
    BAD_OPTION = 130
    FORBIDDEN = 131
    NOT_FOUND = 132
    METHOD_NOT_ALLOWED = 133
    NOT_ACCEPTABLE = 134
    REQUEST_ENTITY_INCOMPLETE = 136
    PRECONDITION_FAILED = 140
    REQUEST_ENTITY_TOO_LARGE = 141
    UNSUPPORTED_MEDIA_TYPE = 143
    INTERNAL_SERVER_ERROR = 160
    NOT_IMPLEMENTED = 161
    BAD_GATEWAY = 162
    SERVICE_UNAVAILABLE = 163
    GATEWAY_TIMEOUT = 164
    PROXYING_NOT_SUPPORTED = 165

    def is_request(self):
        """True if the code is in the request code range"""
        return True if (self >= 1 and self < 32) else False


    def is_response(self):
        """True if the code is in the response code range"""
        return True if (self >= 64 and self < 192) else False


    def is_successful(self):
        """True if the code is in the successful subrange of the response code range"""
        return True if (self >= 64 and self < 96) else False

    @property
    def dotted(self):
        """The numeric value three-decimal-digits (c.dd) form"""
        return "%d.%02d"%divmod(self, 32)

    @property
    def name_printable(self):
        """The name of the code in human-readable form"""
        return self.name.replace('_', ' ').title()

    def __str__(self):
        if self.is_request() or self is self.EMPTY:
            return self.name
        elif self.is_response():
            return "%s %s"%(self.dotted, self.name_printable)
        else:
            return "%d"%self

    def __repr__(self):
        return '<Code %d "%s">'%(self, self)

    name = property(lambda self: self._name if hasattr(self, "_name") else "(unknown)", lambda self, value: setattr(self, "_name", value), doc="The constant name of the code (equals name_printable readable in all-caps and with underscores)")

for k in vars(Code):
    if isinstance(getattr(Code, k), Code):
        locals()[k] = getattr(Code, k)

__all__ = ['Code'] + [k for (k,v) in locals().items() if isinstance(v, Code)]
