
headers = ['id', 'Фамилия', 'Имя', 'Телефон', 'email', 'DataCreated']

name_db = 'book_sqlite.db'

table_users = '''CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                            lastname TEXT NOT NULL,
                            name TEXT NOT NULL,
                            phone TEXT NOT NULL,
                            email TEXT NOT NULL default 'not email',
                            created_at datetime default current_timestamp);'''

insert_user = """INSERT INTO users
                          (lastname, name, phone, email)
                          VALUES (?, ?, ?, ?);"""

view_all = '''SELECT * FROM users'''

sql_delete_query = """DELETE FROM users WHERE id = ?"""