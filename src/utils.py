import os
import sqlite3
import mysql.connector
import psycopg2


class IsExistsDB:
    @staticmethod
    def db_exists(path):
        return os.path.exists(path)


class CreateSqliteConnection:
    @staticmethod
    def create_conn(db_path):
        if IsExistsDB.db_exists(db_path):
            return sqlite3.connect(db_path)
        return CreateDB.create_sqlite_db(db_path)


class CreatePostgreSqlConnection:
    @staticmethod
    def create_conn(**conn_params):
        if IsExistsDB.db_exists(conn_params['dbname']):
            with psycopg2.connect(conn_params['dbname']) as conn:
                return conn
        return CreateDB.create_postgres_db( **conn_params)


class CreateMySqlConnection:
    @staticmethod
    def create_conn(**conn_params):
        return CreateDB.create_mysql_db(**conn_params)


class CreateDB:
    @staticmethod
    def create_sqlite_db(db_path):
        with open('db/database_setup.sql', 'r') as file:
            scripts = file.read()
        try:
            with sqlite3.connect(db_path) as conn:
                cursor = conn.cursor()
                cursor.executescript(scripts)
                return conn
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            return

    @staticmethod
    def create_postgres_db(**conn_params):
        with open('db/database_setup.sql', 'r') as file:
            scripts = file.read()

        with psycopg2.connect(**conn_params) as conn:
            conn.autocommit = True
            cursor = conn.cursor()
            sql = "CREATE DATABASE postgres"
            cursor.execute(sql)
            cursor.execute(scripts)
            cursor.close()
            return conn

    @staticmethod
    def create_mysql_db(**conn_params):
        with open('db/database_setup.sql', 'r') as file:
            scripts = file.read()

        with mysql.connector.connect(**conn_params) as conn:
            conn.autocommit = True
            cursor = conn.cursor()
            cursor.execute(scripts)
            cursor.close()
            return conn

