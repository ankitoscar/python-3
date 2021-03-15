# Importing setup module
try:
    from setuptools import setup
except ImportError: # In case the previous import doesn't happen
    from distutils.core import setup

# Config dictionary
config = {
    'description': 'Ex46 project',
    'author': 'Ankit Oscar',
    'url': 'https://www.github.com/ankitoscar/python-3',
    'download_url': 'https://www.github.com/ankitoscar/python-3.git',
    'author_email': 'ankitoscar911@gmail.com',
    'version': '0.0.1',
    'install_requires': ['nose'],
    'packages': ['project'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
