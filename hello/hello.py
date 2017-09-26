"""
Trivial project is just for trying out Git and the
grading mechanisms.
"""

import configparser
config = configparser.ConfigParser()
config.read("credentials.py")

message = config["DEFAULT"]["message"]

print(message)
