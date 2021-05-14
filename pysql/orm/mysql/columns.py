from constants.mysql.columns import MysqlColumnConstants
from orm.core.columns import CoreSQLColumn


class MySQLColumn(CoreSQLColumn):

    def _generate_column_definition(self):
        """_generate_column_definition."""
        keywords = [self.column_name, self.db_data_type]
        if self.NOT_NULL:
            keywords.append("NOT NULL")
        if self.DEFAULT:
            keywords.append("DEFAULT {0}".format(self.DEFAULT))
        self.column_definition = " ".join(keywords)


class BitColumn(MySQLColumn):
    __slots__ = MysqlColumnConstants.BIT_COLUMN_SLOTS
    default_properties_map = MysqlColumnConstants.BIT_COLUMN_DEFAULT_PROPERTIES_VALUE
    data_type_validator = None
    db_data_type = "BIT"

    def _generate_column_definition(self):
        """_generate_column_definition."""
        keywords = [self.column_name, "BIT({0})".format(self.bit_limit)]
        if self.NOT_NULL:
            keywords.append("NOT NULL")
        if self.DEFAULT:
            keywords.append("DEFAULT {0}".format(self.DEFAULT))
        self.column_definition = " ".join(keywords)


class BooleanColumn(MySQLColumn):
    __slots__ = MysqlColumnConstants.BOOLEAN_COLUMN_SLOTS
    default_properties_map = MysqlColumnConstants.BOOLEAN_COLUMN_DEFAULT_PROPERTIES_VALUE
    data_type_validator = bool
    db_data_type = "BOOLEAN"


class IntColumn(MySQLColumn):
    __slots__ = MysqlColumnConstants.INT_COLUMN_SLOTS
    default_properties_map = MysqlColumnConstants.INT_COLUMN_DEFAULT_PROPERTIES_VALUE
    data_type_validator = int
    db_data_type = "INT"

    def _generate_column_definition(self):
        """_generate_column_definition."""
        keywords = [self.column_name, self.db_data_type]
        if self.NOT_NULL:
            keywords.append("NOT NULL")
        if self.AUTO_INCREMENT:
            keywords.append("AUTO INCREMENT")
        if self.UNSIGNED:
            keywords.append("UNSIGNED")
        if self.ZEROFILL:
            keywords.append("ZEROFILL")
        if self.DEFAULT:
            keywords.append("DEFAULT {0}".format(self.DEFAULT))
        self.column_definition = " ".join(keywords)


class TinyIntColumn(IntColumn):
    db_data_type = "TINYINT"


class SmallIntColumn(IntColumn):
    db_data_type = "SMALLINT"


class MediumIntColumn(IntColumn):
    db_data_type = "MEDIUMINT"


class BigIntColumn(IntColumn):
    db_data_type = "BIGINT"


class FloatColumn(MySQLColumn):
    __slots__ = MysqlColumnConstants.FLOAT_COLUMN_SLOTS
    default_properties_map = MysqlColumnConstants.FLOAT_COLUMN_DEFAULT_PROPERTIES_VALUE
    data_type_validator = float
    db_data_type = "FLOAT"

    def _generate_column_definition(self):
        """_generate_column_definition."""
        keywords = [
            self.column_name,
            "{0}({1},{2})".format(
                self.db_data_type, self.MAX_DIGITS, self.DECIMAL_POINTS
            )
        ]
        if self.NOT_NULL:
            keywords.append("NOT NULL")
        if self.AUTO_INCREMENT:
            keywords.append("AUTO INCREMENT")
        if self.UNSIGNED:
            keywords.append("UNSIGNED")
        if self.ZEROFILL:
            keywords.append("ZEROFILL")
        if self.DEFAULT:
            keywords.append("DEFAULT {0}".format(self.DEFAULT))
        self.column_definition = " ".join(keywords)


class DoubleColumn(FloatColumn):
    db_data_type = "DOUBLE"


class DecimalColumn(FloatColumn):
    db_data_type = "DECIMAL"
