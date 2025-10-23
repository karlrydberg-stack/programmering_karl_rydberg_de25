from numbers import Number

def validate(value):
    
    if not isinstance(value, Number):
        raise TypeError(f"Elements must be numbers not {type(value)}")