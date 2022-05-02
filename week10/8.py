"""
create or replace function get_account_by_id2(id integer)
returns TABLE(user_id integer, username varchar) as
$$
begin
    return query
    select accounts.user_id, accounts.username from accounts where accounts.user_id=id;
end;
$$

language plpgsql;
"""
import psycopg2
from config import config

def get_account(id):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.callproc('get_account_by_id2', (id, ))
        row = cur.fetchone()
        while row is not None:
            print(row)
            row = cur.fetchone()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()

get_account(2)