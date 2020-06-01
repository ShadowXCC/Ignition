import GUIFunctions
from tkinter import *

def onClose():
    print("Closing")
    #GPIO.cleanup()
    window.destroy()

def popup(event):
    p = GUIFunctions.popupWithEntry()
    #window.withdraw()

def deiconify():
    window.deiconify()

window = Tk()

window.title("Ignition")
window.iconbitmap("flameIco.ico")
#window.geometry("500x500")
window.resizable(0, 0)

class App:
    def __init__(self, parent):
        buttonOne = Button(window, text = "Turn on ZombieCuda", fg = "green")
        buttonOne.grid(row = 0, column = 0, sticky = W)
        buttonOne.bind("<Button-1>", GUIFunctions.turnOnDeviceOne)
        buttonTwo = Button(window, text = "Turn off ZombieCuda", fg = "red")
        buttonTwo.grid(row = 0, column = 3, sticky = E)
        buttonTwo.bind("<Button-1>", GUIFunctions.turnOffDeviceOne)

        buttonThree = Button(window, text = "Turn on ___", fg = "green")
        buttonThree.grid(row = 1, column = 0, sticky = W)
        buttonThree.bind("<Button-1>", GUIFunctions.turnOnDeviceTwo)
        buttonFour = Button(window, text = "Turn off ___", fg = "red")
        buttonFour.grid(row = 1, column = 3, sticky = E)
        buttonFour.bind("<Button-1>", GUIFunctions.turnOffDeviceTwo)

        buttonFive = Button(window, text = "Turn on ___", fg = "green")
        buttonFive.grid(row = 2, column = 0, sticky = W)
        buttonFive.bind("<Button-1>", GUIFunctions.turnOnDeviceThree)
        buttonSix = Button(window, text = "Turn off ___", fg = "red")
        buttonSix.grid(row = 2, column = 3, sticky = E)
        buttonSix.bind("<Button-1>", GUIFunctions.turnOffDeviceThree)

        buttonSeven = Button(window, text = "Turn on ___", fg = "green")
        buttonSeven.grid(row = 3, column = 0, sticky = W)
        buttonSeven.bind("<Button-1>", GUIFunctions.turnOnDeviceFour)
        buttonEight = Button(window, text = "Turn off ___", fg = "red")
        buttonEight.grid(row = 3, column = 3, sticky = E)
        buttonEight.bind("<Button-1>", GUIFunctions.turnOffDeviceFour)

        buttonNine = Button(window, text = "Test Pin #", fg = "blue")
        buttonNine.grid(row = 5, column = 2)
        #buttonNine.bind("<Button-1>", GUIFunctions.testPin)
        buttonNine.bind("<Button-1>", popup)

app = App(window)
window.protocol("WM_DELETE_WINDOW", onClose)
window.mainloop()