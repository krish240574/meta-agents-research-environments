def safe_strip(value):
    return value.strip() if isinstance(value, str) else ''  # FIX: Handle NoneType