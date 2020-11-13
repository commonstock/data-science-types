from .extension import ExtensionIndex
from .numeric import Int64Index


class DatetimeIndexOpsMixin(ExtensionIndex):
    ...


class DatetimeTimedeltaMixin(DatetimeIndexOpsMixin, Int64Index):
    ...
