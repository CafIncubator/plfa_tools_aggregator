import unittest
import pathlib
import pandas as pd
from plfatools.aggregator import Aggregator

class Test_Aggregator(unittest.TestCase):
    
    def test_transform_raw_to_stacked_returns_expected_format(self):
        # Arrange
        path_to_formatted_xlsx = pathlib.Path.cwd() / "tests" / "assets" /  "PlfaToolAggregator_exampleTransformations.xlsx"
        formatted_xlsx = pd.ExcelFile(str(path_to_formatted_xlsx))
        expected = formatted_xlsx.parse("stacked")
        
        # Act
        actual = Aggregator().transform_raw_to_stacked(
            formatted_xlsx.parse(sheet_name="raw", header=None))

        # Assert
        # Check for same number of columns and same names
        self.assertIsInstance(actual, pd.DataFrame)
        self.assertEqual(len(expected.columns), len(actual.columns))
        self.assertEqual(len(expected.columns.difference(actual.columns)),0)

        # make sure to have the test_ for the unit test.

    def test_transform_stacked_to_tidy_returns_expected_format(self):
        
        path_to_formatted_xlsx = pathlib.Path.cwd() / "tests" / "assets" /  "PlfaToolAggregator_exampleTransformations.xlsx"
        formatted_xlsx = pd.ExcelFile(str(path_to_formatted_xlsx))
        expected = formatted_xlsx.parse("tidy")

        actual = Aggregator().tidy(
            formatted_xlsx.parse(sheet_name="stacked"))

        # Assert
        # Check for same number of columns and same names
        self.assertIsInstance(actual, pd.DataFrame)
        self.assertEqual(len(expected.columns), len(actual.columns))
        self.assertEqual(len(expected.columns.difference(actual.columns)),0)

if __name__ == "__main__":
    unittest.main()