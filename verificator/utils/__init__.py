import os
import yaml
import platform
import logging
TN=""
loglevel = 3
rootDir = ""
logPath = ""

def get_configuration(path_to_test):
    """function returns configuration for environment
    and for test if it's specified"""
    """
    print(__file__)
    global_config_file = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "../config.yaml")
    """
    global TN
    delimiter = getDelimiter()
    nameList = path_to_test.split(delimiter)
    global rootDir
    for name in nameList:
        rootDir  = rootDir + name + delimiter
        if name == "scenarioTestFramework":
            break
            
    global_config_file = rootDir + delimiter + "verificator" + delimiter + "config.yml"
    TN=nameList[-1]

    with open(global_config_file, 'r') as file:
        global_config = yaml.load(file)

    config_file = os.path.join(
        os.path.dirname(os.path.abspath(path_to_test)), "config.yml")


    if os.path.exists(config_file):
        with open(config_file, 'r') as file:
            global_config.update(yaml.load(file))
            
    global loglevel
    loglevel = global_config['loglevel']
    return global_config
    
def loginfo(tag, msg):
    global TN
    global loglevel
    global logPath
    delimiter = getDelimiter()
    logDirPath = rootDir + "logs"
    if logPath == "":
        if not os.path.exists(logDirPath):
            os.makedirs(logDirPath)
            
        numberOfRuns = len(os.listdir(logDirPath))
        os.makedirs(logDirPath + delimiter + str(numberOfRuns + 1))
        logPath = logDirPath + delimiter + str(numberOfRuns + 1) + delimiter
        
        
    nameOnly = TN.split(".")[0]
    logging.basicConfig(filename=logPath + nameOnly + ".txt", level=logging.DEBUG)
    logging.info(tag + ": " + msg)
    
def getDelimiter():
    if platform.system().find("Window") != -1:
        return "\\"
    else:
        return "/"