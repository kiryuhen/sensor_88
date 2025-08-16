import sqlite3
from datetime import datetime, timedelta

# Инициализация базы данных
DB_NAME = 'sensor_data.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS readings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            temperature REAL,
            humidity REAL,
            pressure REAL
        )
    ''')
    conn.commit()
    conn.close()

# Логирование данных
def log_data(data):
    if data:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO readings (temperature, humidity, pressure)
            VALUES (?, ?, ?)
        ''', (data['temperature'], data['humidity'], data['pressure']))
        conn.commit()
        conn.close()

# Получение статистики за период
def get_statistics(period):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    if period == 'week':
        start_date = datetime.now() - timedelta(days=7)
    elif period == 'month':
        start_date = datetime.now() - timedelta(days=30)
    else:
        return None
    
    cursor.execute('''
        SELECT AVG(temperature), AVG(humidity), AVG(pressure)
        FROM readings
        WHERE timestamp >= ?
    ''', (start_date,))
    
    result = cursor.fetchone()
    conn.close()
    
    if result:
        return {
            'avg_temperature': round(result[0], 2) if result[0] else 0,
            'avg_humidity': round(result[1], 2) if result[1] else 0,
            'avg_pressure': round(result[2], 2) if result[2] else 0
        }
    return None