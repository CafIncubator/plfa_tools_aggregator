import unittest
import pathlib
import pandas as pd
from plfatools.aggregator import Aggregator

class Test_Aggregator(unittest.TestCase):
    #def setup(self):
    #    self.sut = Aggregator()

    def test_transform_raw_to_stacked_returns_dataframe(self):
        # Arrange, Act, Assert
        self.assertIsInstance(
            Aggregator.transform_raw_to_stacked(""), pd.DataFrame)
    
    def test_transform_raw_to_stacked_returns_expected_format(self):
        # Arrange
        path_to_formatted_xlsx = pathlib.Path.cwd() / "tests" / "assets" /  "PlfaToolAggregator_exampleTransformations.xlsx"
        formatted_xlsx = pd.ExcelFile(path_to_formatted_xlsx)
        expected = formatted_xlsx.parse("stacked")
        
        # Act
        actual = Aggregator.transform_raw_to_stacked(formatted_xlsx.parse("raw"))

        # Assert
        # Check for same number of columns and same names
        self.assertIsInstance(actual, pd.DataFrame)
        self.assertEqual(len(expected.columns), len(actual.columns))
        self.assertEqual(len(expected.columns.difference(actual.columns)),0)

if __name__ == "__main__":
    unittest.main()
