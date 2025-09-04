def llm_classification_prompt(query: str) -> str:
    return f"""
You are an AI routing assistant for a local-first LLM system.

Task: Given a user query, decide which language model provider to use.

Rules:
1. Always prefer "ollama" (local) if the query can be handled locally.
2. Use "openai" only if the query requires advanced reasoning or generation.
3. Return only the provider name: "ollama" or "openai".
4. Keep the response short and lowercase.
5. Do not include any explanations or additional text.
6. If unsure, default to "ollama".
7. Do not mention any other providers.
8. Answer in a single word, without quotes.

Options:
- "ollama": For general questions, simple tasks, local data processing, and privacy-sensitive queries.
- "openai": For complex reasoning, creative writing, advanced coding tasks, and when high accuracy is essential.

User query:
"{query}"

Answer:
"""
