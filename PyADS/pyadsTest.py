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

# print all symbols from the GVL variables file
for symbol in symbols:
    # if the name string contains 'GVL' then print the name
    if symbol.name.find('GVL') != -1:
        print(f"{symbol.name} {symbol.comment}")

plc.close()
