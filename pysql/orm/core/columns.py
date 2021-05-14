from constants.core.columns import CoreColumnConstants
from exceptions.core.columns import InvalidColumnPropertyException


class CoreColumn:
    """CoreColumn."""
    __slots__ = CoreColumnConstants.core_column_slots
    default_properties_map = CoreColumnConstants.core_properties_default_values
    data_type_validator = None
    data_type_error_msg = "Invalid data type detected"
    db_data_type = ""

    def __init__(
        self,  **kwargs
    ):
        """Init."""
        for column_property, property_value in self.default_properties_map.items():
            setattr(self, column_property, property_value)

        invalid_properties = list()
        for column_property, property_value in kwargs.items():
            if column_property not in self.__slots__:
                invalid_properties.append(column_property)

        if invalid_properties:
            raise InvalidColumnPropertyException(invalid_properties)
        self._validate_column_initialisation()

    def _add_table_refrence(self, tablecls):
        self.table = tablecls

    def _set_column_name(self, default_column_name):
        self.column_name = self.column_name or default_column_name

    def _validate_column_initialisation(self):
        pass

    def validate_data_type(self, data):
        """validate_data_type."""
        if not self.NOT_NULL and data is None:
            return True, data
        try:
            return True, self.data_type_validator(data)
        except Exception:
            return False, None


class CoreSQLColumn(CoreColumn):

    def __init__(self, *args, **kwargs):
        """__init__."""
        super().__init__(*args, **kwargs)

    def _generate_column_definition(self):
        """_generate_column_definition."""
        keywords = [self.column_name, self.db_data_type]
        if self.NOT_NULL:
            keywords.append("NOT NULL")
        if self.UNIQUE:
            keywords.append("UNIQUE")
        if self.DEFAULT:
            keywords.append("DEFAULT {0}".format(self.DEFAULT))
        self.column_definition = " ".join(keywords)

    def ADD_COLUMN(self):
        return self.column_definition

    def DROP_COLUMN(self):
        return self.column_name

    def ALTER_COLUMN(self):
        return self.column_definition

    def INSERT_INTO(self):
        return self.column_name

    def ON(self):
        return self.column_name

    def SELECT(self):
        """select."""
        return self.column_name

    def AS_SELECT(self):
        """as select."""
        return self.column_name

    def SELECT_DISTINCT(self):
        return self.column_name


class StarColumn(CoreSQLColumn):
    """StarColumn."""
    pass


class NumericColumn(CoreSQLColumn):
    pass


class SmallMoneyColumn(CoreSQLColumn):
    pass


class MoneyColumn(CoreSQLColumn):
    pass


class RealColumn(CoreSQLColumn):
    pass
