import os

import psycopg2 #łaczy z bazą
import dotenv

config = {}

def init(): #init database
    dotenv.load_dotenv()
    config["db_ip"]=os.environ.get("db_ip")
    config["db_name"]=os.environ.get("db_name")
    config["db_user"]=os.environ.get("db_user")
    config["db_password"]=os.environ.get("db_password")


def get_product(ean):
    pg_handler=psycopg2.connect(host=config["db_ip"],database=config["db_name"], user=config["db_user"], password=config["db_password"])
    pg_cursor=pg_handler.cursor()
    pg_cursor.execute(f"SELECT * FROM products WHERE EAN = '{ean}';")
    result= pg_cursor.fetchall() #daje wszystkie wyniki
    pg_handler.close()
    return result

def insert_product(ean,name,bin): #dodawanie do bazy
    pg_handler = psycopg2.connect(host=config["db_ip"], database=config["db_name"], user=config["db_user"],
                                  password=config["db_password"])
    pg_cursor = pg_handler.cursor()
    pg_cursor.execute(f"SELECT * FROM products WHERE EAN = '{ean}';")
    result = pg_cursor.fetchall()
    if len(result)!=0:
        print(f"{ean} already exists")
        return

    pg_cursor.execute(f"insert into products(ean, name, bin) values('{ean}', '{name}', '{bin}');")
    pg_handler.commit()
    pg_handler.close()