# Data classes are just regular classes that are geared towards storing state, rather than containing a lot of logic.
# Every time you create a class that mostly consists of attributes, you make a data clas

from dataclasses import dataclass, field
# data classes is merely classes used to hold data.
# simply like model classes

# problems with attributes in classes:
# 1. too much arguments
# 2. ugly init() [i.e initializing attributes inside init ]
# 3. can properly define datatype of properties.

# note: we can use properties with dataclasses.


# using normal classes
class Vehicle:
    def __init__(self, wheels: int):
        self.wheels = wheels


# using data classes
@dataclass
class Vehicle:
    wheels: int=0
# note: dataclasses automatically created init method for us.

# nested dataclass
from typing import List, Any

@dataclass
class PlayingCard:
    rank: str
    suit: str

@dataclass
class Deck:
    cards: List[PlayingCard]

queen_of_hearts = PlayingCard('Q', 'Hearts')
ace_of_spades = PlayingCard('A', 'Spades')
two_cards = Deck([queen_of_hearts, ace_of_spades])

# inheritance

@dataclass
class Position:
    name: str
    lon: float
    lat: float

@dataclass
class Capital(Position):
    country: str

Capital('Oslo', 10.8, 59.9, 'Norway')


# @dataclass(frozen=True) will create immutable data classes.
# @dataclass(order=True) will add __gt__ , __ge__, __lt__, __le__ to this class,
# to compare different objects of this class.

# @dataclass(eq=True) will generate __eq__ method. by default eq method generated.
# __post_init__ -> The generated __init__ method calls the __post_init__ method before returning.


# field()
# we can customize each attribute using field()
# field function arguments: [note: all these argument take true/false as value except default and default_factory]
# 1. default -> to set some constant default value
# 2. default_factory -> it will use to set some dynamic value of the field as default value,
# (here we have to pass some function reference),
#  like this  ` marks: List[int] = field(default_factory = get_random_marks)`
# 3.init -> if we want to omit some field from initialization then we set init=false.
# 4.repr -> if we want to omit some field from object representation then we set repr=False).
# 5. compare -> used to add or remove attribute compare functions.

# note: @dataclass(order=True) by default provide dictionary like comparison, that first it compares first attribute,
# if different then return comparison result else compare next attribute and so on. we can override __gt__, __ge__, etc
# methods for custom comparison and sorting.
# also, there s one more default behaviour of data-classes is that, the variable that is specified in the __post_init__
# method will be used for data-class ordering, so using this behaviour we can avoid to override all
# __gt__, __ge__, etc methods
# example:
@dataclass(order=True)
class RGBClass:
    sort_index: int = field(init=False, repr=False)
    # this sort_index is just used to order this data-class, we will calculate this new field,
    # that's why we don't want to init and repr it
    red: int
    green: int
    blue: int

    # we usually avoid to override init methods in dataclasses, otherwise  it will destroy the sole purpose
    # of dataclasses. so to perform operations we do in init method we have post_init method in data-classes.
    def __post_init__(self):
        # due to default behaviour of post_init, sort_index will be used for ordering
        self.sort_index = self.red + self.blue + self.green

print(RGBClass(red=255,green=255,blue=255)>RGBClass(0,0,0))
z = sorted([RGBClass(red=255,green=255,blue=255),RGBClass(0,0,0),RGBClass(10,20,30)])
print(z)

# note dataclasses are not made for doing data validation, but if still you want we can abuse post_init method, but it
# is not pythonic, so for that we use other third-party libs cerebrus or pydantic.
# example of data-classes with cerebrus:
# https://medium.com/avmconsulting-blog/validating-python-data-with-cerberus-374447bd3cbe

# also I have projet in my local to get started with cerebrus.
