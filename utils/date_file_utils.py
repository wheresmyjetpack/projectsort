#!/usr/bin/python

import os
from datetime import datetime

def is_dated(f):
    # Check to see if a file/dir name begins with a properly formatted date
    try:
        datetime.strptime(*date_slice(f))    # Unpack two-tuple returned from date_slice()
        return True
    
    except ValueError:
        return False

def is_a_dir(dir):
    # os.path.isdir wrapper
    return os.path.isdir(os.path.abspath(dir))

def date_slice(f):
    # Returns a two-tuple containing a timestamp string and the format string
    if is_a_dir(f):
        return str(os.path.basename(f))[0:10], '%Y-%m-%d'    # YYYY-MM-DD

    else:
        return str(os.path.basename(f))[0:19], '%Y-%m-%d-%H-%M-%S'    # YYYY-MM-DD-HH-mm-ss
    
def get_new_dir(f):
    # Uses a filename to return the new timestamped directory name
    # Only includes the year, month and day from the filename
    return date_slice(f)[0][0:10]
