from stack_queue_brackets.stack_queue_brackets import validate_brackets


def test_one_pair():
    # Actual
    actual = validate_brackets("{}")
    # Expected
    expected = True
    # Assert
    assert actual == expected


def test_three_pair():
    # Actual
    actual = validate_brackets("{}()[]")
    # Expected
    expected = True
    # Assert
    assert actual == expected


def test_extra_pair():
    # Actual
    actual = validate_brackets("()[[Extra Characters]]")
    # Expected
    expected = True
    # Assert
    assert actual == expected


def test_multiple_pair():
    # Actual
    actual = validate_brackets("(){}[[]]")
    # Expected
    expected = True
    # Assert
    assert actual == expected


def test_string_pair():
    # Actual
    actual = validate_brackets("{}{Code}[Fellows](())")
    # Expected
    expected = True
    # Assert
    assert actual == expected


def test_missing_closing():
    # Actual
    actual = validate_brackets("[({}]")
    # Expected
    expected = False
    # Assert
    assert actual == expected


def test_missing():
    # Actual
    actual = validate_brackets("(]()")
    # Expected
    expected = False
    # Assert
    assert actual == expected


def test_missing_opening():
    # Actual
    actual = validate_brackets("{(})")
    # Expected
    expected = False
    # Assert
    assert actual == expected
