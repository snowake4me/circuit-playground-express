import board
import digitalio
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

while True:
    print("Hello, CircuitPython!")
    led.value = True
    print("LED ON")
    time.sleep(0.5)
    led.value = False
    print("LED OFF")
    time.sleep(2.5)
