'''
    * GUI interface using QtPy (PySide6) that allows interfacing with an embedded system via
    * Raspberry Pi's GPIO pins.
    * Coded by: Ricky Dodd
'''
import sys
import time
import RPi.GPIO as GPIO
from PySide6 import QtCore, QtWidgets, QtGui

RED_PHYS_PIN   = 11
GREEN_PHYS_PIN = 13
BLUE_PHYS_PIN  = 15

class LedControlPanel(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Establishing the QtWidgets
        self.DescriptionText = QtWidgets.QLabel("Welcome to the LED Control Panel!\n" +
                "Simply press the radio button corresponding with the colour of the LED\n" +
                "you want to turn on. It'll turn it on and turn off all the others.",
                alignment=QtCore.Qt.AlignHCenter)
        self.RedButton = QtWidgets.QRadioButton("Red")
        self.GreenButton = QtWidgets.QRadioButton("Green")
        self.BlueButton = QtWidgets.QRadioButton("Blue")

        # Adding the QtWidgets to layout (showing them)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.DescriptionText)
        self.layout.addWidget(self.RedButton, alignment=QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.GreenButton, alignment=QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.BlueButton, alignment=QtCore.Qt.AlignCenter)
        
        # Event hooks
        self.RedButton.clicked.connect(self.RedEvent)
        self.GreenButton.clicked.connect(self.GreenEvent)
        self.BlueButton.clicked.connect(self.BlueEvent)
    
    def RedEvent(self):
        GPIO.output(RED_PHYS_PIN, GPIO.HIGH)
        GPIO.output(GREEN_PHYS_PIN, GPIO.LOW)
        GPIO.output(BLUE_PHYS_PIN, GPIO.LOW)
        return
    
    def GreenEvent(self):
        GPIO.output(GREEN_PHYS_PIN, GPIO.HIGH)
        GPIO.output(RED_PHYS_PIN, GPIO.LOW)
        GPIO.output(BLUE_PHYS_PIN, GPIO.LOW)
        return
    
    def BlueEvent(self):
        GPIO.output(BLUE_PHYS_PIN, GPIO.HIGH)
        GPIO.output(RED_PHYS_PIN, GPIO.LOW)
        GPIO.output(GREEN_PHYS_PIN, GPIO.LOW)
        return

def StartApplication():
    app = QtWidgets.QApplication([])

    widget = LedControlPanel()
    widget.resize(500, 500)
    widget.show()

    sys.exit(app.exec_())
    return

def GPIOSetup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(RED_PHYS_PIN,   GPIO.OUT)
    GPIO.setup(GREEN_PHYS_PIN, GPIO.OUT)
    GPIO.setup(BLUE_PHYS_PIN,  GPIO.OUT)
    return

def main():
    GPIOSetup()
    StartApplication()
    return

main()
