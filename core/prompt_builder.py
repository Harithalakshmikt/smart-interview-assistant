def build_feedback_prompt(answer):
    return f"""Rate the following answer based on clarity, relevance, and confidence.

Examples:
Q: I used a dictionary to store key-value pairs.
A: Clear and relevant. Shows basic understanding of Python.

Q: I used recursion to solve the problem.
A: Good use of recursion. Could mention time complexity.

Q: {answer}
A:"""

def build_behavioral_prompt(answer):
    return f"""Evaluate this behavioral response for professionalism, empathy, and problem-solving.

Examples:
Q: I resolved a team conflict by listening to both sides.
A: Thoughtful and diplomatic. Shows emotional intelligence and leadership.

Q: I handled a missed deadline by blaming my teammate.
A: Poor accountability. Lacks professionalism.

Q: {answer}
A:"""

def build_resume_question_prompt(context, query):
    return f"""Based on the following resume:\n{context}\n\nAnswer this: {query}"""
