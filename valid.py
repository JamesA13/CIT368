import re

class Valid:

    @staticmethod
    def validate_zip(zip):
        if re.match("^[0-9]{5}$", zip):
            return True
        return False

    @staticmethod
    def validate_response_code(resp_code):
        if(resp_code == 200):
            return True
        return False