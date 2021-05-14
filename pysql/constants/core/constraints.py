class CoreConstraintConstants:
    core_constraint_slots = (
        "table", "constraint_name", "constraint_definition",
        "UNIQUE", "PRIMARY_KEY", "FOREIGN_KEY", "REFERENCES",
        "CHECK", "DEFAULT", "FOR"
    )
    core_constraint_default_values = {
        "table": None,
        "constraint_name": None,
        "constraint_definition": "",
        "UNIQUE": (),
        "PRIMARY_KEY": (),
        "FOREIGN_KEY": None,
        "REFERENCES": None,
        "CHECK": (),
        "DEFAULT": None,
        "FOR": None
    }

