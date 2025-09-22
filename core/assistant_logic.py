from core.prompt_builder import build_feedback_prompt

prompt = build_feedback_prompt(user_input)
response = llm(prompt, max_length=300)[0]["generated_text"]
