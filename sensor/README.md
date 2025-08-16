# RPi Sensor Bot

Система мониторинга данных с BME280 на Raspberry Pi Zero 2W с интеграцией в Telegram-бот и управлением RGB LED.

## Требования
- Raspberry Pi Zero 2W с Raspbian OS.
- BME280 подключен по I2C.
- RGB LED подключен к GPIO 17 (красный), 27 (зеленый), 22 (синий).
- Telegram бот (создайте через @BotFather и установите токен как переменную окружения BOT_TOKEN).

## Последовательность действий для загрузки проекта через GitHub и изменения данных для WiFi

1. **Клонируйте репозиторий с GitHub**:
   - Подключитесь к RPi по SSH или напрямую.
   - Установите Git, если не установлен: `sudo apt update && sudo apt install git`.
   - Клонируйте: `git clone https://github.com/yourusername/rpi_sensor_bot.git` (замените на ваш репозиторий).
   - Перейдите в директорию: `cd rpi_sensor_bot`.

2. **Изменение данных для WiFi** (если нужно подключиться к новой сети):
   - Отредактируйте файл `/etc/wpa_supplicant/wpa_supplicant.conf`: