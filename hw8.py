import sqlite3

# Устанавливаем подключение к базе данных
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# Создаем таблицы (если они еще не существуют)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS countries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL
    );
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS cities (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        area REAL DEFAULT 0,
        country_id INTEGER,
        FOREIGN KEY (country_id) REFERENCES countries(id)
    );
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        city_id INTEGER,
        FOREIGN KEY (city_id) REFERENCES cities(id)
    );
""")

# Добавляем страны
cursor.execute("INSERT OR IGNORE INTO countries (title) VALUES ('Кыргызстан')")
cursor.execute("INSERT OR IGNORE INTO countries (title) VALUES ('Германия')")
cursor.execute("INSERT OR IGNORE INTO countries (title) VALUES ('Китай')")

# Добавляем города
cursor.execute("INSERT OR IGNORE INTO cities (title, area, country_id) VALUES ('Бишкек', 250.0, 1)")
cursor.execute("INSERT OR IGNORE INTO cities (title, area, country_id) VALUES ('Ош', 200.0, 1)")
cursor.execute("INSERT OR IGNORE INTO cities (title, area, country_id) VALUES ('Берлин', 891.8, 2)")
cursor.execute("INSERT OR IGNORE INTO cities (title, area, country_id) VALUES ('Мюнхен', 310.7, 2)")
cursor.execute("INSERT OR IGNORE INTO cities (title, area, country_id) VALUES ('Пекин', 16410.0, 3)")
cursor.execute("INSERT OR IGNORE INTO cities (title, area, country_id) VALUES ('Шанхай', 6340.5, 3)")
cursor.execute("INSERT OR IGNORE INTO cities (title, area, country_id) VALUES ('Гуанчжоу', 7434.4, 3)")

# Добавляем учеников
cursor.execute("INSERT OR IGNORE INTO students (first_name, last_name, city_id) VALUES ('Али', 'Искендеров', 1)")
cursor.execute("INSERT OR IGNORE INTO students (first_name, last_name, city_id) VALUES ('Айгерим', 'Султанова', 1)")
cursor.execute("INSERT OR IGNORE INTO students (first_name, last_name, city_id) VALUES ('Нурлан', 'Кайырбеков', 2)")
cursor.execute("INSERT OR IGNORE INTO students (first_name, last_name, city_id) VALUES ('Эмиль', 'Токтогазиев', 2)")
cursor.execute("INSERT OR IGNORE INTO students (first_name, last_name, city_id) VALUES ('Герман', 'Шмидт', 3)")
cursor.execute("INSERT OR IGNORE INTO students (first_name, last_name, city_id) VALUES ('Ева', 'Мюллер', 3)")
cursor.execute("INSERT OR IGNORE INTO students (first_name, last_name, city_id) VALUES ('Юлия', 'Шмидт', 4)")
cursor.execute("INSERT OR IGNORE INTO students (first_name, last_name, city_id) VALUES ('Джон', 'Вильямс', 4)")
cursor.execute("INSERT OR IGNORE INTO students (first_name, last_name, city_id) VALUES ('Чжан', 'Ли', 5)")
cursor.execute("INSERT OR IGNORE INTO students (first_name, last_name, city_id) VALUES ('Ли', 'Мэн', 5)")
cursor.execute("INSERT OR IGNORE INTO students (first_name, last_name, city_id) VALUES ('Юн', 'Ван', 6)")
cursor.execute("INSERT OR IGNORE INTO students (first_name, last_name, city_id) VALUES ('Мин', 'Ли', 6)")
cursor.execute("INSERT OR IGNORE INTO students (first_name, last_name, city_id) VALUES ('Ли', 'Цзяо', 7)")
cursor.execute("INSERT OR IGNORE INTO students (first_name, last_name, city_id) VALUES ('Панг', 'Ци', 7)")
cursor.execute("INSERT OR IGNORE INTO students (first_name, last_name, city_id) VALUES ('Тан', 'Ши', 1)")

# Сохраняем изменения
conn.commit()

# Закрываем соединение
conn.close()

import sqlite3

def main():
    # Устанавливаем подключение к базе данных
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()

    # Выводим сообщение для пользователя
    print("Вы можете отобразить список учеников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:")

    # Запросим все города
    cursor.execute("SELECT id, title FROM cities")
    cities = cursor.fetchall()

    # Если города не найдены, выводим сообщение и выходим
    if not cities:
        print("В базе данных нет городов.")
        conn.close()
        return

    # Выводим список городов
    for city in cities:
        print(f"{city[0]}. {city[1]}")

    # Получаем выбор пользователя
    city_id = int(input("Введите id города: "))

    # Если пользователь вводит 0, выходим
    if city_id == 0:
        print("Выход из программы.")
    else:
        # Находим всех учеников в выбранном городе
        cursor.execute("""
            SELECT s.first_name, s.last_name, co.title AS country, c.title AS city, c.area
            FROM students s
            JOIN cities c ON s.city_id = c.id
            JOIN countries co ON c.country_id = co.id
            WHERE c.id = ?
        """, (city_id,))
        students = cursor.fetchall()

        # Выводим список учеников
        if students:
            print(f"\nУченики из города {city_id}:")
            for student in students:
                print(f"Имя: {student[0]}, Фамилия: {student[1]}, Страна: {student[2]}, Город: {student[3]}, Площадь города: {student[4]}")
        else:
            print("В выбранном городе нет учеников.")

    # Закрываем соединение с базой данных
    conn.close()

if __name__ == "__main__":
    main()


