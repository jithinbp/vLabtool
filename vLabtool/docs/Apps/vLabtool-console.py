#!/usr/bin/python

from vLabtool import experiment
from vLabtool import interface

if __name__ == "__main__":
	Exp=experiment.Experiment(parent=None,showresult=False)
	I = interface.Interface()
	
	Plot = Exp.add2DPlot()
	curve = Exp.addCurve(Plot,name = 'plot')
	console = Exp.addConsole(I=I)
	console.printText('\nuse built-in function "plot(x,y)" to plot data to the embedded graph')
	def plot(*args):
		curve.setData(*args)
	console.pushVariables({'plot':plot})
	Exp.run()
