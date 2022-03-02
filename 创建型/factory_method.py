# !/usr/bin/env python 
# -*- coding: utf-8 -*-

# -----------#
# 工厂模式: 定义一个用于创建对象的接口，让子类决定实例化哪一个类 
# -----------#


from abc import ABC, abstractmethod


class DatabaseWapper:
    """
    定义一个数据库操作类
    """
    @abstractmethod
    def create_connection(self) -> 'Connection':
        """
        生成一个数据库连接对象
        """
        raise NotImplementedError('`create_connection()` must be implemented.')
    

    def execute_sql(self, sql):
        conn = self.create_connection()
        conn.check(sql)
        return conn.execute(sql)
    


class MySQLDatabaseWapper(DatabaseWapper):

    def create_connection(self) -> 'Connection':
        return MySQLConnection()


class OracleDatabaseWapper(DatabaseWapper):

    def create_connection(self) -> 'Connection':
        return OracleConnection()


class Connection(ABC):

    @abstractmethod
    def check(self, sql) -> None:
        pass

    @abstractmethod
    def execute(self, sql) -> None:
        pass

class MySQLConnection(Connection):

    def check(self, sql) -> None:
        print("mysql语句检查通过")

    def execute(self, sql) -> None:
        print("mysql语句执行成功")


class OracleConnection(Connection):

    def check(self, sql) -> None:
        print("oracle语句检查通过")

    def execute(self, sql) -> None:
        print("oracle语句执行成功")


# 应用级别的代码
class QueryApp:
    
    def __init__(self, sql_type):
        
        self.database_client = None
        if sql_type == "mysql":
            self.database_client = MySQLDatabaseWapper()
        elif sql_type == "oracle":
            self.database_client = OracleDatabaseWapper()
        
        assert self.database_client, "database_client must not None"

    @property
    def query(self):
        return self.database_client.execute_sql("select * from users;")


if __name__ == "__main__":

    mysql_query = QueryApp("mysql")
    print(mysql_query.query)

    orcle_query = QueryApp("oracle")
    print(mysql_query.query)