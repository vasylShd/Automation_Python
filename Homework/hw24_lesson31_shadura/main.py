from api_to_sql_adapter import APItoSQLAdapter
from db_config import user, password, host, port, database
from requests_config import object_url, list_json, object_headers


table_name = 'devices'
columns_create = [
    "Id SERIAL PRIMARY KEY",
    "id_from_api varchar(150) NOT NULL",
    "name varchar(150) NOT NULL",
    "data varchar(150) NOT NULL"
]

columns_insert = ["id_from_api", "name", "data"]

adapter = APItoSQLAdapter(user, password, host, port, database, table_name, columns_create, columns_insert)

object_created_in_api_id = adapter.create_object_in_api(object_url, object_headers, list_json[0])
print(f"Object created in API with ID: {object_created_in_api_id}\n")

get_object_from_api = adapter.get_object_from_api()
print(f"Object retrieved from API: {get_object_from_api}\n")

adapter.insert_object_in_database()

adapter.select_object_from_sql()

adapter.update_object_in_api(list_json[1])
object_from_api = adapter.get_object_from_api()
print(f"Object retrieved from API: {object_from_api}\n")

adapter.update_object_in_sql()

adapter.delete_object_from_api()

adapter.delete_object_from_sql()
