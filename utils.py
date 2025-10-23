def safe_strip(value):
    # FIX: Ensure value is not None before calling strip()
    if value is None:
        return ''
    return value.strip() if isinstance(value, str) else value