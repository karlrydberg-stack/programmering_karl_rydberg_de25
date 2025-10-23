from numbers import Number
def validate_positive(new_value):
        if not isinstance(new_value, Number):
            raise ValueError("Only numbers")
        else:
            if new_value < 0:
                raise ValueError("Number can not be negative")