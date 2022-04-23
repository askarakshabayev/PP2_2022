import psycopg2
from config import config


def insert_account(username, email):
    sql = """
    INSERT INTO accounts(username, email)
    VALUES(%s, %s) RETURNING user_id;
    """

    conn = None
    user_id = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (username, email))
        user_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()

    return user_id

# insert_account('Almas', 'almas@gmail.com')
# insert_account("Dina", 'dina@gmail.com')
insert_account('askar', 'askar.akshabayev@gmail.com')