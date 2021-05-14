class SQLKeywords:
    # DDL KEYWORDS
    CREATE_TABLE = "CREATE TABLE"
    ALTER_TABLE = "ALTER_TABLE"
    DROP_TABLE = "DROP TABLE"
    ADD = "ADD"
    DROP_COLUMN = "DROP COLUMN"
    # DML KEYWORDS
    INSERT_INTO = "INSERT_INTO"
    UPDATE_TABLE = "UPDATE TABLE"
    DELETE_FROM = "DELETE FROM"
    FROM = "FROM"
    SELECT = "SELECT"
    SELECT_DISTINCT = "SELECT DISTINCT"
    DISTINCT = "DISTINCT"
    SET = "SET"
    TRUNCATE = "TRUNCATE"
    AS = "AS"
    ORDER_BY = "ORDER BY"
    GROUP_BY = "GROUP BY"
    ASC = "ASC"
    DESC = "DESC"
    WHERE = "WHERE"
    BETWEEN = "BETWEEN"
    HAVING = "HAVING"
    LIKE = "LIKE"
    IN = "IN"
    AND = "AND"
    OR = "OR"
    IS_NULL = "IS NULL"
    LIMIT = "LIMIT"
    JOIN = "JOIN"
    UNION = "UNION"
    UNION_ALL = "UNION ALL"
    EXISTS = "EXISTS"
    CASE = "CASE"


class FilterConstants:
    """FilterConstants."""
    OR = "or"
    AND = "and"
    IN = "in"
    NOT_IN = "notin"
    IS_NOT = "isnot"
    VALIDATOR = "validator"
    MAX_LENGTH = ""
    MIN_LENGTH = ""
    OPTIONS = ""
    ERROR_MSG = ""
    VALIDATED_VALUE = ""
    IS_SUCCESS = ""
    NOT_ALLOWED_FILTER_KEY_MSG = "filtering with {0} is not allowed on {1}"
    NOT_ALLOWED_FILTER_VALUE_MSG = "Invalid filter value for {0}, data_type should be {1}"
    NOT_ALLOWED_FILTER_VALUE_IN_ARRAY_MSG = "Filter values in array for {0} needs to be of {1} data_type"
    INVALID_FILTER_VALUE_MSG = "Invalid filter value for given filter key"


class URLConstants:
    """URLConstants."""
    TABLE = "table"
    WHERE = "where"
    SELECT = "select"
    PAGE_NO = "page_no"
    PAGE_SIZE = "page_size"
    ORDER_BY = "order_by"

    URL_PARAMS_TO_IDENTIFIER_MAP = {
        "table": "table:",
        "where": "where:",
        "select": "select:",
        "page_no": "page_no:",
        "page_size": "page_size:",
        "order_by": "order_by:"
    }


SQL_FUNCTION_CONFIG_MAP = {
    "BLOCK_START": "",
    "BLOCK_END": "",
    "NEXT_FUNCTIONS": {
        "START_TRANSACTION": {
            "BLOCK_START": "START TRANSACTION",
            "BLOCK_END": "",
            "NEXT_FUNCTIONS": None
        },
        "COMMIT": {
            "BLOCK_START": "COMMIT",
            "BLOCK_END": "",
            "NEXT_FUNCTIONS": None
        },
        "ROLLBACK": {
            "BLOCK_START": "ROLLBACK",
            "BLOCK_END": "",
            "NEXT_FUNCTIONS": None
        },
        "CLOSE": {
            "BLOCK_START": "CLOSE",
            "BLOCK_END": "",
            "NEXT_FUNCTIONS": None
        },
        "CREATE_TABLE": {
            "BLOCK_START": "CREATE TABLE",
            "BLOCK_END": "",
            "NEXT_FUNCTIONS": None
        },
        "ALTER_TABLE": {
            "BLOCK_START": "ALTER TABLE",
            "BLOCK_END": "",
            "NEXT_FUNCTIONS": {
                "ADD": {
                    "BLOCK_START": "ADD",
                    "BLOCK_END": "",
                    "NEXT_FUNCTIONS": None
                },
                "DROP_COLUMN": {
                    "BLOCK_START": "DROP COLUMN",
                    "BLOCK_END": "",
                    "NEXT_FUNCTIONS": None
                },
                "MODIFY_COLUMN": {
                    "BLOCK_START": "MODIFY COLUMN",
                    "BLOCK_END": "",
                    "NEXT_FUNCTIONS": None
                },
                "MODIFY": {
                    "BLOCK_START": "MODIFY",
                    "BLOCK_END": "",
                    "NEXT_FUNCTIONS": {
                        "DEFAULT": {
                            "BLOCK_START": "DEFAULT",
                            "BLOCK_END": "",
                            "NEXT_FUNCTIONS": None
                        }
                    }
                },
                "ALTER_COLUMN": {
                    "BLOCK_START": "ALTER",
                    "BLOCK_END": "",
                    "NEXT_FUNCTIONS": {
                        "SET_DEFAULT": {
                            "BLOCK_START": "SET DEFAULT",
                            "BLOCK_END": "",
                            "NEXT_FUNCTIONS": None
                        },
                        "DROP DEFAULT": {
                            "BLOCK_START": "DROP DEFAULT",
                            "BLOCK_END": "",
                            "NEXT_FUNCTIONS": None
                        }
                    }
                },
                "ALTER": {
                    "BLOCK_START": "ALTER",
                    "BLOCK_END": "",
                    "NEXT_FUNCTIONS": {
                        "SET_DEFAULT": {
                            "BLOCK_START": "SET DEFAULT",
                            "BLOCK_END": "",
                            "NEXT_FUNCTIONS": None
                        },
                        "DROP DEFAULT": {
                            "BLOCK_START": "DROP DEFAULT",
                            "BLOCK_END": "",
                            "NEXT_FUNCTIONS": None
                        }
                    }
                },
                "ADD_CONSTRAINT": {
                    "BLOCK_START": "ADD CONSTRAINT",
                    "BLOCK_END": "",
                    "NEXT_FUNCTIONS": {
                        "UNIQUE": {
                            "BLOCK_START": "UNIQUE (",
                            "BLOCK_END": ")",
                            "NEXT_FUNCTIONS": None
                        },
                        "PRIMARY_KEY": {
                            "BLOCK_START": "PRIMARY KEY (",
                            "BLOCK_END": ")",
                            "NEXT_FUNCTIONS": None
                        },
                        "FOREIGN_KEY": {
                            "BLOCK_START": "FOREIGN KEY (",
                            "BLOCK_END": ")",
                            "NEXT_FUNCTIONS": {
                                "REFERENCES": {
                                    "BLOCK_START": "REFERENCES",
                                    "BLOCK_END": "",
                                    "NEXT_FUNCTIONS": None
                                }
                            }
                        },
                        "CHECK": {
                            "BLOCK_START": "CHECK",
                            "BLOCK_END": "",
                            "NEXT_FUNCTIONS": None
                        },
                        "DEFAULT": {
                            "BLOCK_START": "DEFAULT",
                            "BLOCK_END": "",
                            "NEXT_FUNCTIONS": {
                                "FOR": {
                                    "BLOCK_START": "FOR",
                                    "BLOCK_END": "",
                                    "NEXT_FUNCTIONS": None
                                }
                            }
                        },
                    }
                },
                "DROP_CONSTRAINT": {
                    "BLOCK_START": "DROP CONSTRAINT",
                    "BLOCK_END": "",
                    "NEXT_FUNCTIONS": None
                },
                "DROP_CHECK": {
                    "BLOCK_START": "DROP CHECK",
                    "BLOCK_END": "",
                    "NEXT_FUNCTIONS": None
                },
                "DROP_INDEX": {
                    "BLOCK_START": "DROP INDEX",
                    "BLOCK_END": "",
                    "NEXT_FUNCTIONS": None
                },
                "ADD_PRIMARY_KEY": {
                    "BLOCK_START": "ADD PRIMARY KEY",
                    "BLOCK_END": "",
                    "NEXT_FUNCTIONS": None
                },
                "ADD_FOREIGN_KEY": {
                    "BLOCK_START": "ADD FOREIGN KEY (",
                    "BLOCK_END": ")",
                    "NEXT_FUNCTIONS": {
                        "REFERENCES": {
                            "BLOCK_START": "REFERENCES",
                            "BLOCK_END": "",
                            "NEXT_FUNCTIONS": None
                        }
                    }
                },
                "ADD_UNIQUE": {
                    "BLOCK_START": "ADD UNIQUE",
                    "BLOCK_END": "",
                    "NEXT_FUNCTIONS": None
                },
                "DROP_PRIMARY_KEY": {
                    "BLOCK_START": "DROP PRIMARY KEY",
                    "BLOCK_END": "",
                    "NEXT_FUNCTIONS": None
                },
                "DROP_FOREIGN_KEY": {
                    "BLOCK_START": "DROP FOREIGN KEY",
                    "BLOCK_END": "",
                    "NEXT_FUNCTIONS": None
                }
            }
        },
        "DROP_TABLE": {
            "BLOCK_START": "DROP TABLE",
            "BLOCK_END": "",
            "NEXT_FUNCTIONS": None
        },
        "CREATE_INDEX": {
            "BLOCK_START": "CREATE INDEX",
            "BLOCK_END": "",
            "NEXT_FUNCTIONS": {
                "ON": {
                    "BLOCK_START": "ON",
                    "BLOCK_END": "",
                    "NEXT_FUNCTIONS": None
                }
            }
        },
        "CREATE_UNIQUE_INDEX": {
            "BLOCK_START": "CREATE UNIQUE INDEX",
            "BLOCK_END": "",
            "NEXT_FUNCTIONS": {
                "ON": {
                    "BLOCK_START": "ON",
                    "BLOCK_END": "",
                    "NEXT_FUNCTIONS": None
                }
            }
        },
        "DROP_INDEX": {
            "BLOCK_START": "DROP INDEX",
            "BLOCK_END": "",
            "NEXT_FUNCTIONS": None
        },
        "CREATE_VIEW": {
            "BLOCK_START": "CREATE VIEW",
            "BLOCK_END": "",
            "NEXT_FUNCTIONS": {
                "AS_SELECT": {
                    "BLOCK_START": "AS SELECT",
                    "BLOCK_END": "",
                    "NEXT_FUNCTIONS": None
                }
            }
        },
        "DROP_VIEW": {
            "BLOCK_START": "DROP VIEW",
            "BLOCK_END": "",
            "NEXT_FUNCTIONS": None
        },
        "INSERT_INTO": {
            "BLOCK_START": "INSERT INTO",
            "BLOCK_END": "",
            "NEXT_FUNCTIONS": {
                "VALUES": {
                    "BLOCK_START": "VALUES (",
                    "BLOCK_END": ")",
                    "NEXT_FUNCTIONS": None
                },
                "SET": {
                    "BLOCK_START": "SET",
                    "BLOCK_END": "",
                    "NEXT_FUNCTIONS": None
                },
            }
        },
        "DELETE_FROM": {
            "BLOCK_START": "DELETE FROM",
            "BLOCK_END": "",
            "NEXT_FUNCTIONS": {
                "WHERE": {
                    "BLOCK_START": "WHERE",
                    "BLOCK_END": "",
                    "NEXT_FUNCTIONS": {
                        "LIMIT": {
                            "BLOCK_START": "LIMIT",
                            "BLOCK_END": "",
                            "NEXT_FUNCTIONS": {
                                "OFFSET": {
                                    "BLOCK_START": "OFFSET",
                                    "BLOCK_END": "",
                                    "NEXT_FUNCTIONS": None
                                }
                            }
                        }
                    }
                }
            }
        },
        "UPDATE": {
            "BLOCK_START": "UPDATE",
            "BLOCK_END": "",
            "NEXT_FUNCTIONS": {
                "SET": {
                    "BLOCK_START": "SET",
                    "BLOCK_END": "",
                    "NEXT_FUNCTIONS": {
                        "WHERE": {
                            "BLOCK_START": "WHERE",
                            "BLOCK_END": "",
                            "NEXT_FUNCTIONS": {
                                "LIMIT": {
                                    "BLOCK_START": "LIMIT",
                                    "BLOCK_END": "",
                                    "NEXT_FUNCTIONS": {
                                        "OFFSET": {
                                            "BLOCK_START": "OFFSET",
                                            "BLOCK_END": "",
                                            "NEXT_FUNCTIONS": None
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        "SELECT": {
            "BLOCK_START": "SELECT",
            "BLOCK_END": "",
            "NEXT_FUNCTIONS": {
                "FROM": {
                    "BLOCK_START": "FROM",
                    "BLOCK_END": "",
                    "NEXT_FUNCTIONS": {
                        "WHERE": {
                            "BLOCK_START": "WHERE",
                            "BLOCK_END": "",
                            "NEXT_FUNCTIONS": {
                                "LIMIT": {
                                    "BLOCK_START": "LIMIT",
                                    "BLOCK_END": "",
                                    "NEXT_FUNCTIONS": {
                                        "OFFSET": {
                                            "BLOCK_START": "OFFSET",
                                            "BLOCK_END": "",
                                            "NEXT_FUNCTIONS": None
                                        }
                                    }
                                }
                            }
                        },
                        "INNER_JOIN": {
                            "BLOCK_START": "INNER JOIN",
                            "BLOCK_END": "",
                            "NEXT_FUNCTIONS": {
                                "ON": {
                                    "BLOCK_START": "ON",
                                    "BLOCK_END": "",
                                    "NEXT_FUNCTIONS": {
                                        "WHERE": {
                                            "BLOCK_START": "WHERE",
                                            "BLOCK_END": "",
                                            "NEXT_FUNCTIONS": {
                                                "LIMIT": {
                                                    "BLOCK_START": "LIMIT",
                                                    "BLOCK_END": "",
                                                    "NEXT_FUNCTIONS": {
                                                        "OFFSET": {
                                                            "BLOCK_START": "OFFSET",
                                                            "BLOCK_END": "",
                                                            "NEXT_FUNCTIONS": None
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
