import psycopg2
from config import load_config

def update_balance(user_id, balance):
    sql = """UPDATE customer_details SET balance = %s WHERE user_id = %s"""

    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (balance, user_id))

        conn.commit()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)