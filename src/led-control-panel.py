'''
    * GUI interface using QtPy (PySide6) that allows interfacing with an embedded system via
    * Raspberry Pi's GPIO pins.
    * Coded by: Ricky Dodd
'''
import sys
import time
import RPi.GPIO as GPIO
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QRadioButton, QVBoxLayout
from PyQt5.QtCore import pyqtSlot

RED_PHYS_PIN   = 11
GREEN_PHYS_PIN = 13
BLUE_PHYS_PIN  = 15

class App(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "LED Control Panel"
        self.left = 0
        self.top = 0
        self.width = 500
        self.height = 500
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.control_panel_widget = LedControlPanel(self)
        self.setCentralWidget(self.control_panel_widget)

        self.show()

    def closeEvent(self, event):
        GPIO.output(RED_PHYS_PIN, GPIO.LOW)
        GPIO.output(GREEN_PHYS_PIN, GPIO.LOW)
        GPIO.output(BLUE_PHYS_PIN, GPIO.LOW)
        event.accept()
        return

class LedControlPanel(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        # Establishing the QtWidgets
        self.DescriptionText = QLabel("Welcome to the LED Control Panel!\n" +
                "Simply press the radio button corresponding with the colour of the LED\n" +
                "you want to turn on. It'll turn it on and turn off all the others.",)
        self.RedButton = QRadioButton("Red")
        self.GreenButton = QRadioButton("Green")
        self.BlueButton = QRadioButton("Blue")

        # Adding the QtWidgets to layout (showing them)
        self.layout.addWidget(self.DescriptionText)
        self.layout.addWidget(self.RedButton)
        self.layout.addWidget(self.GreenButton)
        self.layout.addWidget(self.BlueButton)

        # Event hooks
        self.RedButton.clicked.connect(self.RedEvent)
        self.GreenButton.clicked.connect(self.GreenEvent)
        self.BlueButton.clicked.connect(self.BlueEvent)

    @pyqtSlot()
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
    app = QApplication(sys.argv)
    ex = App()
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
