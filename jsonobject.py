class  JSONObject(object):
    def __init__(self,value=''):
        """Builds from JSON to object."""
        if value is '':
            return
        if type(value) is str:
            self.__getdict(value)
        else:
            self.__dict__ = self.__convertto(value)
    def __getdict(self,value):
        value = value.replace("\"","'")
        _dict = eval(value)
        self.__dict__ = self.__convertto(_dict)
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
    def __init__(self):
        self.__colon = ':'
        self.__comma = ','
        self.__space = ' '
        self.__leftbrace = '{'
        self.__rightbrace = '}'
        self.__leftbracket ='['
        self.__rightbracket = ']'
        self.__true = 'True'
        self.__false = 'False'
        self.__null = 'null'
        self.__none = 'None'
    def __iscolon(self,value):
        return  value  ==  self.__colon
    def __iscomma(self,value):
        return value == self.__comma
    def __isleftbracket(self,value):
        return self.__leftbracket == value
    def __isrightbracket(self,value):
        return  value  ==  self.__rightbracket
    def __isrightbrace(self,value):
        return  value  ==  self.__rightbrace
    def __isleftbrace(self,value):
        return  value  ==  self.__leftbrace
    def __insert(self,value,index,key):
        return value[:index] + key + value[index:]
    def __toseparate(self,json):
        get = json
        length = len(get)
        index = 0
        while index < length:
            if self.__isrightbrace(get[index]) or self.__isrightbracket(get[index]) or self.__iscolon(get[index]):
                get = self.__insert(get,index,self.__space)
                length = len(get)
                index += 1
            if  self.__isleftbrace(get[index]) or self.__isleftbracket(get[index]) or self.__iscomma(get[index]):
                get = self.__insert(get,index+1,self.__space)
                length = len(get)
                index += 1
            index +=1
        return get
    def converttoobject(self,value):
        """Convert to Object and return one."""
        return JSONObject(self.__topython(value))
    def converttojson(self,obj):
        """Convert to JSON and return one."""
        _dict = { }
        if issubclass(obj.__class__, JSONObject):
            for key, value in obj.__dict__.items():
                self.__setvalue(_dict,key,value)
        else:
            self.__exception(obj)
        return self.__tojson(str(_dict))
    def __getitem_convertfrom(self,obj):
        if  issubclass(obj.__class__, JSONObject):
            _dict = {}
            for key, value in obj.__dict__.items():
                self.__setvalue(_dict,key,value)
            return _dict
        elif (type(obj) is list) or (type(obj) is tuple):
            return [self.__getitem_convertfrom(index) for index in obj]
        elif (type(obj) is str) or (type(obj) is int) or (type(obj) is float) or (type(obj) is bool) or (type(obj) is dict) or (obj is None):
            return obj
        else:
            self.__exception(obj)
    def __exception(self,obj):
        error = "Object " + str(obj) +" does not inherit from JSONObject."
        raise Exception(error)
    def __setvalue(self,_dict ,key, value):
        _dict[self.__remove(key)] =  self.__getitem_convertfrom(value)
    def __remove(self,value):
        if '__' in value:
            key = value.split("__")
            return key[1]
        else:
            return value
    def __gettopython(self,value,index):
        if value[index+1:index+1+len(self.__true)] == self.__true.lower():
            return value[:index+1] + value[index+1:index+1+len(self.__true)].capitalize() +  value[index+1+len(self.__true):]
        elif value[index+1:index+1+len(self.__false)] == self.__false.lower():
            return value[:index+1] + value[index+1:index+1+len(self.__false)].capitalize() +  value[index+1+len(self.__false):]
        elif value[index+1:index+1+len(self.__null)] == self.__null.lower():
            return value[:index+1] + self.__none.capitalize() +  value[index+1+len(self.__none):]
        return value
    def __topython(self, value):
        if type(value) is bytes:
            value = value.decode('utf-8')
        value = self.__toseparate(value)
        index = 0
        length = len(value)
        while(index < length):
          if self.__iscolon(value[index]):
            value = self.__gettopython(value,index)
          elif self.__isleftbracket(value[index]):
            value = self.__gettopython(value,index)
          elif self.__iscomma(value[index]):
            value = self.__gettopython(value,index)
          index+=1
        return value.replace('\"','\'')
    def __tojson(self, value):
        if type(value) is bytes:
            value = value.decode('utf-8')
        index = 0
        length = len(value)
        while(index < length):
            if self.__iscolon(value[index]):
                value = self.__gettojson(value,index)
            elif self.__isleftbracket(value[index]):
                value = self.__gettojson(value,index)
            elif self.__iscomma(value[index]):
                value = self.__gettojson(value,index)
            index+=1
        return value.replace('\'','\"')
    def __gettojson(self,value,index):
        if value[index+2:index+2+len(self.__true)] == self.__true.capitalize():
            return value[:index+2] + value[index+2:index+2+len(self.__true)].lower() +  value[index+2+len(self.__true):]
        elif value[index+2:index+2+len(self.__false)] == self.__false.capitalize():
            return  value[:index+2] + value[index+2:index+2+len(self.__false)].lower() +  value[index+2+len(self.__false):]
        elif value[index+2:index+2+len(self.__none)] == self.__none.capitalize():
            return  value[:index+2] + self.__null.lower() +  value[index+2+len(self.__none):]
        return value
