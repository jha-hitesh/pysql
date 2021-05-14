from constants.core.constraints import CoreConstraintConstants
from exceptions.core.constraints import InvalidConstraintPropertyException
from exceptions.core.base import UnSupportedException
from orm.core.columns import CoreSQLColumn
from orm.core.tables import TableMetaClass


class CoreConstraint:
    """CoreConstraint."""
    __slots__ = CoreConstraintConstants.core_constraint_slots
    default_properties_map = CoreConstraintConstants.core_constraint_default_values

    def __init__(
        self,  **kwargs
    ):
        """Init."""
        for constraint_property, property_value in self.default_properties_map.items():
            setattr(self, constraint_property, property_value)

        invalid_properties = list()
        for constraint_property, property_value in kwargs.items():
            if constraint_property not in self.__slots__:
                invalid_properties.append(constraint_property)

        if invalid_properties:
            raise InvalidConstraintPropertyException(invalid_properties)

    def _add_table_refrence(self, tablecls):
        self.table = tablecls

    def _set_constraint_name(self, default_constraint_name):
        self.constraint_name = self.constraint_name or default_constraint_name

    def _generate_constraint_definition(self):
        pass


class CoreSQLConstraint(CoreConstraint):

    CONSTRAINT_VALIDATOR_MAP = {
        "UNIQUE": "_generate_unique_constraint_definition",
        "PRIMARY_KEY": "_generate_primary_key_constraint_definition",
        "FOREIGN_KEY": "_generate_foreign_key_constraint_definition",
        "CHECK": "_generate_check_constraint_definition",
        "DEFAULT": "_generate_default_constraint_definition"
    }

    def _generate_constraint_definition(self):
        primary_constraint_found = False
        invalid_properties = list()
        for constraint in self.CONSTRAINT_VALIDATOR_MAP.keys():
            if getattr(self, constraint):
                if primary_constraint_found:
                    invalid_properties.append(constraint)
                else:
                    self.constraint_definition = getattr(self, self.CONSTRAINT_VALIDATOR_MAP[constraint])()
                    primary_constraint_found = True
        if invalid_properties:
            raise InvalidConstraintPropertyException(invalid_properties)

    def _generate_unique_constraint_definition(self):
        if type(self.UNIQUE) not in [tuple, list]:
            raise InvalidConstraintPropertyException(
                "UNIQUE must be either a list or a tuple"
            )
        if len(self.UNIQUE) == 0:
            raise InvalidConstraintPropertyException(
                "UNIQUE must be a combination of columns"
            )
        column_names = list()
        for column_property in self.UNIQUE:
            if type(column_property) == str and column_property in TableMetaClass._table_column_names_map[self.table]:
                column_names.append(column_property)
                continue
            if column_property not in TableMetaClass._table_columns_map[self.table]:
                raise InvalidConstraintPropertyException(
                    "all columns in UNIQUE must be from current table"
                )
            column_names.append(column_property.column_name)
        self.constraint_definition = " ".join(
            "CONSTRAINT", self.constraint_name, "UNIQUE", "(",
            ",".join(column_names), ")"
        )

    def _generate_primary_key_constraint_definition(self):
        if type(self.PRIMARY_KEY) not in [tuple, list]:
            raise InvalidConstraintPropertyException(
                "PRIMARY_KEY must be either a list or a tuple"
            )
        if len(self.PRIMARY_KEY) == 0:
            raise InvalidConstraintPropertyException(
                "PRIMARY_KEY must be a combination of columns"
            )
        column_names = list()
        for column_property in self.PRIMARY_KEY:
            if type(column_property) == str and column_property in TableMetaClass._table_column_names_map[self.table]:
                column_names.append(column_property)
                continue
            if column_property not in TableMetaClass._table_columns_map[self.table]:
                raise InvalidConstraintPropertyException(
                    "all columns in PRIMARY_KEY must be from current table"
                )
            column_names.append(column_property.column_name)
        self.constraint_definition = " ".join(
            "CONSTRAINT", self.constraint_name, "PRIMARY KEY", "(",
            ",".join(column_names), ")"
        )

    def _generate_foreign_key_constraint_definition(self):
        foreign_key_column_name = ""
        if type(self.FOREIGN_KEY) == str and self.FOREIGN_KEY in TableMetaClass._table_column_names_map[self.table]:
            foreign_key_column_name = self.FOREIGN_KEY
        elif not (
            isinstance(self.FOREIGN_KEY, CoreSQLColumn) and
            self.FOREIGN_KEY in TableMetaClass._table_columns_map[self.table]
        ):
            raise InvalidConstraintPropertyException(
                "FOREIGN_KEY must be a column from current table"
            )

        foreign_key_column_name = self.FOREIGN_KEY.column_name

        if not (
            isinstance(self.REFERENCES, CoreSQLColumn) and
            self.REFERENCES not in TableMetaClass._table_columns_map[self.table]
        ):
            raise InvalidConstraintPropertyException(
                "REFERENCES must be a column from other table"
            )

        self.constraint_definition = " ".join(
            "CONSTRAINT", self.constraint_name, "FOREIGN KEY",
            "(", foreign_key_column_name, ")", "REFERENCES",
            self.REFERENCES.table._table_name_, "(", self.REFERENCES.column_name, ")"
        )

    def _generate_default_constraint_definition(self):
        for_column_name = ""
        if type(self.FOR) == str and self.FOR in TableMetaClass._table_column_names_map[self.table]:
            for_column_name = self.FOR
        elif not (
            isinstance(self.FOR, CoreSQLColumn) and
            self.FOR in TableMetaClass._table_columns_map[self.table]
        ):
            raise InvalidConstraintPropertyException(
                "FOR must be a column from current table"
            )

        for_column_name = self.FOR.column_name

        # TODO: validate default value here

        self.constraint_definition = " ".join(
            "CONSTRAINT", self.constraint_name, "DEFAULT",
            self.DEFAULT, "FOR", for_column_name
        )

    def _generate_check_constraint_definition(self):
        # TODO: validate check values here
        if type(self.CHECK) == str:
            self.constraint_definition = " ".join(
                "CONSTRAINT", self.constraint_name, "CHECK", self.CHECK
            )
        else:
            raise UnSupportedException("not implemented yet")
        # TODO: add generate check from column relation here
