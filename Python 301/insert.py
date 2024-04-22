import psycopg2
from config import load_config

def new_customer(user_id, user_name, user_pin, balance):
    sql = """INSERT INTO customer_details(user_id, user_name, user_pin, balance)
             VALUES(%s, %s, %s, %s);"""
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (user_id, user_name, user_pin, balance))

                conn.commit()

    except(Exception, psycopg2.DatabaseError) as error:
        print(error)