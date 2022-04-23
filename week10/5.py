import psycopg2
from config import config

def insert_user_list(user_list):
    sql = """
    insert into accounts(username, email) values (%s, %s);
    """

    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.executemany(sql, user_list)
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()

insert_user_list([
    ('user1', 'email1@gmail.com'),
    ('user2', 'email2@gmail.com'),
    ('user3', 'email3@gmail.com'),
    ('user4', 'email4@gmail.com'),
])