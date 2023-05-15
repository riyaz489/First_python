# python descriptors are like getter and setter in other languages.
# _get__(self, obj, type=None) : This method is called when you want to retrieve the information (var = obj.attr),
# and we can manage or decide what this attribute should return, by using this getter method.
# __set__(self, obj, value) : This method is called to set the values of an attribute (obj.attr = 'value'), and it
# will not return anything to you.
# __delete__(self, obj) : This method is called when the attribute is deleted from an object (del obj.attr)

# above are methods and below we are using decorators for creating getters and setter
# because that is cleaner way.

"""Creating a Descriptor using @property Decorator :
In this we use the power of property decorators which are a combination of property type method and Python decorators."""
# here property are created with '_' prefix.
# and to create getter and setter for any attribute we have to use @property decorator.
# @property is for getter and @attr_name.setter is for setter and @attr_name.deleter for attribute del

class Alphabet:
    def __init__(self, value):
        self._value = value

        # getting the values

    @property
    def value(self):
        print('Getting value')
        return self._value

        # setting the values

    @value.setter
    def value(self, value):
        print('Setting value to ' + value)
        self._value = value

        # deleting the values

    @value.deleter
    def value(self):
        print('Deleting value')
        del self._value

    # passing the value


x = Alphabet('Peter')
# this will call fget() method of python internally
print(x.value)
# this will call fset() method of python internally
x.value = 'Diesel'
# this will call fdel() method of python internally
del x.value

# note: properties will be inherited

# so we will follow below code for inritnace
class Number:

    def __init__(self, value):
        """Uses property setter."""
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value


class Integer(Number):

    @property
    def value(self):
        # getting parent 'value' property
        return super().value

    @value.setter
    def value(self, new_value):
        _value = int(new_value)
        # setting parent 'value' property
        super(Integer, type(self)).value.fset(self, _value)

