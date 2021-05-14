from constants.core.columns import CoreColumnConstants


class MysqlColumnConstants:
    """MysqlColumnConstants."""
    INT_COLUMN_SLOTS = CoreColumnConstants.core_column_slots + (
        "DISPLAY_WIDTH", "AUTO_INCREMENT", "UNSIGNED", "ZEROFILL"
    )
    INT_COLUMN_DEFAULT_PROPERTIES_VALUE = {
        "DISPLAY_WIDTH": None,
        "AUTO_INCREMENT": False,
        "UNSIGNED": False,
        "ZEROFILL": False,
        **CoreColumnConstants.core_properties_default_values
    }

    BIT_COLUMN_SLOTS = CoreColumnConstants.core_column_slots + (
        "MAX_BIT"
    )
    BIT_COLUMN_DEFAULT_PROPERTIES_VALUE = {
        "MAX_BIT": 1,
        **CoreColumnConstants.core_properties_default_values
    }

    BOOLEAN_COLUMN_SLOTS = CoreColumnConstants.core_column_slots
    BOOLEAN_COLUMN_DEFAULT_PROPERTIES_VALUE = CoreColumnConstants.core_properties_default_values

    FLOAT_COLUMN_SLOTS = CoreColumnConstants.core_column_slots + (
        "MAX_DIGITS", "DECIMAL_POINTS"
    )
    FLOAT_COLUMN_DEFAULT_PROPERTIES_VALUE = {
        "MAX_DIGITS": 10,
        "DECIMAL_POINTS": 0,
        **CoreColumnConstants.core_properties_default_values
    }
