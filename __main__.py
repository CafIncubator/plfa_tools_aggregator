import pathlib
from plfatools.aggregator import Aggregator
import sys


if len(sys.argv) == 3:
    dir_path = pathlib.Path(sys.argv[1]) # Cast the first argument to a Path type
    output_path_str = str(sys.argv[2]) + '\\final.csv' # Add in the name of the file to end of output path
    output_path = pathlib.Path(output_path_str) # Cast ouput path string to Path type
    final = Aggregator().read_dir(dir_path) # Aggregate
    final.to_csv(output_path, index=False) # Output excel file to path specified

else:
    print('Not enough arguments!')







# if __name__ == "__main__":
#     main()