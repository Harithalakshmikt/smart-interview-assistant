def get_interview_answer(user_query):
    snippets = search_web(user_query)
    chunks = chunk_and_clean(snippets)
    prompt = build_prompt(chunks, user_query)

    print("🧠 Prompt sent to LLM:\n", prompt)  # Debug line

    response = call_llm_api(prompt)
    print("📨 Raw LLM response:\n", response)  # Debug line

    return response
