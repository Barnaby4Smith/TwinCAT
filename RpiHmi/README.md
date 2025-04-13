# TwinCAT Raspberry Pi HMI

## Notes:
1. ADS route will need to be added between the PLC and every HMI being used. This can be done on the PLC webpage.
2. The python code may require 3 parameters to setup a connection

## ToDo:
1. Script needs to be deployable
    - IP address should be variable
    - deploy via docker container through kubernetes
    - Symbols will all be created on the PLC - symbols need to be dynamic

2. RPI should run in kisok mode, e.g. no settings or keyboard, just the HMI

3. 
