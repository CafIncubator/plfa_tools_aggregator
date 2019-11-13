# -*- coding: utf-8 -*-
#%%
"""

"""

import pathlib
import pandas as pd

class Aggregator():
   
    def transform_raw_to_stacked(self, plfa_tools_output: pd.DataFrame) -> pd.DataFrame:
        """Reformats output from PLFA Tools, of a single sample, into proper tabular format
        plfa_tools_output = Output from PLFA Tools of a single worksheet in the form of a Pandas DataFrame
        
        Header names: SampleId, GCRunId, GCFileLoc, ProcessingCode, ProcessMethod, RunDateTime, RT, Response, Ar/Ht, RFact, ECL, Peak Name, Percent, Comment1, Comment2
        """

        # Read in disjunct values
        SampleId = plfa_tools_output.iloc[2,2]
        GCRunId = plfa_tools_output.iloc[2,1]
        GCFileLoc = plfa_tools_output.iloc[0, 6]
        ProcessingCode = plfa_tools_output.iloc[0,7]
        ProcessingMethod = plfa_tools_output.iloc[3,6]
        RunDateTime = plfa_tools_output.iloc[3,7]
        
        # Copy input df, extract out table of results, set headers
        result = pd.DataFrame(plfa_tools_output)
        result.drop(result.head(5).index, inplace = True)
        result.drop(result.tail(5).index, inplace = True)
        result.columns = result.iloc[0]
        result = result[1:]
        
        # Create columns for disjunct values
        result.insert(0, 'RunDateTime', RunDateTime)
        result.insert(0, 'ProcessingMethod', ProcessingMethod)
        result.insert(0, 'ProcessingCode', ProcessingCode)
        result.insert(0, 'GCFileLoc', GCFileLoc)
        result.insert(0, 'GCRunID', GCRunId)
        result.insert(0, 'SampleID', SampleId)

        #result['SampleID'] = SampleId
        #result['GCRunID'] = GCRunId
        #result['GCFileLoc'] = GCFileLoc
        #result['ProcessingCode'] = ProcessingCode
        #result['ProcessingMethod'] = ProcessingMethod
        #result['RunDateTime'] = RunDateTime

        return result
        
    def read_file(self, file_path: pathlib.Path) -> pd.DataFrame:
        """Reads a file from PLFA Tools and returns a pandas DataFrame with all data from all worksheets
        file_path = pathlib Path to a xlsx file as produced by PLFA Tools
        """

    def read_dir(self, dir_path: pathlib.Path) -> pd.DataFrame:
        """Reads a directory path that contains multiple files from PLFA Tools and returns a pandas DataFrame with all data from all files and worksheets
        dir_path = pathlib Path to directory containing one or more xlsx files as produced by PLFA Tools
        """

    def tidy(self, df: pd.DataFrame) -> pd.DataFrame:
        """Accepts a Pandas DataFrame generated by "read_dir" or "read_file" and returns a new DataFrame in a tidy format
        df = Pandas DataFrame generated by "read_dir" or "read_file"
        """
        measurement_vars = ['SampleID', 'Peak Name', 'Response']
        drop_vars_meta = ['Peak Name', 'Response']
        drop_vars = ['RT', 'Ar/Ht', 'RFact', 'ECL', 'Percent', 'Comment1', 'Comment2']
        meta_df = df.drop(drop_vars, axis = 1).drop(drop_vars_meta, axis = 1)
        measurement_df = df[measurement_vars]
        tidy_peaks = measurement_df.pivot(index='SampleID', columns='Peak Name', values='Response')
        meta_df = meta_df.drop_duplicates()
        tidy = pd.merge(meta_df, tidy_peaks, on = 'SampleID')
        return tidy
 

#%%
