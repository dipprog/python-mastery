# validate.py

class Validator:
    def __init__(self, name=None):
        self.name = name

    def __set_name__(self, cls, name):
        self.name = name

    @classmethod
    def check(cls, value):
        return value
    
    def __set__(self, instance, value):
        instance.__dict__[self.name] = self.check(value)
    

class Typed(Validator):
    expected_type = object
    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f'Expected {cls.expected_type}')
        return super().check(value)
    
class Integer(Typed):
    expected_type = int

class Float(Typed):
    expected_type = float

class String(Typed):
    expected_type = str


class Positive(Validator):
    @classmethod
    def check(cls, value):
        if value < 0:
            raise ValueError('Expected >= 0')
        return super().check(value)
    
class NonEmpty(Validator):
    @classmethod
    def check(cls, value):
        if len(value) == 0:
            raise ValueError('Must be non-empty')
        return super().check(value)


class PositiveInteger(Integer, Positive):
    pass

class PositiveFloat(Float, Positive):
    pass

class NonEmptyString(String, NonEmpty):
    pass

from inspect import signature

class ValidatedFunction:
    def __init__(self, func):
        self._func = func
        self._signature = signature(func)
        self._annotations = dict(func.__annotations__)
        self._retcheck = self._annotations.pop('return', None) # Return check

    def __call__(self, *args, **kwargs):

        bound = self._signature.bind(*args, **kwargs)

        for name, val in self._annotations.items():
            val.check(bound.arguments[name])
        
        result = self._func(*args, **kwargs)

        if self._retcheck:
            self._retcheck.check(result)

        return result

        
# 'signature' from 'inspect' module are used to get details about functions in a more useful form

# Signatures of functions(its name, parameters and return its type) can be bound to *args and **kwargs(passed when calling the function)

# Help performing all error checking
