def some_function(some_string):
    # Ensure input is not None and is a string before calling strip
    if some_string is None:
        return ""
    return (some_string.strip() if isinstance(some_string, str) else "")