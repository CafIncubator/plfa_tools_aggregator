from distutils.core import setup
setup(
  name = 'PLFA_Tools_Aggregator',         # How you named your package folder (MyLib)
  packages = ['PLFA_Tools_Aggregator'],   # Chose the same as "name"
  version = '0.0.1',      # Start with a small number and increase it with every change you make
  license='CC0',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'The purpose of this package is to automate the aggregation of the data into a single csv file for analysis.',   # Give a short description about your library
  author = 'Patrick Morrell',                   # Type in your name
  author_email = 'bryan.carlson@usda.gov',      # Type in your E-Mail
  url = 'https://github.com/cafltar/plfa_tools_aggregator',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/cafltar/plfa_tools_aggregator.git',    # I explain this later on
  keywords = ['Aggregator', 'PLFA', 'CSV'],   # Keywords that define your package best
  install_requires=  ['pathlib', 'pandas', 'numpy'],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: PLFA Users',      # Define that your audience are developers
    'Topic :: Data Aggregation :: Aggregator Tools',
    'License :: OSI Approved :: CC0 License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)