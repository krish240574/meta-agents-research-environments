def some_function(some_string):
    # Safely handle NoneType by checking before using strip
    if some_string is None:
        return ""
    if isinstance(some_string, str):
        return some_string.strip()
    return ""