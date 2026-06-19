def format_response(result) -> str:
    messages = result.get("messages", []) if isinstance(result, dict) else []
    if not messages:
        return "No response returned."

    final_message = messages[-1]
    content = getattr(final_message, "content", final_message)

    if isinstance(content, list):
        content = "\n".join(
            part.get("text", str(part)) if isinstance(part, dict) else str(part)
            for part in content
        )

    return f"Agent Response:\n{content}"