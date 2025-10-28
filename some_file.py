def some_function(some_string):
    # Validate input and handle NoneType correctly
    if isinstance(some_string, str):
        return some_string.strip()
    return ""