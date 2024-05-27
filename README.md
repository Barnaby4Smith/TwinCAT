# TwinCAT
A WIP repository for projects related to TwinCAT.

![Alt Text](images\20240527_215810.jpg)

## TwinCAT
The repository contains a sandbox TwinCAT project that exercises some basic features of TwinCAT. A simple program has been written to demonstrate how to use Beckhoff I/O using structured text within the TwinCAT XAE. This program response to button presses and a 4-20mA input from a potentiometer, and outputs to two LED indicators.

### TwinCAT Measurement Project
The project includes a TwinCAT measurement project, showing how symbols from within the project can be logged as part of testing or debugging, without the use of an external tool.

![Alt Text](images\TwinCAT_Measurement_Project.png)

### TwinCAT Dashboard Webpage
TwinCAT includes a feature for serving webpages from a target. This enables development of GUIs for control and monitoring. This example includes a simple example of a GUI, showing the status of the LED outputs and the 4-20mA inputs.

![Alt Text](images\DashboardWebpage.png)

## SolidEdge
A simplified CAD model of the test setup has been produced using SolidEdge. This includes custom 3D printed components for the DIN rail stand, and the DIN mounted control panel.

![Alt Text](images\Beckhoff_Development_Rig_4-1.jpg)

## ADS - Python and LabVIEW
The [pyads](https://github.com/stlehmann/pyads) python package is a python wrapper for the TwinCAT ADS library that provides python functions for communicating with TwinCAT devices. Similarly, the [TwinCAT 3 Interface for LabVIEW](https://www.beckhoff.com/en-gb/products/automation/twincat/tfxxxx-twincat-3-functions/tf3xxx-measurement/tf3710.html?) enables communication with TwinCAT devices through LabVIEW. This repository explores the use of this package to enable control of TwinCAT devices using high level scripting languages, narrowing the range of programming skills required by developers.

## Schematics, BOM and manufacturing data
WIP - Schematics, BOM (Bill Of Materials) and other manufacturing data required to reproduce the development setup.



