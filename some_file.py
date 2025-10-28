def some_function(some_string):
    # Handle NoneType and ensure some_string is a string before calling strip
    if not isinstance(some_string, str):
        return ""
    return some_string.strip()