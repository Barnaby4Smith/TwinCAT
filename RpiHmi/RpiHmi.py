"""
A python module for a Raspberry Pi, leveraging PyADS for communication with EtherCAT devices.
This module creates a class for a HMI (Human-Machine Interface) that can be used to interact
with EtherCAT devices, using symbols exposed on the ADS server.

The HMI features a simple dial and readout for a variable, and two buttons for control.

Initialization parameters are stored in the RpiHmi.ini file, which is read at runtime.
"""

import pyads
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QPushButton, QDial, QWidget, QLCDNumber
from PySide6.QtCore import QTimer
from PySide6.QtCore import Qt
import configparser


class RpiHmi(QMainWindow):
    """
    A class representing a Human-Machine Interface (HMI) for a Raspberry Pi using PyADS.

    Attributes:
        ads (pyads.Connection): The ADS connection to the EtherCAT device.
        symbol_name (str): The name of the symbol to be controlled by the HMI.
        dial_value (float): The current value of the dial.
        button1_state (bool): The state of button 1.
        button2_state (bool): The state of button 2.
    """

    def __init__(self, ini_file='RpiHmi.ini'):
        """
        Initializes the RpiHmi instance.
        
        Args:
            ini_file (str): Path to the INI file containing configuration settings.
        """

        super().__init__()
        
        self.ini_file = ini_file

        # ADS attributes
        self.dial_value = 0.0
        self.button1_state = False
        self.button2_state = False
        self.ams_net_id = None
        self.ams_port = None
        self.plc_ip = None
        self.counter = 0

        # GUI attributes
        self.window_title = ""
        self.window_width = 400
        self.window_height = 300

        self.load_from_ini()

        self.plc = pyads.Connection(self.ams_net_id, self.ams_port, self.plc_ip)
        self.plc.open()

        # GUI setup
        self.setWindowTitle(self.window_title)
        self.setGeometry(100, 100, self.window_width, self.window_height)

        # Create the main layout
        self.central_widget = QWidget()
        self.layout = QVBoxLayout(self.central_widget)

        # Create a label to display the dial value
        self.dial_label = QLabel(f"Dial Value: {self.dial_value}")
        self.dial_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.dial_label)

        # Create a dial to control the value
        self.dial = QDial()
        self.dial.setMinimum(0)
        self.dial.setMaximum(100)
        self.dial.setValue(int(self.dial_value))
        self.dial.valueChanged.connect(self.update_dial_value)
        self.layout.addWidget(self.dial)

        # Create a gauge (QLCDNumber) to display speed
        self.speed_gauge = QLCDNumber()
        self.speed_gauge.setDigitCount(5)
        self.speed_gauge.display(self.counter)
        self.layout.addWidget(self.speed_gauge)

        # Create Button 1
        self.button1 = QPushButton("Button 1")
        self.button1.setCheckable(True)
        self.button1.setChecked(self.button1_state)
        self.button1.clicked.connect(self.toggle_button1)
        self.layout.addWidget(self.button1)

        # Create Button 2
        self.button2 = QPushButton("Button 2")
        self.button2.setCheckable(True)
        self.button2.setChecked(self.button2_state)
        self.button2.clicked.connect(self.toggle_button2)
        self.layout.addWidget(self.button2)

        # Set the central widget
        self.setCentralWidget(self.central_widget)

        # Setup a timer to update variables
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_variables)
        self.timer.start(10) # update every 10 ms


    def update_dial_value(self, value):
        """Update the dial value in the HMI and the label."""
        self.dial_value = value
        self.dial_label.setText(f"Dial Value: {value}")
        self.save_to_ini()  # Save the updated value to the INI file

    def toggle_button1(self, checked):
        """Toggle the state of Button 1."""
        self.button1_state = checked
        self.save_to_ini()  # Save the updated state to the INI file

    def toggle_button2(self, checked):
        """Toggle the state of Button 2."""
        self.button2_state = checked
        self.save_to_ini()  # Save the updated state to the INI file

    def update_variables(self):
        """
        Update the PLC variables with the current values from the HMI.
        This method is called periodically by the QTimer.
        """

        # Update the PLC variables
        # self.plc.write_by_name('MAIN.dial_value', self.dial_value, pyads.PLCTYPE_REAL)
        # self.plc.write_by_name('MAIN.button1_state', self.button1_state, pyads.PLCTYPE_BOOL)
        # self.plc.write_by_name('MAIN.button2_state', self.button2_state, pyads.PLCTYPE_BOOL)

        # Read the updated values from the PLC
        self.counter = self.plc.read_by_name('MAIN.counter', pyads.PLCTYPE_INT)
        # self.button1_state = self.plc.read_by_name('MAIN.button1_state', pyads.PLCTYPE_BOOL)
        # self.button2_state = self.plc.read_by_name('MAIN.button2_state', pyads.PLCTYPE_BOOL)

        # Update the speed gauge display
        self.speed_gauge.display(self.counter)

    def load_from_ini(self):
        """
        Loads configuration settings from the INI file.
        """

        config = configparser.ConfigParser()
        config.read(self.ini_file)
        self.ams_net_id = config['Settings']['ams_net_id']
        self.ams_port = int(config['Settings']['ams_port'])
        self.plc_ip = config['Settings']['plc_ip']
        self.dial_value = float(config['Settings']['dial_value'])
        self.button1_state = config.getboolean('Settings', 'button1_state')
        self.button2_state = config.getboolean('Settings', 'button2_state')

        self.window_title = config['Gui'].get('window_title', 'Raspberry Pi HMI')
        self.window_width = config['Gui'].getint('window_width', 400)
        self.window_height = config['Gui'].getint('window_height', 300)

    def save_to_ini(self):
        """
        Saves the current configuration settings to the INI file.
        """

        config = configparser.ConfigParser()
        config['Settings'] = {
            'ams_net_id': self.ams_net_id,
            'ams_port': str(self.ams_port),
            'plc_ip': self.plc_ip,
            'dial_value': str(self.dial_value),
            'button1_state': str(self.button1_state),
            'button2_state': str(self.button2_state)
        }
        config['Gui'] = {
            'window_title': self.window_title,
            'window_width': str(self.window_width),
            'window_height': str(self.window_height)
        }
        with open(self.ini_file, 'w') as configfile:
            config.write(configfile)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    hmi = RpiHmi(r"C:\git\TwinCAT\RpiHmi\RpiHmi.ini")
    hmi.show()
    sys.exit(app.exec())
