import datetime

class Log:
    @staticmethod
    def log(zip, code):
        timestamp = datetime.datetime.now()
        f = open("logs.txt", "a")
        f.write("ZIP code: " + str(zip) + "; Time: " + str(timestamp) + "; Response Code: " + str(code) + "\n")
        f.close()
        return