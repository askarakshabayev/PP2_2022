import psycopg2
from config import config


def add_data(role_name, user_list):
    insert_role = "INSERT INTO roles(role_name) VALUES(%s) RETURNING role_id;"
    account_roles = "insert into account_roles(user_id,role_id) values(%s, %s);"
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(insert_role, (role_name,))
        role_id = cur.fetchone()[0]
        for user_id in user_list:
            cur.execute(account_roles, (user_id, role_id))
        conn.commit()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()

# add_data('role1', [1, 7])
# add_data('manager', [8, 9])
add_data('moderator', [5, 10])