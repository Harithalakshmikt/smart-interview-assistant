import gradio as gr
from assistant_logic import get_interview_answer

demo = gr.Interface(
    fn=get_interview_answer,
    inputs=gr.Textbox(lines=2, label="Ask your interview question"),
    outputs="text",
    title="🧠 Smart Interview Assistant",
    description="Ask for interview questions, answers, or explanations. Powered by RAG + LLM API."
)

demo.launch()
