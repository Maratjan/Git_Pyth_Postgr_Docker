import psycopg2
conn = psycopg2.connect(
    host = "localhost",
    database = "my_finances",
    user = "postgres"
    password = "DB"
)
#Создаём таблицу, если её нет
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses(
        ID SERIAL PRIMARY KEY,
        amount DECIMAL,
        category varchar(100),
        description TEXT,
        created_at TIMESTAMP DEFAULT NOW()
    )
""")
conn.commit()
# Добавляем тестовую запись 
cursor.execute("INSERT INTO expenses (amount, category) VALUES (1000, 'food')")
conn.commit
cursor.execute("SELECT * FROM expenses")
records = cursor.fetchall()
print("Записи в БД:", records)
#закрываем соединение 
cursor.close()
conn.close