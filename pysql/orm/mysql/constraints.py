from constants.mysql.constraints import MysqlConstraintConstants
from orm.core.constraints import CoreSQLConstraint


class MySQLConstraint(CoreSQLConstraint):

    __slots__ = MysqlConstraintConstants.mysql_constraint_slots
    default_properties_map = MysqlConstraintConstants.mysql_constraint_default_values

    CONSTRAINT_VALIDATOR_MAP = {
        "UNIQUE": "_generate_unique_constraint_definition",
        "PRIMARY_KEY": "_generate_primary_key_constraint_definition",
        "FOREIGN_KEY": "_generate_foreign_key_constraint_definition",
        "CHECK": "_generate_check_constraint_definition"
    }
