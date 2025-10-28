def some_function(some_string):
    # Ensure some_string is not None before calling strip
    if some_string is None:
        return ""
    return some_string.strip() if isinstance(some_string, str) else ""