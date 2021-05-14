from constants.core.indexes import CoreIndexConstants
from exceptions.core.indexes import InvalidIndexPropertyException


class CoreIndex:
    """CoreIndex."""
    __slots__ = CoreIndexConstants.core_index_slots
    default_properties_map = CoreIndexConstants.core_index_default_values

    def __init__(
        self,  **kwargs
    ):
        """Init."""
        for index_property, property_value in self.default_properties_map.items():
            setattr(self, index_property, property_value)

        invalid_properties = list()
        for index_property, property_value in kwargs.items():
            if index_property not in self.__slots__:
                invalid_properties.append(index_property)

        if invalid_properties:
            raise InvalidIndexPropertyException(invalid_properties)
        self._validate_index_initialisation()

    def _add_table_refrence(self, tablecls):
        self.table = tablecls

    def _set_index_name(self, default_index_name):
        self.index_name = self.index_name or default_index_name

    def _validate_index_initialisation(self):
        pass

    def _generate_index_definition(self):
        """_generate_index_definition."""
        self.index_definition = ""


class CoreSQLIndex(CoreIndex):
    pass
