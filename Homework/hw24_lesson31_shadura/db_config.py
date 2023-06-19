user ='postgres'
password ='postgres'
host ='127.0.0.1'
port ='5432'
database='postgres_api'

table_name = 'devices_1'
columns_create = [
    "Id SERIAL PRIMARY KEY",
    "id_from_api varchar(150) NOT NULL",
    "name varchar(150) NOT NULL",
    "data varchar(150) NOT NULL"
]
columns_insert = ["id_from_api", "name", "data"]
