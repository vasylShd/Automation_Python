from api_to_sql_adapter import APItoSQLAdapter
from db_config import user, password, host, port, database, table_name, columns_create, columns_insert
from requests_config import object_url, list_json, object_headers


api_sql_adapter = APItoSQLAdapter(user, password, host, port, database, table_name, columns_create, columns_insert)

object_created_in_api_id = api_sql_adapter.create_object_in_api(object_url, object_headers, list_json[0])
print(f"Object created in API with ID: {object_created_in_api_id}\n")

get_object_from_api = api_sql_adapter.get_object_from_api()
print(f"Object retrieved from API: {get_object_from_api}\n")

api_sql_adapter.insert_object_in_database()

api_sql_adapter.select_object_from_sql()

api_sql_adapter.update_object_in_api(list_json[1])
object_from_api = api_sql_adapter.get_object_from_api()
print(f"Object retrieved from API: {object_from_api}\n")

api_sql_adapter.update_object_in_sql()

api_sql_adapter.delete_object_from_api()

api_sql_adapter.delete_object_from_sql()
