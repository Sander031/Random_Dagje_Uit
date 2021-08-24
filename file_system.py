"""
This module is designed to provide system functions.
"""

import getpass
import os

import set_logger_profile


"""Set the logger profile."""
logger = set_logger_profile.logger(name=str(os.path.basename(__file__)),
                                   level=10,
                                   formatter="%(asctime)s "
                                             "- %(name)s "
                                             "- %(funcName)s "
                                             "- %(levelname)s "
                                             "- %(message)s ")


def get_username() -> str:
    """
    Returns the system specific username as a string.
    Example "sande" or "Sander".
    """
    username = getpass.getuser()
    logger.debug("get_username func: " + username)
    return username
