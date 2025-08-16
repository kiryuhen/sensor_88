from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
import asyncio
import os  # Добавлен импорт для работы с переменными окружения

from sensor import read_sensor_data
from database import get_statistics

# Токен берется из переменной окружения BOT_TOKEN
BOT_TOKEN = os.getenv('BOT_TOKEN')
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN не установлен в переменных окружения!")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Inline клавиатура
inline_kb = InlineKeyboardMarkup(row_width=1)
inline_kb.add(InlineKeyboardButton("Текущие данные", callback_data='current'))
inline_kb.add(InlineKeyboardButton("Статистика за неделю", callback_data='week'))
inline_kb.add(InlineKeyboardButton("Статистика за месяц", callback_data='month'))

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Привет! Выберите действие:", reply_markup=inline_kb)

@dp.callback_query_handler()
async def callback_query_handler(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    
    if callback_query.data == 'current':
        data = read_sensor_data()
        if data:
            response = f"Текущие данные:\nТемпература: {data['temperature']}°C\nВлажность: {data['humidity']}%\nДавление: {data['pressure']} hPa"
        else:
            response = "Ошибка чтения данных."
        await bot.send_message(callback_query.from_user.id, response)
    
    elif callback_query.data == 'week':
        stats = get_statistics('week')
        if stats:
            response = f"Статистика за неделю:\nСредняя температура: {stats['avg_temperature']}°C\nСредняя влажность: {stats['avg_humidity']}%\nСреднее давление: {stats['avg_pressure']} hPa"
        else:
            response = "Нет данных за неделю."
        await bot.send_message(callback_query.from_user.id, response)
    
    elif callback_query.data == 'month':
        stats = get_statistics('month')
        if stats:
            response = f"Статистика за месяц:\nСредняя температура: {stats['avg_temperature']}°C\nСредняя влажность: {stats['avg_humidity']}%\nСреднее давление: {stats['avg_pressure']} hPa"
        else:
            response = "Нет данных за месяц."
        await bot.send_message(callback_query.from_user.id, response)

# Функция для запуска бота
def start_bot():
    executor.start_polling(dp, skip_updates=True)