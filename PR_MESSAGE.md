Title: Fix: JSON executor normalizes schema-like inputs; clarify tool descriptions and JSON rules to prevent dict passed for string

Summary
- Tools expecting simple types (e.g., content: string) fail when the LLM copies the tool schema into the action_input and passes a dict ({"type":"string","description":"..."}) instead of a literal.
- At runtime, strict type checking enforces content: str, causing TypeError when a dict is passed.
- This PR:
  - Normalizes common schema-like values in the JSON executor into literals before tool invocation.
  - Clarifies tool descriptions to show name:type pairs rather than raw dict schemas.
  - Adds an explicit JSON rule informing the model to pass literal values, not schema objects.

User-Facing Impact
- Prevents failures like “Argument 'content' must be of type <class 'str'>, got <class 'dict'>” when using AgentUserInterface__send_message_to_user with content.
- Improves model behavior by making tool usage examples and rules unambiguous.

Reproduction
- Command: are-run -s identify_consolidation_opportunity -a default --kwargs '{"db_connection_string": "postgresql://postgres:password@localhost:5432/spend_analytics"}' --provider openai --model gpt-4o-mini
- Tool call produced:
  - action: "AgentUserInterface__send_message_to_user"
  - action_input: {"content": {"description": "…message…", "type": "string"}}
- Error:
  - TypeError: Argument 'content' must be of type <class 'str'>, got <class 'dict'>

Root Cause
- Tool descriptions embed the full input schema dict in “Takes inputs”, which the LLM sometimes copies directly into action_input.
- The JSON executor forwards arguments as-is, and type checks fire when the dict reaches the tool.

Changes
- Argument normalization in JSON executor
  - are/simulation/agents/default_agent/tools/json_action_executor.py: normalize common schema-like dicts (e.g., {"type": "string", "description": "..."}) into the literal description string before tool invocation.
- Clarify tool descriptions to avoid prompting schema copying
  - are/simulation/tool_box.py: change DEFAULT_TOOL_DESCRIPTION_TEMPLATE to list inputs as name: type pairs and add a note to pass literal values.
- Tighten JSON usage rules in system prompt
  - are/simulation/agents/default_agent/prompts/system_prompt.py: add an explicit "no schema-like objects" rule under ACTION RULES with an example.

Why this approach
- Keeps strict runtime type checking intact and tool APIs unchanged.
- Fixes the class of errors at the executor boundary with a minimal, safe normalization.
- Reduces future occurrences by making prompts and descriptions model-friendly and less misleading.

Backward Compatibility
- Safe and additive:
  - Executor normalization only affects malformed schema-like inputs; valid calls are untouched.
  - Tool description formatting is user-facing text and does not change runtime behavior.
  - Prompt update improves clarity without altering agent interfaces.

Alternatives considered
- Loosening AgentUserInterface.send_message_to_user to accept Any and coerce. Rejected to preserve strict API types and avoid hiding other mistakes.
- Wider normalization (e.g., number parsing) now out of scope; can be added if similar issues surface.

Tests/Validation
- Manual validation attempt was blocked under a read-only sandbox due to missing temp dir, but behavior is straightforward: if content is a dict with {"type":"string","description":"…"}, it now gets normalized to the literal string before tool invocation.
- Suggested follow-up: unit test JsonActionExecutor.execute_tool_call to confirm {"content": {"type":"string","description":"hi"}} invokes tool with content="hi".

Related observation (separate issue)
- In a sample scenario, PlanningApp__generate_negotiation_strategy failed earlier with ValueError: Unknown format code 'f' for object of type 'str' when given a string for a numeric field. That is scenario code; consider coercion/validation there in a separate PR.

Changed files
- are/simulation/agents/default_agent/tools/json_action_executor.py
- are/simulation/tool_box.py
- are/simulation/agents/default_agent/prompts/system_prompt.py

