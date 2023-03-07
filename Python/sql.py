"""
Package for communicating with MySQL database
"""
# Standard Imports
import pymysql
import math
from typing import Union


class NoValueExists(Exception):
    """
    Raised when no value exists
    """
    pass


class MultipleValuesExists(Exception):
    """
    Raised when multiple values exist
    """
    pass


class SQL_Client:
    """
    Client for communicating with a MySQL database
    """

    def __init__(self, connection_parameters: dict):
        """
        Initialization function called when class is initialized

        Parameters
        ----------
        connection_parameters: dict
            {
                "host": hostname,
                "database": database name,
                "user": username,
                "password": user password
            }
        """
        self.connection_parameters = connection_parameters
        self.connected = False

    def connect(self):
        """
        Establishes connection with the MySQL Database
        """
        self.connection = pymysql.connect(
            host=self.connection_parameters["host"],
            user=self.connection_parameters["user"],
            password=self.connection_parameters["password"],
            db=self.connection_parameters["database"],
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor,
            connect_timeout=10
        )
        self.connected = True

    def connect_no_database(self):
        """
        Establishes connection with MySQL Database with no database specified
        """
        self.connection = pymysql.connect(
            host=self.connection_parameters["host"],
            user=self.connection_parameters["user"],
            password=self.connection_parameters["password"],
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor,
            connect_timeout=10
        )
        self.connected = True

    def disconnect(self):
        """
        Closes connection with the MySQL Database
        """
        self.connection.close()
        self.connected = False

    def query(self, sql_query: str, query_parameters: list = None, execute_many: bool = False) -> list:
        """
        Performs a query on the MySQL Database

        Parameters
        ----------
        sql_query: str
            The SQL query to perform on the database
        query_parameters: list = None
            Parameters for the SQL query
        execute_many: bool = False
            Whether the query_parameters are a sequence of parameters to execute or not

        Returns
        -------
        list
            A list of dictionaries containing the results of the query

        Notes
        -----
        Example query
        sql_query = "SELECT * FROM table WHERE column = %s
        query_parameters = [column_value]
        """
        close_connection = False
        if not self.connected:
            self.connect()
            close_connection = True
        with self.connection.cursor() as cursor:
            if query_parameters is None:
                cursor.execute(sql_query)
            else:
                if execute_many:
                    cursor.executemany(sql_query, query_parameters)
                else:
                    cursor.execute(sql_query, query_parameters)
            result = cursor.fetchall()
            self.connection.commit()
        if close_connection:
            self.disconnect()
        return result

    def get_last_insert_id(self):
        """
        Retrieves the primary key of the last inserted record

        Notes
        -----
        Should be used immediately after an upload record to retrieve the primary key  
        The connection must be kept open between the upload and the retrieve command  
        """
        return self.query(
            """
            SELECT LAST_INSERT_ID()
            """
        )[0]["LAST_INSERT_ID()"]

    def get_max_value(self, table_name: str, column_name: str):
        """
        Get the maximum value from an SQL table

        Parameters
        ----------
        table_name: str
            The name of the SQL table
        column_name: str
            The name of the column

        Returns
        -------
        int, float
            The maximum value
        """
        sql_stmt = "SELECT MAX(`{0}`) FROM `{1}`".format(column_name, table_name)
        result = self.query(sql_stmt)
        value = result[0][list(result[0].keys())[0]]
        if value is None:
            raise NoValueExists
        else:
            return value

    def get_value(self, table_name: str, column_name: str, where_columns: list, where_values: list) -> Union[int, float, str]:
        """
        Returns value that matches multiple where conditions

        Parameters
        ----------
        table_name: str
            The name of the SQL table
        column_name: str
            The column name of the value to return
        where_columns: list
            The name of the columns in the SQL table to use in the where condition
        where_values: list
            The values to use with the where_columns in the where condition

        Returns
        -------
        Union[int, float, str]
            The value associated with the column_name that matches the multiple where conditions

        Notes
        -----
        Raises exception if no value exists or if multiple values exist
        """
        sql_stmt_template = "SELECT `{0}` FROM `{1}` WHERE {2}"
        where_condition = " AND ".join(["`{}` = %s".format(column) for column in where_columns])
        sql_stmt = sql_stmt_template.format(column_name, table_name, where_condition)
        result = self.query(sql_stmt, where_values)
        if len(result) == 0:
            raise NoValueExists
        elif len(result) > 1:
            raise MultipleValuesExists
        else:
            return result[0][column_name]

    def upload_record(self, table_name: str, columns: list, values: list):
        """
        Uploads record/s to a MySQL table

        Parameters
        ----------
        table_name: str
            The name of the SQL table
        columns: list [col1, col2, col3, ...]
            The column names for each value to upload in the same order as values
        values: list [[val1, val2, val3, ...], list2, list3, ...]
            A list of lists of values for each record you want to enter in the same order as columns
        """
        sql_stmt_template = "INSERT INTO `{0}` ({1}) VALUES ({2})"
        num_items = len(columns)
        formatted_columns = ["`{}`".format(column) for column in columns]
        sql_stmt = sql_stmt_template.format(
            table_name,
            ','.join(formatted_columns),
            ','.join(["%s"]*num_items)
        )
        upload_values = []
        for record in values:
            upload_values.append([])
            for value in record:
                if value is None:
                    upload_values[-1].append(None)
                elif type(value) is str:
                    upload_values[-1].append(value)
                elif type(value) is bytes:
                    upload_values[-1].append(value)
                elif math.isnan(value):
                    upload_values[-1].append(None)
                else:
                    upload_values[-1].append(value)
        self.query(sql_stmt, upload_values, execute_many=True)

    def alter_value(self, table_name: str, where_columns: list, where_values: list, column_names: list, values: list):
        """
        Alter value/s in a database

        Parameters
        ----------
        table_name: str
            The name of the SQL table
        where_columns: list [col1, col2, ...]
            The columns to use to identify the records to alter
        where_values: list [[val1, val2, ...], list2, ...]
            A list of lists of values for the corresponding where_columns to identify the records to alter
        column_names: list [col1, col2, ...]
            The column names of values to update
        values: list [[value1, value2, value3, ...], list2, list3, ...]
            A list of lists of values to update in the same order as column_names
        """
        sql_stmt_template = "UPDATE `{0}` SET {1} WHERE {2}"
        formatted_column_names = ",".join(["`{}` = %s".format(column) for column in column_names])
        where_condition = " AND ".join(["`{}` = %s".format(column) for column in where_columns])
        sql_stmt = sql_stmt_template.format(
            table_name,
            formatted_column_names,
            where_condition
        )
        values_where_values = [v + w for v, w in zip(values, where_values)]
        self.query(sql_stmt, values_where_values, execute_many=True)

    def delete_record(self, table_name: str, where_columns: list, where_values: list):
        """
        Delete SQL records based on where condition

        Parameters
        ----------
        table_name: str
            The name of the SQL table
        where_columns: list
            The columns to use to identify the records to delete
        where_values: list
            The values for the corresponding where_columns to identify the records to delete
        """
        sql_stmt_template = "DELETE FROM `{0}` WHERE {1}"
        where_condition = " AND ".join(["`{}` = %s".format(column) for column in where_columns])
        sql_stmt = sql_stmt_template.format(table_name, where_condition)
        self.query(sql_stmt, where_values)

    def exists(self, table_name: str, where_columns: list, where_values: list) -> bool:
        """
        Check the SQL table to see if value exists within column of table

        Parameters
        ----------
        table_name: str
            The name of the SQL table
        where_columns: list
            The columns to use to identify the record
        where_values: list
            The values for the corresponding where_columns to identify the record

        Returns
        -------
        bool
            Whether the value exists or not
        """
        sql_subquery_stmt_template = "SELECT * FROM `{0}` WHERE {1}"
        where_condition = " AND ".join(["`{}` = %s".format(column) for column in where_columns])
        sql_subquery_stmt = sql_subquery_stmt_template.format(table_name, where_condition)
        sql_stmt = "SELECT EXISTS({})".format(sql_subquery_stmt)
        result = self.query(sql_stmt, where_values)
        value = result[0][list(result[0].keys())[0]]
        if value == 1:
            return True
        else:
            return False
