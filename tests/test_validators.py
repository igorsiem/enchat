from enchat.validators import FloatRange, IntegerRange, validate_using

def test_float_range():
    # Simple range checks
    float_range = FloatRange(error_message="", allow_empty=False, min=1.0, max=2.0)
    assert float_range.is_valid(1)
    assert float_range.is_valid(1.5)
    assert float_range.is_valid(2)
    assert float_range.is_valid(0) is False
    assert float_range.is_valid(3) is False

    # Just a minimum
    float_range = FloatRange(error_message="", allow_empty=False, min=1.0)
    assert float_range.is_valid(1)
    assert float_range.is_valid(1.5)
    assert float_range.is_valid(2)
    assert float_range.is_valid(0) is False
    assert float_range.is_valid(3)

    # Just a maximum
    float_range = FloatRange(error_message="", allow_empty=False, max=2.0)
    assert float_range.is_valid(1)
    assert float_range.is_valid(1.5)
    assert float_range.is_valid(2)
    assert float_range.is_valid(0)
    assert float_range.is_valid(3) is False

