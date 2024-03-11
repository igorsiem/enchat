from toga.validators import BooleanValidator

class FloatRange(BooleanValidator):
    """Validator for a floating point range

    This validator checks that the input is between a given range when converted to a floating point. It does *not* check that the input
    is numeric (use the `Number` validator).

    TODO Tests for the FloatRange validator class
    """

    def __init__(self, error_message : str, allow_empty : bool = True, min : float = None, max : float = None):

        if min is not None and max is not None:
            assert(float(min) < float(max))

        self._min = float(min) if min is not None else None
        self._max = float(max) if max is not None else None
            
        super(FloatRange, self).__init__(error_message, allow_empty)

    def is_valid(self, input_string : str) -> bool:
        v = float(input_string)
        if self._min is not None and v < self._min:
            return False
            
        if self._max is not None and v > self._max:
            return False
            
        return True

class IntegerRange(BooleanValidator):
    """Validator for an integer range

    This validator checks that the input is between a given range when converted to a floating point. It does *not* check that the input
    is numeric (use the `Number` validator), but it *does* check that - if a numeric - it's an integer.

    TODO Tests for the IntegerRange validator class
    """

    def __init__(self, error_message : str, allow_empty : bool = True, min : int = None, max : int = None):

        if min is not None and max is not None:
            assert(int(min) < int(max))

        self._min = int(min) if min is not None else None            
        self._max = int(max) if max is not None else None
            
        super(IntegerRange, self).__init__(error_message, allow_empty)
        
    def is_valid(self, input_string : str) -> bool:
        try:
            v = int(input_string)
        except ValueError:
            return False        

        if self._min is not None and v < self._min:
            return False
            
        if self._max is not None and v > self._max:
            return False
            
        return True

def validate_using(value, *args):
    """Validate a value against one or more BooleanValidator objects

    Args:
        value (_type_): The value to check
        *args: One or more validator objects

    Raises:
        RuntimeError: _description_
        RuntimeError: _description_

    Returns:
        _type_: _description_
    """
    validators = list(args)

    if len(validators) < 1:
        raise RuntimeError("the `validate_using` function needs at least one BooleanValidator")
    
    if any(isinstance(v, BooleanValidator) is False for v in validators):
        raise RuntimeError("`validate_using` was called with one or more objects that are not BooleanValidator objects")
    
    return all(v.is_valid(value) for v in validators)
