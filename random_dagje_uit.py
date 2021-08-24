"""
This program selects one random uitje from an CSV file.
The selection is based on the desired loaction.

"""

__author__ = "Sander Timmermans"

import time
import os

import process_uitjes_file
import file_system
import set_logger_profile


"""Set the logger profile"""
logger = set_logger_profile.logger(name=str(os.path.basename(__file__)),
                                   level=10,
                                   formatter="%(asctime)s "
                                             "- %(name)s "
                                             "- %(levelname)s "
                                             "- %(message)s ")

"""
Begroeten van de kids en vragen wat voor uitje ze vandaag willen ondernemen. 
"""
welkom = "Hoi Mick en Zoë, willen jullie vandaag iets Binnen- of Buiten doen?"
input_binnen_of_buiten = input(welkom)

"""
Uitjes bestandslocatie bepalen. 
"""
system_user_name = file_system.get_username()

data_file_path = "C:/Users/" \
                 + system_user_name \
                 + "/OneDrive/Python_Programs/Random_Dagje_Uit/Uitjes.csv"

"""
Check if the uitje in the row dictionary variable is equal to the kids input.
"""

i = 0
while i == 0:
    """
    Determine an random row number in the uitjes file.
    """
    random_row_file = process_uitjes_file.set_randint_csv_file(
        data_file_path)
    logger.debug("random_row_file: " + str(random_row_file))
    """
    Get the row details from the file.
    """
    row = process_uitjes_file.get_row_file(data_file_path,
                                           random_row_file)
    logger.debug(row)
    logger.debug(row["Uitje"])
    logger.debug(row["Binnen_of_Buiten"])

    if row["Binnen_of_Buiten"] != input_binnen_of_buiten:
        logger.debug("Continue the while loop")
        continue
    if row["Binnen_of_Buiten"] == input_binnen_of_buiten:
        logger.debug("Break the while loop")
        break

time.sleep(1)
print("We gaan dit doen! " + row["Uitje"])
time.sleep(10)
