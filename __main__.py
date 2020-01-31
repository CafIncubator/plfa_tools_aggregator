import pathlib
from plfatools.aggregator import Aggregator
import sys


if len(sys.argv) == 3:
    dir_path = pathlib.Path(sys.argv[1])
    output_path_str = str(sys.argv[2]) + 'final.xlsx'
    output_path = pathlib.Path(output_path_str)
    final = Aggregator().read_dir(dir_path)
    final.to_excel(output_path, index=False)
else:
    print('Not enough arguments!')







#if __name__ == "__main__":
#    main()