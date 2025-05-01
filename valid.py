import re

def validate_zip(zip):
    if re.match("^[0-9]{5}$", zip):
        return True
    return False