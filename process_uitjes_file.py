"""
This module contains all the functions that are related to the
processing of the csv files.
"""

import csv
import glob
from random import randrange
import os

import set_logger_profile

"""Set the logger profile"""
logger = set_logger_profile.logger(name=str(os.path.basename(__file__)),
                                   level=10,
                                   formatter="%(asctime)s "
                                             "- %(name)s "
                                             "- %(funcName)s "
                                             "- %(levelname)s "
                                             "- %(message)s ")


def get_total_rows_csv_file(source: str) -> int:
    """
    returns the number of total rows that are in the file.
    The "_unused" syntax is conform convention.
    """
    for filename in glob.glob(source):
        with open(filename, encoding="utf-8") as csv_file:
            read_csv = csv.reader(csv_file, delimiter=';')
            next(read_csv)  # skip header
            row_count = sum(1 for _unused in csv_file)
            # count the row numbers in the file & save in row_count.
            return row_count


def set_randint_csv_file(source: str) -> int:
    """
    returns an random row number that is a product in the csv file.
    The "_unused" syntax is conform convention.
    """
    for filename in glob.glob(source):
        with open(filename, encoding="utf-8") as csv_file:
            read_csv = csv.reader(csv_file, delimiter=';')
            next(read_csv)  # skip header
            row_count = sum(1 for _unused in csv_file)
            # count the row numbers in the file & save in row_count.
            random_int_voorraad_file = randrange(row_count)
            # set an random integer between 0 and the row_count
            return random_int_voorraad_file


def get_row_file(source: str,
                 row_file: int) -> dict:
    """
    Return the row for the number that is stored in row_voorraad_file
    as an dictionary data type.
    Be careful, it is not sure that the returned value is in stock.
    """
    for filename in glob.glob(source):
        with open(filename, encoding="utf-8") as voorraad_file:
            read_csv = csv.DictReader(voorraad_file, delimiter=';')
            iterator = 1
            for row in read_csv:
                iterator += 1
                if row_file == iterator:
                    return row
