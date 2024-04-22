import psycopg2
from config import load_config

def check_user(user_id, user_pin):
    sql = "SELECT * FROM customer_details WHERE user_id = %s AND user_pin = %s"
    
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
               cur.execute(sql, [user_id, user_pin])
               _user_tuple = cur.fetchone()
               return _user_tuple[0], _user_tuple[1], _user_tuple[3]
           
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)

def new_user_check(user_id):
    sql = "SELECT * FROM customer_details WHERE user_id = %s"

    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, [user_id])
                user_tuple = cur.fetchone()
                return user_tuple
            
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)