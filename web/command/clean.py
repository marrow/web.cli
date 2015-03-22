# encoding: utf-8

from __future__ import unicode_literals, print_function

import os

from functools import partial

from marrow.package.host import PluginManager


def clean_python(cli, pretend=False):
	count = 0
	
	for base, directories, files in os.walk('.'):
		if os.path.basename(base).startswith('.'):
			continue
		
		for name in filter(lambda path: os.path.splitext(path)[1] in ('.pyc', '.pyo'), files):
			path = os.path.abspath(os.path.join(base, name))
			
			if cli.verbose:
				print(path)
			
			if not pretend:
				os.remove(path)
			
			count += 1
	
	if cli.verbose:
		print()
	
	if not pretend:
		print("Removed {0} bytecode files.".format(count))
	else:
		print("Would have removed {0} bytecode files.".format(count))


def clean(cli, pretend=False, plugins=None: partial(str.split, sep=',')):
	"""Search for and remove compiled Python bytecode."""
	
	for cleaner in PluginManager('web.clean', plugins):
		cleaner(cli, pretend=pretend)
