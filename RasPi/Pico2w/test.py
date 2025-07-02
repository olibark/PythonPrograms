from machine import Pin
import time

pir = Pin(16, Pin.IN)

print("Warming up...")
time.sleep(60)

while True:
    print(pir.value())
    time.sleep(0.5)
