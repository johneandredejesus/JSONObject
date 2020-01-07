# JSONObject usage:
```
class Position(JSONObject): #example class
    def __init__(self):
        super().__init__()#optional
        self.__index = -1
        self.__positionx = 0
        self.__positiony = 0
        
    @property
    def index(self):
        return self.__index
    @index.setter
    def index(self, value):
        self.__index = value
    @property
    def positionx(self):
        return self.__positionx
    @positionx.setter
    def positionx(self, value):
        self.__positionx = value
    @property
    def positiony(self):
        return self.__positiony
    @positiony.setter
    def positiony(self, value):
        self.__positiony = value
 
        
class Control(JSONObject):#example class
    def __init__(self):
        super().__init__()#optional
        self.__index = -1
        self.__identify = ""
        self.__controls = []
        self.__position =  Position()
       
    @property
    def index(self):
        return self.__index
    @index.setter
    def index(self, value):
        self.__index = value
    @property
    def identify(self):
        return self.__identify
    @identify.setter
    def identify(self, value):
        self.__identify = value
    @property
    def controls(self):
        return self.__controls
    @controls.setter
    def controls(self, value):
        self.__controls = value
    @property
    def position(self):
        return self.__position
    @position.setter
    def position(self, value):
        self.__position = value
    

json = '{"controls":[{"identify":"Test","index":-12,"position":{"positionx":1000,"positiony":789,"index":-1}}],"identify":"Test2","index":891,"position":{"positionx":182,"positiony": 112,"index":-132}}'

control = Control()
control.identify = "Control0"
control.index = 100
control.position.positionx = 9

position = Position()
position.positionx = 1222
position.positiony = 44
control.controls.append(position)

position2 = Position()
position2.positionx = 3000
position2.positiony = 5000
control.controls.append(position2)

position3 = Position()
position3.positionx = 6000
position3.positiony = 7000
control.controls.append(position3)


convert  = JSON()
#Build object
obj = convert.converttoobject(json)
print(obj.identify)
print(obj.position.positionx)
#Build JSON
json = convert.converttojson(control)
print(json)
