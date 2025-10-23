def safe_strip(value):
    # FIX: Add additional checks to ensure value is safely handled
    if value is None:
        return ''
    if isinstance(value, str):
        return value.strip()
    raise TypeError(f'Expected a string or None, got {type(value).__name__}')