class  JSONObject(object):
    def __init__(self,value=''):
        """Builds from JSON to object."""
        if value is '':
            return
        else:
            if type(value) is str:
                value = value.replace("\"","'")
                _dict = eval(value)
                self.__dict__ = self.__convertto(_dict)
            else:
                self.__dict__ = self.__convertto(value)
    def __convertto(self,dictvalue):
        _dict = {}
        for key , value in dictvalue.items():
                _dict[key] = self.__getitem_convertto(value)
        return _dict
    def __getitem_convertto(self,value):
        if type(value) is list:
                return [self.__getitem_convertto(index) for index in value]
        elif type(value) is dict:
                return JSONObject(value)
        else:
                return value
class JSON(object):
    def converttojson(self,obj):
        """Convert to JSON and return one."""
        _dict = { }
        if issubclass(obj.__class__, JSONObject):
            for key, value in obj.__dict__.items():
                 self.__setvalue(_dict,key,value)
        else:
            self.__exception(obj)
        return str(_dict).replace("'","\"")
    def __getitem_convertfrom(self,obj):
        if type(obj) is dict:
            return obj
        elif  issubclass(obj.__class__, JSONObject):
            _dict = {}
            for key, value in obj.__dict__.items():
                self.__setvalue(_dict,key,value)
            return _dict
        elif type(obj) is list:
            return [self.__getitem_convertfrom(index) for index in obj]
        elif type(obj) is int:
            return obj
        elif type(obj) is float:
            return obj
        elif type(obj) is str:
            return obj
        else:
           self.__exception(obj)
    def __exception(self,obj):
        error = "Object " + str(obj) +" does not inherit from JSONObject."
        raise Exception(error)
    def __setvalue(self,_dict ,key, value):
        result = self.__getitem_convertfrom(value)
        if result is not None:
            _dict[self.__remove(key)] = result
    def __remove(self,value):
        if '__' in value:
            key = value.split("__")
            return key[1]
        else:
            return value
    def converttoobject(self,value):
        """Convert to Object and return one."""
        return JSONObject(value)
