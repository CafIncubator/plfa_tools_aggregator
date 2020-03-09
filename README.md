# PLFA Tools Aggregator

## Purpose

The MIDI Inc. Sherlock PLFA Analysis Software has a paid add-on package called PLFA Tools. The software takes as input GC results of PLFA (and NLFA) samples and assigns peaks to categories (General FAME, Gram Negative, etc.). The software creates a new Excel Worksheet for each sample, resulting in 100s of worksheets of various formats. The purpose of this package is to automate the aggregation of the data into a single csv file for analysis.

## License

As a work of the United States government, this project is in the public domain within the United States.

Additionally, we waive copyright and related rights in the work worldwide through the CC0 1.0 Universal public domain dedication.

## Contents

Files for plfatools, version 0.1.0:
* plfatools-0.1.0.tar.gz : Contains the entire PLFA Tools Aggregator package including aggregator class and tests.

## Installation information
Can be installed using pip install.

Must be using python 3.0.0 or later to use this package.

## Using this package
Can use via the command line by running the main file within the aggregator package. It takes two arguments: The first being the file directory to the files to be 
aggregated and the second being where you want the final.xlsx file to be outputted.
**Note**: If there are other .xlsx files in the directory to be aggregated this will cause errors as the main file assumes all the excel files in the directory are GC results. 

