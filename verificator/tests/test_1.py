import sys
import verificator.utils as config
import logging

def test1():
    print(__file__)
    c = config.get_configuration(__file__)
    config.loginfo("INFO", "This is test logging")
    config.loginfo("INFO", "This is test logging")
    config.loginfo("INFO", "This is test logging")
    print(c)