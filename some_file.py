def some_function(some_string):
    # Ensure some_string is a string; if None, return an empty string
    if some_string is None:
        return ""
    return some_string.strip() if isinstance(some_string, str) else ""