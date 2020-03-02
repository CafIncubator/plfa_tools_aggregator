from setuptools import setup
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
setup(
  name = 'plfatools',         
  packages = ['plfatools'], 
  version = '0.1.0',      
  license='CC0',        
  description = 'The purpose of this package is to automate the aggregation of the data into a single csv file for analysis.', 
  author = 'Patrick Morrell, Bryan Carlson',                   
  author_email = 'bryan.carlson@usda.gov',     
  url = 'https://github.com/cafltar/plfa_tools_aggregator',   
  download_url = 'https://github.com/cafltar/plfa_tools_aggregator.git',   
  keywords = ['Aggregator', 'PLFA', 'CSV'],   
  install_requires=  ['pathlib', 'pandas', 'numpy'],
  entry_points = {"console_scripts": ["plfatools=plfatools.__main__:main"]},
  long_description = long_description,
  long_description_content_type='text/markdown',
  classifiers=[
    'Development Status :: 4 - Beta',     
		'Intended Audience :: Science/Research',      
		'Topic :: Scientific/Engineering',
		'Topic :: Scientific/Engineering :: Bio-Informatics',
		'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',  
		'Programming Language :: Python :: 3'
  ],
)