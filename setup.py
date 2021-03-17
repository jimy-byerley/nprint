from setuptools import setup

setup(
	name = 'pnprint',
	version = '1.0',
	package_data = {
		'': ['nprint.py'],
		},
	
	# metadata for pypi
	author = 'Jimy Byerley',
	author_email = 'jimy.byerley@gmail.com',
	url = 'https://github.com/jimy-byerley/nprint',
	license = "GNU LGPL v3",
	description = "format and color serialized data strings, to make them more human readable",
	long_description = open('README.md').read(),
	long_description_content_type = 'text/markdown',
)
