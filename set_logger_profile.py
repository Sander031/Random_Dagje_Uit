"""
Setting up of the logging mechanism.
More can be found here https://docs.python.org/3/library/logging.html
"""
import logging


def logger(name="",
           level=20,
           formatter="%(asctime)s "
                     "- %(name)s "
                     "- %(levelname)s "
                     "- %(message)s "):
    """
    Level       Numlvl  Logging Function        Description
    DEBUG       10      logging.debug()         The lowest level.
                                                Used for small details.
                                                Usually you care about these
                                                messages
                                                only when diagnosing problems.
    INFO        20      logging.info()          Used to record information on
                                                general events in your program
                                                or confirm that
                                                things are working at their
                                                point in the program.
    WARNING     30      logging.warning()       Used to indicate a potential
                                                problem that does not prevent
                                                the program from working
                                                but might do so in the future.
    ERROR       40      logging.error()         Used to record an error that
                                                caused the program to fail to
                                                do something.
    CRITICAL    50      logging.critical()      The highest level.
                                                Used to indicate a fatal error
                                                that has caused or is about
                                                to cause the program to stop
                                                running entirely.
    Keyword arguments:
    name        Name of the logger used to log the call.
                e.g. str(os.path.basename(__file__) or __name__
    level       Numeric logging level for the message (DEBUG,
                                                       INFO,
                                                       WARNING,
                                                       ERROR,
                                                       CRITICAL).
    formatter   LogRecord attributes
                %(asctime)s
                    Human-readable time when the LogRecord was created.
                    By default this is of the form ‘2003-07-08 16:49:45,896’
                    (the numbers after the comma are millisecond portion
                    of the time).
                %(name)s
                    Name of the logger used to log the call.
                %(levelname)s
                    Text logging level for the message ('DEBUG',
                                                        'INFO',
                                                        'WARNING',
                                                        'ERROR',
                                                        'CRITICAL').
                %(message)s
                    The logged message, computed as msg % args.
                    This is set when Formatter.format() is invoked.
    """
    logger_profile = logging.getLogger(name)
    logger_profile.setLevel(level)
    formatter = logging.Formatter(formatter)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger_profile.addHandler(stream_handler)
    return logger_profile
