from setuptools import setup
from glob import glob
setup(name='insultgenerator',
	version='0.3',
	packages=['insultgenerator'],
	license='MIT',
	author='James Cheese',
	author_email='trust@tr00st.co.uk',
	install_requires=['six'],
	test_suite='insultgenerator.tests',
	description='Random insult generator',
	url="https://github.com/tr00st/insult_generator",
	package_data = {
		'insultgenerator': ['wordlists/*.txt'],
	},
	classifiers = [
		'Development Status :: 3 - Alpha',
	    'Programming Language :: Python :: 2.7',
	    'Programming Language :: Python :: 3',
	    'Programming Language :: Python :: 3.4',
	    'Programming Language :: Python :: 3.5',
	    'Programming Language :: Python :: 3.6',
	    'Programming Language :: Python :: 3.7',
	    'License :: OSI Approved :: MIT License',
	]
)
