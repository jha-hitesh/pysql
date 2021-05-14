import asyncio
import time

from config import MYSQL_CONFIG
from constants.core.others import SQL_FUNCTION_CONFIG_MAP
from exceptions.mysql.connections import MysqlConnectionPoolExhausted, MySQLPartialSQLInterrupted
import mysql.connector
from ordered_set import OrderedSet


class MysqlConnector:
    """MysqlConnector."""
    @staticmethod
    def get_raw_connection():
        """get_raw_connection."""
        return mysql.connector.connect(
            host=MYSQL_CONFIG["host"],
            port=MYSQL_CONFIG["port"],
            user=MYSQL_CONFIG["user"],
            password=MYSQL_CONFIG["password"],
            database=MYSQL_CONFIG["database"],
            ssl_disabled=MYSQL_CONFIG["ssl_disabled"],
            autocommit=MYSQL_CONFIG["autocommit"]
        )

    @staticmethod
    def return_raw_connection(connection_obj):
        """return_raw_connection."""
        connection_obj.cursor.close()


class ConnectionPool():
    """ConnectionPool."""
    def __init__(self, *args, **kwargs):
        """__init__."""
        self.is_dead = False
        self.pool_size = kwargs.get("pool_size") or 10
        self.connection_wait_retries = int(kwargs.get("connection_wait_retries", 5))
        self.connection_wait_time = int(kwargs.get("connection_wait_time", 2))
        self.idle_connections = OrderedSet()
        self.used_connections = OrderedSet()
        for connection_number in range(self.pool_size):
            self.idle_connections.add(MysqlConnector.get_raw_connection())

    async def get_connection_from_pool_async(self):
        """get_connection_from_pool_async."""
        retry = 0
        while True:
            if not len(self.idle_connections):
                retry += 1
                if retry > self.connection_wait_retries:
                    raise MysqlConnectionPoolExhausted("no idle connection available")
                asyncio.sleep(self.connection_wait_time)
                continue
            idle_connection = self.idle_connections[0]
            self.idle_connections.remove(idle_connection)
            self.used_connections.add(idle_connection)
            return idle_connection
        raise MysqlConnectionPoolExhausted("no idle connection available")

    async def return_connection_to_pool_async(self, connection_obj):
        """return_connection_to_pool_async."""
        if connection_obj in self.used_connections:
            self.used_connections.remove(connection_obj)
        self.idle_connections.add(connection_obj)

    def return_connection_to_pool(self, connection_obj):
        """return_connection_to_pool."""
        if connection_obj in self.used_connections:
            self.used_connections.remove(connection_obj)
        self.idle_connections.add(connection_obj)

    def get_connection_from_pool(self):
        """get_connection_from_pool."""
        retry = 0
        while True:
            if not len(self.idle_connections):
                retry += 1
                if retry > self.connection_wait_retries:
                    raise MysqlConnectionPoolExhausted("no idle connection available")
                time.sleep(self.connection_wait_time)
                continue
            idle_connection = self.idle_connections[0]
            self.idle_connections.remove(idle_connection)
            self.used_connections.add(idle_connection)
            return idle_connection
        raise MysqlConnectionPoolExhausted("no idle connection available")

    def close_connections(self):
        """close_connections."""
        for connection_obj in self.idle_connections:
            connection_obj.close()
        # TODO: Implement closing used connection here.


class MysqlQueryManager:
    """MysqlQueryManager."""

    def __init__(
        self, connection_pool=None
    ):
        """__init__."""
        self.current_sql_keyword_used = ""
        self.allowed_sql_functions_config = SQL_FUNCTION_CONFIG_MAP
        self.current_sql_formation = list()
        self.pending_sql_statements = list()
        self.cursor_object = None
        self.connection_obj = None
        if connection_pool:
            self.get_connection = connection_pool.get_connection_from_pool
            self.return_connection = connection_pool.return_connection_to_pool
        else:
            self.get_connection = MysqlConnector.get_raw_connection
            self.return_connection = MysqlConnector.return_raw_connection

    def __getattr__(self, attr):
        if attr in self.allowed_sql_functions_config["NEXT_FUNCTIONS"]:
            self.current_sql_keyword_used = attr
            return self._perform_sql_keyword_operation
        else:
            return super().a.__getattribute__(attr)

    def _generate_sql(self):
        self.current_sql_formation.append(";")
        self.pending_sql_statements.append(" ".join(self.current_sql_formation))
        self.clear_partial_sql()

    def _perform_sql_keyword_operation(self, *args):
        if self.current_sql_keyword_used not in self.allowed_sql_functions_config["NEXT_FUNCTIONS"]:
            raise MySQLPartialSQLInterrupted(
                "{0} not permitted in the middle of sql formation, issue clear_partial_sql first"
            )
        self.allowed_sql_functions_config = self.allowed_sql_functions_config["NEXT_FUNCTIONS"][self.current_sql_keyword_used]  # noqa: E501
        self.current_sql_formation.append(self.allowed_sql_functions_config["BLOCK_START"])
        for object_refrence in args:
            if type(object_refrence) == str:
                self.current_sql_formation.append(object_refrence)
            if not hasattr(object_refrence, self.current_sql_keyword_used):
                raise Exception("invalid object")
            self.current_sql_formation.append(getattr(object_refrence, self.current_sql_keyword_used)())
        self.current_sql_formation.append(self.allowed_sql_functions_config["BLOCK_END"])
        if not self.allowed_sql_functions_config["NEXT_FUNCTIONS"]:
            self._generate_sql()
        return self

    def CLOSE(self, *args):
        """close."""
        if self.connection_obj:
            self.return_connection(self.connection_obj)

    def execute(self, *args):
        if not self.cursor_object:
            self.connection_obj = self.get_connection()
            self.cursor_object = self.connection_obj.cursor()
        for sql in self.pending_sql_statements:
            self.cursor_object.execute(sql)

    def clear_partial_sql(self, *args):
        self.allowed_sql_functions_config = SQL_FUNCTION_CONFIG_MAP
        self.current_sql_formation = list()

