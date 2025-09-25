from search_engine import search_web
from chunker import chunk_and_clean
from prompt_builder import build_prompt
from llm_api import call_llm_api

def get_interview_answer(user_query):
    snippets = search_web(user_query)
    chunks = chunk_and_clean(snippets)
    prompt = build_prompt(chunks, user_query)
    return call_llm_api(prompt)
