#!/usr/bin/env python

#from distutils.core import setup
from setuptools import setup, find_packages
from setuptools.command.install import install
import os,shutil
from distutils.util import execute
from distutils.cmd import Command
from subprocess import call



def udev_reload_rules():
	call(["udevadm", "control", "--reload-rules"])

def udev_trigger():
	call(["udevadm", "trigger", "--subsystem-match=usb","--attr-match=idVendor=04d8", "--action=add"])

def install_udev_rules(raise_exception):
	if check_root():
		shutil.copy('vLabtool/calib_data/proto.rules', '/etc/udev/rules.d')
		execute(udev_reload_rules, [], "Reloading udev rules")
		execute(udev_trigger, [], "Triggering udev rules")
	else:
		msg = "You must have root privileges to install udev rules. Run 'sudo python setup.py install'"
		if raise_exception:
			raise OSError(msg)
		else:
			print(msg)

def check_root():
	return os.geteuid() == 0

class CustomInstall(install):
	def run(self):
		install_udev_rules(True)
		install.run(self)


setup(name='vLabtool',
	version='0.0.1',
	description='Package to deal with vLabtool',
	author='Jithin B.P.',
	author_email='jithinbp@gmail.com',
	url='https://www.jithinbp.in/',
	install_requires = ['numpy>=1.8.1','pyqtgraph>=0.9.10'],
	packages=find_packages(),#['Labtools', 'Labtools.widgets'],
	scripts=["vLabtool/bin/vLabtool-scope","vLabtool/bin/vLabtool-stream","vLabtool/bin/vLabtool-experiments"],
	package_data={'': ['*.css','*.png']},
	cmdclass={'install': CustomInstall},
	)
