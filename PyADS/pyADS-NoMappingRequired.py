""" pyADS-NoMappingRequired.py
    This script is a work in progress, and is intended to demonstrate how to
    access I/O devices within the TwinCAT project without the need to map them to
    a symbol within the the TwinCAT project."""


import time
import sys
import clr
import pyads

clr.AddReference(r'C:\TwinCAT\AdsApi\.NET\v4.0.30319\TwinCAT.Ads')
import TwinCAT
import TwinCAT.Ads
import TwinCAT.Ads.TypeSystem as TypeSystem

def __getSymbols__():
    """ recursively get all symbols from the TwinCAT project """



# create a session id object instance
sessionID = TwinCAT.Ads.AmsNetId('5.29.104.106.1.1')
# 5.29.104.106.1.1
# create an AdsSession object instance
adsSession = TwinCAT.Ads.AdsSession(sessionID, 27906)
# pyads.PORT_TC3PLC1
# connect to the session
adsSession.Connect()

# check if the session is connected
isConnected = adsSession.IsConnected

# session is connected, proceed with obtaining symbols
# create a symbol loader factory object
SymbolLoaderFactory = TypeSystem.SymbolLoaderFactory()

# create a symbol loader settings object
settings = TwinCAT.Ads.SymbolLoaderSettings(TwinCAT.SymbolsLoadMode.DynamicTree)

# call the create method of the symbol loader factory object
SymbolLoader = SymbolLoaderFactory.Create(adsSession.Connection, settings)

idx = SymbolLoader.Symbols.Count

symbols = []

# get the instance path of each symbol
for i in range(idx):
    symbol = SymbolLoader.Symbols.get_Item(i)
    symbols.append((symbol.InstanceName, symbol.InstancePath, symbol.Comment))

    symbol = None

# remove references to the symbol loader and symbol loader factory objects
SymbolLoader = None
settings = None
SymbolLoaderFactory = None

adsSession.Disconnect()

adsSession.Dispose()

adsSession = None