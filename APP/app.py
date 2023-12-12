from machine import Pin,UART
from machine import Pin
led = Pin(25, Pin.OUT)
led1 = Pin(21, Pin.OUT)
led2 = Pin(20, Pin.OUT)
led3 = Pin(19, Pin.OUT)
led4 = Pin(18, Pin.OUT)

led.value(1)
led1.value(1)
led2.value(1)
led3.value(1)
led4.value(1)


led.toggle()
uart = UART(0,9600)
while True:
    # print('checking BT')
    if uart.any():
        command = uart.readline()
        print(command[0])
        if(command[0]==50):
            print("led1 on")
            led.value(1)
        elif(command[0]==49):
            print("led1 off")
            led.value(0)
        elif(command[0]==51):
            print("led2 on")
            led1.value(1)
        elif(command[0]==52):
            print("led2 off")
            led1.value(0)
        elif(command[0]==53):
            print("led3 on")
            led2.value(1)
        elif(command[0]==54):
            print("led3 off")
            led2.value(0)
        elif(command[0]==55):
            print("led4 on")
            led3.value(1)
        elif(command[0]==56):
            print("led4 off")
            led3.value(0)
        elif(command[0]==57):
            print("led4 on")
            led4.value(1)
        elif(command[0]==48):
            print("led4 off")
            led4.value(0)
