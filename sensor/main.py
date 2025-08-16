import asyncio
import time
from threading import Thread

from database import init_db, log_data
from sensor import read_sensor_data
from bot import start_bot

# Инициализация БД
init_db()

# Фоновая задача для периодического чтения и логирования данных (каждые 5 минут)
async def background_sensor_task():
    while True:
        data = read_sensor_data()
        if data:
            log_data(data)
        await asyncio.sleep(300)  # 5 минут

# Запуск фоновой задачи в отдельном потоке (поскольку aiogram на asyncio)
def run_background_task():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(background_sensor_task())

if __name__ == '__main__':
    # Запуск фоновой задачи в потоке
    sensor_thread = Thread(target=run_background_task)
    sensor_thread.daemon = True
    sensor_thread.start()
    
    # Запуск бота
    start_bot()