from machine import Pin, ADC, PWM
from time import sleep

led = Pin(2, Pin.OUT)
button = Pin(15, Pin.IN)

#Configure ADC for ESP32
pot = ADC(Pin(34))
pot.width(ADC.WIDTH_10BIT)
pot.atten(ADC.ATTN_11DB)

#Configure ADC for ESP8266
#pot = ADC(0)

led_pwm = PWM(Pin(4),5000)

while True:
  button_state = button.value()
  led.value(button_state)

  pot_value = pot.read()
  led_pwm.duty(pot_value)

  sleep(0.1)


import dht 

sensor = dht.DHT22(Pin(14))
#sensor = dht.DHT11(Pin(14))

while True:
  try:
    sleep(2)
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    temp_f = temp * (9/5) + 32.0
    print('Temperature: %3.1f C' %temp)
    print('Temperature: %3.1f F' %temp_f)
    print('Humidity: %3.1f %%' %hum)
  except OSError as e:
    print('Failed to read sensor.')