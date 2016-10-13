import json
from collections import namedtuple

class dict2obj(object):

    def __init__(self, d):
        self.__dict__['d'] = d

    def __getattr__(self, key):
        value = self.__dict__['d'][key]
        if type(value) == type({}):
            return dict2obj(value)

        return value

    def __setattr__(self, key, value):
        self.__dict__['d'][key] = value

    def update(self, d):
        for key in d:
            self.__dict__['d'][key] = d[key]


def getJsonFromFile(jsonFile):
	jsonData = None
	with open(jsonFile) as fileData:
		jsonData = dict2obj(json.load(fileData))

	return jsonData
