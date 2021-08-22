"""
This module is designed to provide system functions.
"""

import shutil
import getpass
import glob
import unicodedata
import string
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


def delete_files_in_downloads(username: str = "sande") -> bool:
    """
    Delete all the files in the downloads folder.
    The username is dynamic because this can be different between machines.
    This function is created for Windows machines.
    """
    logger.debug(username)
    shutil.rmtree('C:/Users/'+username+'/Downloads/', ignore_errors=True)
    return True


def delete_file(path: str) -> bool:
    """
    Deletes a specific file.
    If the file is not present the function will return False.
    This function is created for Windows machines.
    """
    try:
        os.remove(path)
        return True
    except Exception as e:
        logger.critical(e)
        return False


def get_list_of_files_in_folder(
        source: str = "C:/Users/sande/Downloads/",
        file_extension: str = "*.*") -> list:
    """
    Returns an list of files that are in an folder.
    If there are no files an empty list is returned.
    """
    logger.debug("source: " + source)
    logger.debug("file_extension: " + file_extension)
    source_glob = source + file_extension
    list_of_files = []
    for filename in glob.glob(source_glob):
        list_of_files.append(filename)
    return list_of_files


def clean_filename(filename: str,
                   whitelist="-_.() %s%s" % (string.ascii_letters,
                                             string.digits),
                   replace=' ',
                   char_limit=255,):
    """
    Use any character in the current code page for a name, including:
        Unicode characters
        characters in the extended character set (128–255).
    Except for the following reserved characters:
        < (less than)
        > (greater than)
        : (colon)
        " (double quote)
        / (forward slash)
        \\ (backslash)
        | (vertical bar or pipe)
        ? (question mark)
        * (asterisk)
    source: https://docs.microsoft.com/en-us/windows/win32/fileio/naming-a-file
    Spaces " " are converted to an underscore "_".
    Uppercase letters are converted to lowercase letters.
    """
    logger.debug("filename: " + str(filename))
    for space in replace:
        filename = filename.replace(space, '_')
    logger.debug("replaced spaces filename: " + str(filename))
    # keep only valid ascii chars
    cleaned_filename = \
        unicodedata.normalize('NFKD',
                              filename).encode('ASCII',
                                               'ignore').decode()
    logger.debug("only valid ascii chars cleaned_filename: "
                 + str(cleaned_filename))
    cleaned_filename = ''.join(char for char in cleaned_filename
                               if char in whitelist)
    if len(cleaned_filename) > char_limit:
        logger.info("Warning, filename truncated because it was over "
                    + str(char_limit)
                    + " characters. "
                    "Filename may no longer be unique.")
    logger.debug("whitelisted chars cleaned_filename: "
                 + str(cleaned_filename))
    cleaned_filename = cleaned_filename.lower()
    logger.debug("lowercase cleaned_filename: " + str(cleaned_filename))
    return cleaned_filename[:char_limit]
