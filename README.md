# XYZprinting GCODE converter
This plugin was created to enable using Cura 2.6 slicer instead of XYZprinting default one (XYZWare) with the da Vinci 1.1 Plus printer.

It is simple Cura post-processing script to convert GCODE into printer's compatible format. 

The plugin was only tested with da Vinci 1.1 Plus printer but it might work with other da Vinci printers.

# Installation
Simply put the file "DaVinciConvert.py" in the folowing folder: 

[Cura 2.6 installation folder]\plugins\PostProcessingPlugin\scripts

For example on windows, if Cura was installed in the default folder, the script location folder would be: 

C:\Program Files\Cura 2.6\plugins\PostProcessingPlugin\scripts

# Usage
To use the convertion script add it from menu Extensions > Post-Processing > Modifu G-Code. Then add script "da Vinci 1.1 Plus converter". The gcode will be automatically modify after slicing.

#Options
* __Ignore temperature settings__ - ignore the temperature settings from Cura and use the cartridge's default temperatures.
