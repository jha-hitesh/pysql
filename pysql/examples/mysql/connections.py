from orm.mysql.connections import ConnectionPool, MysqlConnector, MysqlQueryManager


def test_mysql_connectors():

    direct_connection = MysqlConnector.get_raw_connection()
    direct_connection.close()
    connection_pool = ConnectionPool(
        pool_size=1, connection_wait_retries=5, connection_wait_time=3
    )
    orm_connection = MysqlQueryManager(connection_pool=connection_pool)
    orm_connection.START_TRANSACTION()
    orm_connection.COMMIT()
    orm_connection.CLOSE()
    connection_pool.close_connections()
