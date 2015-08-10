##Vlabtool Python module and associated apps

Project logs about the hardware can be found at [Hackaday](https://hackaday.io/project/6490-a-versatile-labtool "Hackaday page for the vLabtool")

###INSTALLATION : 
The library has been uploaded to [PyPI](https://pypi.python.org/pypi/vLabtool/0.0.1 "vLabtool PyPI page"), and a debian package will hopefully be ready soon

$sudo easy_install vLabtool

This will have installed the python module for accessing the vLabtool, as well as a few basic graphical programs
These GUIs can be run from directly from a terminal


####An oscilloscope, logic analyzer, and a variety of peripheral management tools
$ vLabtool-scope


####A streaming utility.  It plots the return value of any function that is part of the vLabtool module, and which returns an Integer/float.
$ vLabtool-stream

####A selection window that allows users to pick from a variety of GUIs designed for various experiments
$ vLabtool-experiments
