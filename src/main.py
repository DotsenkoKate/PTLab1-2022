# -*- coding: utf-8 -*-
import argparse
import sys
import os.path

from CalcRating import CalcRating
from TextDataReader import TextDataReader
from JsonReader import JsonReader

def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path

def main():
    path = get_path_from_arguments(sys.argv[1:])

    match os.path.splitext(path):
        case _, '.txt':
            reader = TextDataReader()
        case _, '.json':
            reader = JsonReader()
        case _:
            raise ValueError("Invalid file format")

    students = reader.read(path)
    print("Students: ", students)

    rating = CalcRating(students).calc()
    print("Rating: ", rating)

if __name__ == "__main__":
    main()
