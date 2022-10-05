def assert_equals(actual, expected, message = None):
    if (message == None):
        message = f"Expected value {expected} but obtained {actual}"
    assert actual == expected, message

def assert_not_equals(actual, unexpected, message = None):
    if (message == None):
        message = f"Unexpected value {unexpected}"
    assert actual == unexpected, message

def expect_error(message, thunk):
    return