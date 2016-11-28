try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'ex47',
	'author': 'S e e k',
	'url': 'URL to get it at.',
	'download_url': 'Where to download it.',
	'author_email': '15327700930m0@sina.cn',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': '['ex47'],
	'scripts': [],
	'name': 'ex47'
}

setup(**config)