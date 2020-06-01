import functions
import os
from time import sleep
#import RPi.GPIO as GPIO

#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(7, GPIO.OUT)

zombieCudaPin = "7"
deviceTwoPin = "7"
deviceThreePin = "7"
deviceFourPin = "7"
choice = ""

def wait(seconds):
    print("Please wait (" + str(seconds) + ") ", end="")
    for num in range(0, seconds):
        if num != seconds - 1:
            print(str(num + 1) + ", ", end="")
        else:
            print(str(num + 1), end="")
        sleep(1)

while True:
    functions.showMenu()
    choice = str(input("Enter choice: "))
    if choice == "1":
        print("ZombieCuda turned on (pin " + zombieCudaPin + ")")
        #GPIO.output(int(zombieCudaPin), True)
        wait(3)
        #GPIO.output(int(zombieCudaPin), False)
    if choice == "2":
        print("ZombieCuda turned off (pin " + zombieCudaPin + ")")
        #GPIO.output(int(zombieCudaPin), True)
        wait(5)
        #GPIO.output(int(zombieCudaPin), False)
    if choice == "3":
        print("DeviceTwo turned on (pin " + deviceTwoPin + ")")
        #GPIO.output(int(deviceTwoPin), True)
        wait(3)
        #GPIO.output(int(deviceTwoPin), False)
    if choice == "4":
        print("DeviceTwo turned off (pin " + deviceTwoPin + ")")
        #GPIO.output(int(deviceTwoPin), True)
        wait(5)
        #GPIO.output(int(deviceTwoPin), False)
    if choice == "5":
        print("DeviceThree turned on (pin " + deviceThreePin + ")")
        #GPIO.output(int(deviceThreePin), True)
        wait(3)
        #GPIO.output(int(deviceThreePin), False)
    if choice == "6":
        print("DeviceThree turned off (pin " + deviceThreePin + ")")
        #GPIO.output(int(deviceThreePin), True)
        wait(5)
        #GPIO.output(int(deviceThreePin), False)
    if choice == "7":
        continue
    if choice == "8":
        continue
    if choice == "9":
        toTest = input("Enter pin number to be tested: ")
        toTestSeconds = int(input("Enter seconds for pin " + toTest + " to be tested: "))

        print("Testing pin " + toTest + " for " + str(toTestSeconds) + " seconds.")

        #GPIO.setup(int(toTest), GPIO.OUT)
        #GPIO.output(int(toTest), True)
        wait(toTestSeconds)
        #GPIO.output(int(toTest), False)
    if choice.lower() == "x":
        print("Program closed")
        break

    print()
    try:
        print()
        if os.name == "nt":
            os.system("cls")
        else:
            continue#os.system("clear")
    except:
        print("woo")

#GPIO.cleanup()