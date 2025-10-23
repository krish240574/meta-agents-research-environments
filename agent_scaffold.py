def register_agent_scaffold(scaffold):
    # Existing registration logic...
    if scaffold is None:
        raise ValueError("Scaffold cannot be None")  # FIX: Prevent NoneType registration
    if not isinstance(scaffold, BaseAgentScaffold):
        raise ValueError("Invalid scaffold type, must extend BaseAgentScaffold")
    # Check if the scaffold is already registered
    if scaffold in agent_scaffolds:
        raise ValueError("Scaffold already registered")  # FIX: Prevent duplicate registration
    agent_scaffolds.append(scaffold)
    # ... (rest of the function) ...