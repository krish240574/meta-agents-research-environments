def safe_strip(value):
    # FIX: Ensure value is a string before calling strip()
    if value is None:
        return ''
    if isinstance(value, str):
        return value.strip()
    raise TypeError('Expected a string or None, got {}'.format(type(value).__name__))