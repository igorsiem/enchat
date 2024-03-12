from enchat.validators import FloatRange, IntegerRange, validate_all_using

def test_float_range():
    # Simple range checks
    float_range = FloatRange(error_message="", allow_empty=False, min=1.0, max=2.0)
    assert float_range.is_valid(1) is True
    assert float_range.is_valid(1.5) is True
    assert float_range.is_valid(2) is True
    assert float_range.is_valid(0) is False
    assert float_range.is_valid(3) is False

    # Just a minimum
    float_range = FloatRange(error_message="", allow_empty=False, min=1.0)
    assert float_range.is_valid(1) is True
    assert float_range.is_valid(1.5) is True
    assert float_range.is_valid(2) is True
    assert float_range.is_valid(0) is False
    assert float_range.is_valid(3) is True

    # Just a maximum
    float_range = FloatRange(error_message="", allow_empty=False, max=2.0)
    assert float_range.is_valid(1) is True
    assert float_range.is_valid(1.5) is True
    assert float_range.is_valid(2) is True
    assert float_range.is_valid(0) is True
    assert float_range.is_valid(3) is False

def test_integer_range():
    # Simple range checks
    integer_range = IntegerRange(error_message="", allow_empty=False, min=1, max=3)
    assert integer_range.is_valid(0) is False
    assert integer_range.is_valid(1) is True
    assert integer_range.is_valid(2) is True
    assert integer_range.is_valid(3)  is True
    assert integer_range.is_valid(4)  is False

    # Just a minimum
    integer_range = IntegerRange(error_message="", allow_empty=False, min=1)
    assert integer_range.is_valid(0) is False
    assert integer_range.is_valid(1) is True
    assert integer_range.is_valid(2) is True
    assert integer_range.is_valid(3)  is True
    assert integer_range.is_valid(4)  is True

    # Just a maximum
    integer_range = IntegerRange(error_message="", allow_empty=False, max=3)
    assert integer_range.is_valid(0) is True
    assert integer_range.is_valid(1) is True
    assert integer_range.is_valid(2) is True
    assert integer_range.is_valid(3)  is True
    assert integer_range.is_valid(4)  is False

def test_validate_all_using():
    v1 = IntegerRange(error_message="", min=1, max=3)
    v2 = IntegerRange(error_message="", min=2, max=4)

    assert validate_all_using(0, v1) is False
    assert validate_all_using(1, v1) is True
    assert validate_all_using(2, v1) is True    
    assert validate_all_using(3, v1) is True    
    assert validate_all_using(4, v1) is False

    assert validate_all_using(0, v1, v2) is False
    assert validate_all_using(1, v1, v2) is False    
    assert validate_all_using(2, v1, v2) is True
    assert validate_all_using(3, v1, v2) is True        
    assert validate_all_using(4, v1, v2) is False    

    assert validate_all_using(0, [v1, v2]) is False
    assert validate_all_using(1, [v1, v2]) is False
    assert validate_all_using(2, [v1, v2]) is True
    assert validate_all_using(3, [v1, v2]) is True        
    assert validate_all_using(4, [v1, v2]) is False        