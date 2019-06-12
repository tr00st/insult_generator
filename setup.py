from setuptools import setup
from glob import glob
from os import path
import io

this_directory = path.abspath(path.dirname(__file__))
with io.open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='insultgenerator',
	version='1.0.3',
	packages=['insultgenerator'],
	license='MIT',
	author='James Cheese',
	author_email='trust@tr00st.co.uk',
	install_requires=['six'],
	test_suite='insultgenerator.tests',
	description='Random insult generator',
    long_description=long_description,
    long_description_content_type='text/markdown',      
	url="https://github.com/tr00st/insult_generator",
	package_data = {
		'insultgenerator': ['wordlists/*.txt'],
	},
	classifiers = [
		'Development Status :: 5 - Production/Stable',
	    'Programming Language :: Python :: 2.7',
	    'Programming Language :: Python :: 3',
	    'Programming Language :: Python :: 3.4',
	    'Programming Language :: Python :: 3.5',
	    'Programming Language :: Python :: 3.6',
	    'Programming Language :: Python :: 3.7',
	    'License :: OSI Approved :: MIT License',
	]
)
