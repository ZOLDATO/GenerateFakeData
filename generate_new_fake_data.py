import sqlite3
from faker import Faker

path_my_bd = r'C:\Users\user\AppData\Roaming\DBeaverData\workspace6\.metadata\sample-database-sqlite-1\Chinook.db'


def connect_db(path_bd):
    # Создаем подключение к нашей базе данных
    connection = sqlite3.connect(path_bd)
    cursor = connection.cursor()
    return connection, cursor


def generate_some_fake_data(num, cursor):
    faker = Faker('en_US')

    for _ in range(num):
        some_fake_customer = (
            faker.first_name(),
            faker.last_name(),
            faker.company(),
            faker.address(),
            faker.city(),
            faker.state(),
            faker.country(),
            faker.postalcode(),
            faker.phone_number(),
            faker.phone_number(),
            faker.email(),
            faker.random_number(digits=1)
        )

        cursor.execute(
            'INSERT INTO Customer (FirstName, LastName, Company, Address, City, State, Country, PostalCode, Phone, Fax, Email, SupportRepId) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
            some_fake_customer)


def commit_and_close(connection):
    # Сохраняем изменения и закрываем соединение
    connection.commit()
    connection.close()


try:
    conn, cur = connect_db(path_my_bd)
    generate_some_fake_data(10, cur)  # 10 записей
    commit_and_close(conn)
    print("Операция завершена успешно!")

except sqlite3.Error as e:
    print(f"Ошибка SQLite: {e}")
except Exception as e:
    print(f"Произошла ошибка: {e}")
