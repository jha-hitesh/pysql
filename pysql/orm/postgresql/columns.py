class BaseColumn:
    """BaseColumn."""
    data_type_validator = None
    data_type_error_msg = "Invalid data type detected"

    def __init__(
        self, select=True, where=False,
        join=False, nullable=True, **kwargs
    ):
        """Init."""
        self.where_allowed = where
        self.join_allowed = join
        self.select_allowed = select
        self.null_allowed = nullable
        self.kwargs = kwargs

    def validate_data_type(self, data):
        """validate_data_type."""
        if self.null_allowed and data is None:
            return True, data
        try:
            return True, self.data_type_validator(data)
        except Exception:
            return False, None

    def _custom_validation(self, data):
        pass


class IntColumn(BaseColumn):
    """IntColumn."""
    data_type_validator = int

    def _custom_validation(self, data):
        if not self.kwargs.get("allow_negative") and data < 0:
            return False, "negative value is not allowed"


class FloatColumn(BaseColumn):
    """FloatColumn."""
    data_type_validator = float


class StringColumn(BaseColumn):
    """StringColumn."""
    data_type_validator = str


class JsonArrayColumn(BaseColumn):
    """JsonArrayColumn."""
    data_type_validator = list


class JsonObjectColumn(BaseColumn):
    """JsonObjectColumn."""
    data_type_validator = dict
