from distutils.core import setup

setup(
    name = 'nprint',
    version = '0.1',
    package_data = {
		'': ['nprint.py'],
		},
    
    author = 'Jimy Byerley',
    author_email = 'jimy.byerley@gmail.com',
    url = 'https://github.com/jimy-byerley/nprint',
    license = "GNU GPL v3",
    description = "format and color serialized data strings, to make them more human readable",
	long_description = open('README.md').read(),
)
