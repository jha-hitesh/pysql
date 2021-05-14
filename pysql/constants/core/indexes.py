class CoreIndexConstants:
    core_index_slots = (
        "table", "index_name", "index_definition",
        "UNIQUE"
    )
    core_index_default_values = {
        "table": None,
        "index_name": None,
        "index_definition": "",
        "UNIQUE": False
    }

