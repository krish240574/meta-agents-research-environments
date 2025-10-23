def safe_strip(value: Optional[str]) -> str:
    # FIX: Handle NoneType to avoid AttributeError
    if value is None:
        return ''
    return value.strip()