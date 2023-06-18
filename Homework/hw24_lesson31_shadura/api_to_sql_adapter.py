import psycopg2
import requests
import json


class APItoSQLAdapter:
    def __init__(self, user, password, host, port, database, table_name, columns_create, columns_insert):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.create_database_if_not_exists()
        self.table_name = table_name
        self.column_definitions_create = ", ".join(columns_create)
        self.column_definitions_insert = ", ".join(columns_insert)
        self.column_definitions_update = columns_insert[1:]
        self.create_table_if_not_exists()
        self.object_url = None
        self.object_headers = None
        self.object = None
        self.object_id = None

    def create_database_if_not_exists(self):
        try:
            connection_1 = psycopg2.connect(host=self.host, port=self.port, user=self.user, password=self.password)
            with connection_1.cursor() as cursor:
                connection_1.autocommit = True
                cursor.execute(f"SELECT datname FROM pg_catalog.pg_database WHERE lower(datname) = lower('{self.database}')")
                result = cursor.fetchone()
                if not result:
                    cursor.execute(f"CREATE DATABASE {self.database}")
                    print(f"[INFO FROM SQL] Database '{self.database}' successfully created ")
                else:
                    print(f"[INFO FROM SQL] Database '{self.database}' is already exasts ")
        except psycopg2.OperationalError as err:
            print(f"[INFO FROM SQL] Error connecting to the database: {err}")
        finally:
            if connection_1:
                connection_1.close()
                print("[INFO FROM SQL] PostgreSQL 'create_database_connection' is closed.\n")

    def create_table_if_not_exists(self):
        try:
            connection_2 = psycopg2.connect(host=self.host, port=self.port, user=self.user, password=self.password, database=self.database)
            with connection_2.cursor() as cursor:
                cursor.execute(f"SELECT table_name FROM information_schema.tables WHERE table_name = '{self.table_name}'")
                result = cursor.fetchone()
                if not result:
                    cursor.execute(f"CREATE TABLE {self.table_name} ({self.column_definitions_create})")
                    connection_2.commit()
                    print(f"[INFO FROM SQL] Table '{self.table_name}' created.")
                else:
                    print(f"[INFO FROM SQL] Table '{self.table_name}' already exists.")
        finally:
            if connection_2:
                connection_2.close()
                print("[INFO FROM SQL] PostgreSQL 'create_table_connection' is closed.\n")

    def create_object_in_api(self, object_url, object_headers, object_json):
        # Логика создания объекта в API (POST)
        created_object = requests.post(object_url, data=object_json, headers=object_headers)
        self.object_url = object_url
        self.object_headers = object_headers
        self.object_id = created_object.json().get('id')
        print(f"[INFO FROM API] Object {self.object_id} was successfully created on url: '{object_url}'")
        return self.object_id

    def get_object_from_api(self):
        # Логика получения объекта из API (GET)
        self.object = requests.get(self.object_url + '/' + self.object_id, self.object_headers)
        print(f"[INFO FROM API] Object '{self.object_id}' was successfully received from url: '{self.object_url}'")
        return self.object.json()

    def insert_object_in_database(self):
        try:
            connection_3 = psycopg2.connect(host=self.host, port=self.port, user=self.user, password=self.password, database=self.database)
            with connection_3.cursor() as cursor:
                val_1, val_2, val_3 = self.object.json().get('id'), self.object.json().get('name'), json.dumps(self.object.json().get('data'))
                cursor.execute(f"INSERT INTO {self.table_name} ({self.column_definitions_insert}) VALUES ('{val_1}', '{val_2}', '{val_3}')")
                connection_3.commit()
                print(f"[INFO FROM SQL] Object '{self.object_id}' was successfully inserted into table '{self.table_name}'.")
        finally:
            if connection_3:
                connection_3.close()
                print("[INFO FROM SQL] PostgreSQL 'insert_object_connection' is closed.\n")

    def select_object_from_sql(self):
        try:
            connection_4 = psycopg2.connect(host=self.host, port=self.port, user=self.user, password=self.password, database=self.database)
            with connection_4.cursor() as cursor:
                cursor.execute(f"SELECT * FROM {self.table_name} WHERE id_from_api LIKE '{self.object_id}'")
                result = cursor.fetchone()
                print(f"Selected object from '{self.table_name}': ", result)
                print(f"[INFO FROM SQL] Object '{self.object_id}' was successfully selected from table '{self.table_name}'.")
        finally:
            if connection_4:
                connection_4.close()
                print("[INFO FROM SQL] PostgreSQL 'select_object_connection' is closed.\n")

    def update_object_in_api(self, data):
        put_request = requests.put(self.object_url + '/' + self.object_id, data=data, headers=self.object_headers)
        print(f"[INFO FROM API] Object '{self.object_id}' was successfully updated.")

    def update_object_in_sql(self):
        updated_object_from_api = self.get_object_from_api()
        try:
            connection_5 = psycopg2.connect(host=self.host, port=self.port, user=self.user, password=self.password, database=self.database)
            with connection_5.cursor() as cursor:
                val_1, val_2 = updated_object_from_api.get('name'), json.dumps(updated_object_from_api.get('data'))
                cursor.execute(f"UPDATE {self.table_name} SET {self.column_definitions_update[0]} = '{val_1}', {self.column_definitions_update[1]} = '{val_2}' WHERE {self.table_name}.id_from_api = '{self.object_id}'")
                connection_5.commit()
                cursor.execute(f"SELECT * FROM {self.table_name} WHERE id_from_api LIKE '{self.object_id}'")
                result = cursor.fetchone()
                print(f"Selected updated object (checking) from '{self.table_name}': ", result)
                print(f"[INFO FROM SQL] Object '{self.object_id}' was successfully updated.")
        finally:
            if connection_5:
                connection_5.close()
                print("[INFO FROM SQL] PostgreSQL 'update_object_connection' is closed.\n")


    def delete_object_from_api(self):
        del_request = requests.delete(self.object_url + '/' + self.object_id)
        check_deletef_object = requests.get(self.object_url + '/' + self.object_id, self.object_headers)
        print(check_deletef_object.json())
        print(f"[INFO FROM API] Object '{self.object_id}' was successfully deleted from {self.object_url}.\n")

    def delete_object_from_sql(self):
        try:
            connection_6 = psycopg2.connect(host=self.host, port=self.port, user=self.user, password=self.password, database=self.database)
            with connection_6.cursor() as cursor:
                cursor.execute(f"DELETE FROM {self.table_name} WHERE {self.table_name}.id_from_api = '{self.object_id}'")
                connection_6.commit()
                self.select_object_from_sql()
                print(f"[INFO FROM SQL] Object '{self.object_id}' was successfully deleted.")
        finally:
            if connection_6:
                connection_6.close()
                print("[INFO FROM SQL] PostgreSQL 'delete_object_connection' is closed.\n")