"""
create or replace procedure add_role(
    role_name varchar,
    user_id integer
)
as $$
declare
    return_role_id INT;
begin
    insert into roles(role_name)
    values(role_name)
    returning role_id into return_role_id;

    insert into account_roles(user_id, role_id)
    values(user_id, return_role_id);
end;
$$
language plpgsql;
"""
import psycopg2
from config import config


def add_role(role_name, user_id):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute('call add_role(%s, %s)', (role_name, user_id))
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()

add_role("new role", 2)
add_role("new role 2", 4)