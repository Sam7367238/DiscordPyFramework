import json

from dotenv import load_dotenv

config = {}

def initialize(configFilePath):
  load_dotenv()
  global config

  with open(configFilePath, "r") as configFile:
    config = json.load(configFile)

def getConfig(key):
  return config[key]