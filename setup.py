
import setuptools
from distutils.core import setup
import sys
import time
setup(
	# Application name:
	name="phashlib",

	# Version number (initial):
	version="0.0.1",

	# Application author details:
	author="Connor Wolf",
	author_email="github@imaginaryindustries.com",

	# Packages
	packages=setuptools.find_packages(),
	package_dir = {'phashlib': 'phashlib'},


	# Details
	url="https://github.com/fake-name/phashlib",
	#
	license='BSD 2-clause (see LICENSE file)',
	description="Image P-Hashing convenience functions.",

	long_description=open("README.md").read(),

	dependency_links=[
	],

	# Dependent packages (distributions)
	install_requires=[
		"numpy",
		"scipy",
		"pillow",
	],
)
