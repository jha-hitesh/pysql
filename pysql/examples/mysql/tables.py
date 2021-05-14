from orm.mysql.tables import MysqlTable
from orm.mysql.columns import FloatColumn, IntColumn
from orm.mysql.constraints import MySQLConstraint
from orm.mysql.connections import ConnectionPool, MysqlQueryManager


class Employee(MysqlTable):
    """Employee."""
    _table_name_ = "employee"
    id = IntColumn(NOT_NULL=True, AUTO_INCREMENT=True, UNSIGNED=True)
    emp_id = IntColumn(NOT_NULL=True, UNSIGNED=True)
    age = IntColumn(NOT_NULL=True, DEFAULT=15, UNSIGNED=True)
    leave_balance = FloatColumn(MAX_DIGITS=3, DECIMAL_POINTS=1, DEFAULT=0.0)
    meal_coupon_balance = FloatColumn()
    balance_check = MySQLConstraint(CHECK="(leave_balance<=30)")


def test_table_creation():

    connection_pool = ConnectionPool(
        pool_size=1, connection_wait_retries=5, connection_wait_time=3
    )
    orm_connection = MysqlQueryManager(connection_pool=connection_pool)
    orm_connection.START_TRANSACTION()
    orm_connection.CREATE_TABLE(Employee)
    orm_connection.CREATE_TABLE_IF_NOT_EXISTS(Employee)
    orm_connection.ALTER_TABLE(Employee).DROP_COLUMN(Employee.id).execute()
    orm_connection.ALTER_TABLE(Employee).ADD_COLUMN(Employee.id).execute()
    orm_connection.ALTER_TABLE(Employee).ALTER_COLUMN(Employee.id).execute()
    orm_connection.COMMIT()
    orm_connection.CLOSE()
    connection_pool.close_connections()
