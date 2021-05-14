class CoreColumnConstants:
    core_column_slots = (
        "table", "column_name", "select", "where", "join",
        "NOT_NULL", "DEFAULT", "column_definition"
    )
    core_properties_default_values = {
        "table": None,
        "column_name": None,
        "column_definition": "",
        "select": True,
        "where": True,
        "join": True,
        "NOT_NULL": False,
        "DEFAULT": None,
    }

