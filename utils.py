def safe_strip(value):
    # FIX: Return an empty string for None and handle unexpected types
    if value is None:
        return ''
    if isinstance(value, str):
        return value.strip()
    return ''