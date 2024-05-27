""" pyadsTest.py
    This script tests the connection to the PLC, and performs several operations
    to demonstrate some basic functionality of the pyads library.
    
    The script opens a connection to the PLC, writes to the start and stop buttons,
    reads the state of the start button LED, and prints all symbols from the PLC.
    
    This script has a dependency on the TwinCAT Sandbox project, which must be running
    and must have a global variable list (GVL) with the following variables:
    DO0: BOOL
    DI0_OR: BOOL
    DI1_OR: BOOL
    DI2_AND: BOOL
    """

import time
import pyads

plc = pyads.Connection('5.29.104.106.1.1', pyads.PORT_TC3PLC1)

plc.open()

# press the start button
plc.write_by_name('GVL.DI0_OR', 1)
time.sleep(1)
plc.write_by_name('GVL.DI0_OR', 0)


# read the value of the start button LED
for i in range(10):
    print(f"DO0 state: {plc.read_by_name('GVL.DO0')}")
    time.sleep(1) 

# press the stop button
plc.write_by_name('GVL.DI1_OR', 1)
time.sleep(1)
plc.write_by_name('GVL.DI1_OR', 0)

symbols = plc.get_all_symbols()

# print all symbols
for symbol in symbols:
    print(f"{symbol.name} {symbol.comment}")

plc.close()
