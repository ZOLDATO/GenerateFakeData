import sqlite3
from generate_new_fake_data import path_my_bd, connect_db, generate_some_fake_data_and_get_new_ids


def view_data(ids, cur):
    cur.execute('SELECT * FROM Customer WHERE CustomerId BETWEEN ? AND ?', (ids[0], ids[len(ids) - 1]))
    return cur.fetchall()


try:
    conn, cur = connect_db(path_my_bd)
    ids = generate_some_fake_data_and_get_new_ids(3, cur)  # 3 записи и id новых строк записаны в список
    conn.commit()
    print("Операция завершена успешно!!")

except sqlite3.Error as e:
    print(f"Ошибка SQLite: {e}")
except Exception as e:
    print(f"Произошла ошибка: {e}")

for x in view_data(ids, cur):
    print(x)

conn.close()
