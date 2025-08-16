import board
import adafruit_bme280.basic as adafruit_bme280
import RPi.GPIO as GPIO
import time

# Настройка пинов для RGB LED (общий катод)
RED_PIN = 17
GREEN_PIN = 27
BLUE_PIN = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)

# Функция для установки цвета LED
def set_led_color(color):
    GPIO.output(RED_PIN, GPIO.LOW)
    GPIO.output(GREEN_PIN, GPIO.LOW)
    GPIO.output(BLUE_PIN, GPIO.LOW)
    if color == 'red':
        GPIO.output(RED_PIN, GPIO.HIGH)
    elif color == 'green':
        GPIO.output(GREEN_PIN, GPIO.HIGH)
    elif color == 'blue':
        GPIO.output(BLUE_PIN, GPIO.HIGH)

# Инициализация датчика BME280
i2c = board.I2C()
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

# Функция для чтения данных с датчика и обновления LED
def read_sensor_data():
    try:
        temperature = bme280.temperature
        humidity = bme280.relative_humidity
        pressure = bme280.pressure

        # Логика для LED на основе температуры
        if temperature > 29:
            set_led_color('red')
        elif temperature < 18:
            set_led_color('blue')
        else:
            set_led_color('green')

        return {
            'temperature': round(temperature, 2),
            'humidity': round(humidity, 2),
            'pressure': round(pressure, 2)
        }
    except Exception as e:
        print(f"Error reading sensor: {e}")
        return None