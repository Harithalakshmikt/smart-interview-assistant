def build_prompt(chunks, user_query):
    context = "\n".join(chunks)
    return f"""You are an interview assistant. Based on the following context:
{context}
Answer this query: {user_query}
"""
