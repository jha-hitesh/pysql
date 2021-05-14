from collections import defaultdict

from .columns import CoreColumn, StarColumn
from .constraints import CoreConstraint
from .indexes import CoreIndex


class TableMetaClass(type):
    """TableMetaClass."""
    _table_columns_map = defaultdict(set)
    _table_column_names_map = defaultdict(set)

    _table_constraints_map = defaultdict(set)
    _table_constraint_names_map = defaultdict(set)

    _table_indexes_map = defaultdict(set)
    _table_index_names_map = defaultdict(set)

    def __new__(metacls, name, bases, attrs):
        """__new__."""
        if "_table_name_" not in attrs:
            attrs["_table_name_"] = name
        cls = super().__new__(metacls, name, bases, attrs)
        for attr_name, attr_value in attrs.items():
            if isinstance(attr_value, CoreColumn):
                attr_value._add_table_refrence(cls)
                attr_value._set_column_name(attr_name)
                attr_value._generate_column_definition()
                metacls._table_columns_map[cls].add(attr_value)
                metacls._table_column_names_map[cls].add(attr_value.column_name)
            elif isinstance(attr_value, CoreConstraint):
                attr_value._add_table_refrence(cls)
                attr_value._set_constraint_name(attr_name)
                attr_value._generate_constraint_definition()
                metacls._table_constraints_map[cls].add(attr_value)
                metacls._table_constraint_names_map[cls].add(attr_value.constraint_name)
            elif isinstance(attr_value, CoreIndex):
                attr_value._add_table_refrence(cls)
                attr_value._set_index_name(attr_name)
                attr_value._generate_index_definition()
                metacls._table_indexes_map[cls].add(attr_value)
                metacls._table_index_names_map[cls].add(attr_value.index_name)
        return cls


class CoreTable(metaclass=TableMetaClass):
    """CoreTable."""
    pass


class CoreSQLTable(CoreTable):
    _all_columns_ = StarColumn()

    @classmethod
    def CREATE_TABLE(cls):
        return cls.get_create_table_sql()

    @classmethod
    def CREATE_TABLE_IF_NOT_EXISTS(cls):
        return cls.get_create_table_sql()

    @classmethod
    def ALTER_TABLE(cls):
        return cls._table_name_

    @classmethod
    def DROP_TABLE(cls):
        return cls._table_name_

    @classmethod
    def INSERT_INTO(cls):
        return cls._table_name_

    @classmethod
    def UPDATE_TABLE(cls):
        return cls._table_name_

    @classmethod
    def DELETE_FROM(cls):
        return cls._table_name_

    @classmethod
    def FROM(cls):
        return cls._table_name_

    @classmethod
    def get_create_table_sql(cls, **kwargs):
        """get_create_table_sql."""
        column_definitions = list()
        for column_value in TableMetaClass._table_columns_map[cls]:
            column_definitions.append(column_value.column_definition)
        columns_creation_subquery_string = ",".join(column_definitions)
        return " ".join((
            cls._table_name_, "(", columns_creation_subquery_string, ")"
        ))
