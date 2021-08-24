"""
This module contains all the functions that are related to the
processing of the csv files.
"""

import csv
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


def set_randint_csv_file(source: str) -> int:
    """
    returns an random row number that is a product in the csv file.
    The "_unused" syntax is conform convention.
    """
    with open(source, encoding="utf-8") as csv_file:
        read_csv = csv.reader(csv_file, delimiter=';')
        next(read_csv)  # skip header
        row_count = sum(1 for _unused in csv_file)
        logger.debug("row_count: " + str(row_count))
        # count the row numbers in the file & save in row_count.
        random_int_file = randrange(1, row_count)
        # set an random integer between 0 and the row_count
        return random_int_file


def get_row_file(source: str,
                 row_file: int) -> dict:
    """
    Return the row for the number that is stored in row_file
    as an dictionary data type.
    """
    with open(source, encoding="utf-8") as uitjes_file:
        read_csv = csv.DictReader(uitjes_file, delimiter=';')
        iterator = 0
        for row in read_csv:
            iterator += 1
            if row_file == iterator:
                return row
