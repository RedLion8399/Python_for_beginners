# Basic datatypes in Python

intiger = 1
float_ = 1.0
string = "Text"
boolean = True
none = None

list_ = ["Text", 1, 1.0,]
tuple_ = ("Text", 1, 1.0,)
set_ = {"Text", 1, 1.0,}
dictionary = {"string" : "Text", 
        "intiger" : 1,
        "float" : 1.0,}


# Python is staticly typed
var = 1
print(type(var))

var = "Text"
print(type(var))

var = True
print(type(var))


# Type annotations are possible but optional
text: str = "Hello, World!"
number: int = 1
floating_point_number: float = 1.0
light_on: bool = True