from time import sleep
from tkinter import *
import RPi.GPIO as GPIO

def wait(seconds):
    #pop open alert with message stating name of device, turning on/off, and pulse length
    print("Please wait (" + str(seconds) + ") ", end="")
    for num in range(0, seconds):
        if num != seconds - 1:
            print(str(num + 1) + ", ", end="")
        else:
            print(str(num + 1), end="")
        sleep(1)
    print()

deviceOnePin = "7"
deviceTwoPin = "7"
deviceThreePin = "7"
deviceFourPin = "7"

#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(int(deviceOnePin), GPIO.OUT)
#GPIO.setup(int(deviceTwoPin), GPIO.OUT)
#GPIO.setup(int(deviceThreePin), GPIO.OUT)
#GPIO.setup(int(deviceFourPin), GPIO.OUT)

def turnOnDeviceOne(event):
    print("ZombieCuda turned on (pin " + deviceOnePin + ")")
    GPIO.output(int(deviceOnePin), False)
    wait(3)
    GPIO.output(int(deviceOnePin), True)

def turnOffDeviceOne(event):
    print("ZombieCuda turned off (pin " + deviceOnePin + ")")
    #GPIO.output(int(deviceOnePin), False)
    wait(5)
    #GPIO.output(int(deviceOnePin), True)

def turnOnDeviceTwo(event):
    print("DeviceTwo turned on (pin " + deviceTwoPin + ")")
    #GPIO.output(int(deviceTwoPin), False)
    wait(3)
    #GPIO.output(int(deviceTwoPin), True)

def turnOffDeviceTwo(event):
    print("DeviceTwo turned off (pin " + deviceTwoPin + ")")
    #GPIO.output(int(deviceTwoPin), False)
    wait(5)
    #GPIO.output(int(deviceTwoPin), True)

def turnOnDeviceThree(event):
    print("DeviceThree turned on (pin " + deviceThreePin + ")")
    #GPIO.output(int(deviceThreePin), False)
    wait(3)
    #GPIO.output(int(deviceThreePin), True)

def turnOffDeviceThree(event):
    print("DeviceThree turned off (pin " + deviceThreePin + ")")
    #GPIO.output(int(deviceThreePin), False)
    wait(5)
    #GPIO.output(int(deviceThreePin), True)

def turnOnDeviceFour(event):
    print("DeviceThree turned on (pin " + deviceFourPin + ")")
    # GPIO.output(int(deviceThreePin), False)
    wait(3)
    # GPIO.output(int(deviceThreePin), True)

def turnOffDeviceFour(event):
    print("DeviceThree turned off (pin " + deviceFourPin + ")")
    #GPIO.output(int(deviceThreePin), False)
    wait(5)
    #GPIO.output(int(deviceThreePin), True)

def testPin(event):
    toTest = input("Enter pin number to be tested: ")
    toTestSeconds = int(input("Enter seconds for pin " + toTest + " to be tested: "))

    print("Testing pin " + toTest + " for " + str(toTestSeconds) + " seconds.")

    #GPIO.setup(int(toTest), GPIO.OUT)
    #GPIO.output(int(toTest), False)
    wait(toTestSeconds)
    #GPIO.output(int(toTest), True)







































class popupWithEntry:
    def __init__(self):
        self.popup = Tk()
        self.popup.protocol("WM_DELETE_WINDOW", self.onClose)

        self.pin = ""
        self.seconds = ""

    #def display(self, event):
    #    self.popup.mainloop()

    def onClose(self):
        print("Closing Popup")
        self.popup.destroy()
        #top.deiconify()

    def setPin(self, newPin):
        self.pin = newPin

    def getPin(self):
        return self.pin

'''def popup(event):
    w = popup(window)
    b["state"] = "disabled"
    master.wait_window(w.top)
    b["state"] = "normal"'''

'''class messageBoxWithEntry:
    def __init__(self, master):
        top = self.top = Toplevel(master)
        self.l = Label(top, text="Hello World")
        self.l.pack()
        self.e = Entry(top)
        self.e.pack()
        self.b = Button(top, text='Ok', command=self.cleanup)
        self.b.pack()

    def cleanup(self):
        self.value = self.e.get()
        self.top.destroy()
    def __init__(self):
        popup = Tk()
        Question = Label(popup, "Default Text")
        submitButton = Button("", "")

    def setQuestionText(self, new):
        self.questionText = new
        Question = Label(self.popup, new)'''