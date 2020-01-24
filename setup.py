from distutils.core import setup
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
  classifiers=[
    'Development Status :: 4 - Beta',     
    'Intended Audience :: PLFA Users',      
    'Topic :: Data Aggregation :: Aggregator Tools',
    'License :: OSI Approved :: CC0 License',  
    'Programming Language :: Python :: 3',     
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)