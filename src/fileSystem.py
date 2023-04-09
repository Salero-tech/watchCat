import yaml
import os
import shutil
import subprocess

WORKDIRPATH = "/home/watchcat/"
CONFIG_FILE_PATH = WORKDIRPATH + 'config/config.yml'
TEMPLATE_FOLDER_PATH = WORKDIRPATH + "config/templates/"

CONFIG_FILE_PATH_DEFAULT = WORKDIRPATH + 'defaultConfig/config.yml'
TEMPLATE_FOLDER_PATH_DEFAULT = WORKDIRPATH + "defaultConfig/templates/"

def init ():
    #if files not exists create them
    if FileNotExists(CONFIG_FILE_PATH):
        _createConfigFile()

    if FileNotExists(TEMPLATE_FOLDER_PATH):
        _createTemplates()

    subprocess.run(["chown", "-R", "watchcat", WORKDIRPATH + "config/"])

def _createConfigFile ():
    shutil.copy2(CONFIG_FILE_PATH_DEFAULT, CONFIG_FILE_PATH)

def _createTemplates ():
    shutil.copytree(TEMPLATE_FOLDER_PATH_DEFAULT, TEMPLATE_FOLDER_PATH)

def FileNotExists (path) -> bool:
    if not os.path.exists(path):
        return True
    return False

def loadConfigFile ():
    #check if config file exists
    if FileNotExists(CONFIG_FILE_PATH):
        exit("config file not found")

    #load yml config
    file = open(CONFIG_FILE_PATH, "r")
    configStr = yaml.safe_load(file)
    file.close()

    return configStr

def loadTemplate (templatePath):
    #check if config file exists
    if FileNotExists(TEMPLATE_FOLDER_PATH + templatePath):
        exit(f"template file {TEMPLATE_FOLDER_PATH + templatePath} not found")

    file = open(TEMPLATE_FOLDER_PATH + templatePath, "r")
    templateYml = yaml.safe_load(file)
    file.close()
    return templateYml