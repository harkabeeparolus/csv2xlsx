#! /usr/bin/env python3

"""
Converts a TSV (tab delimited) or CSV (comma delimited) file to an Excel xlsx
file.

If the file name matches *.txt, TSV is assumed.
Otherwise, CSV is assumed and auto-detected.
"""

# By Fredrik Mellström <https://github.com/harkabeeparolus>
# Based on https://gist.github.com/konrad/4154786 by Konrad Förstner

import argparse
import sys

from csv2xlsx import __version__
from csv2xlsx import convert


def main(arguments=None):
    "Parse arguments and run csv2xlsx from the command line."
    if arguments is None:
        arguments = sys.argv[1:]

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "-n",
        "--numbers",
        action="store_true",
        help="convert integers and floats to Excel numbers",
    )
    parser.add_argument("-V", "--version", action="version", version=__version__)
    parser.add_argument("input_file")
    args = parser.parse_args(arguments)

    xlsxfile = convert.write_excel(args.input_file, convert_numbers=args.numbers)

    if xlsxfile:
        print(f"Saved to file: {xlsxfile}")
    else:
        print(f"error: Could not convert {args.input_file}")

    return 0


if __name__ == "__main__":
    sys.exit(main())


# EOF
