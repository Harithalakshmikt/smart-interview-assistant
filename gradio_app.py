import gradio as gr
from transformers import pipeline

generator = pipeline("text-generation", model="google/flan-t5-base")

def interview_assistant(prompt):
    result = generator(prompt, max_length=200, do_sample=True)[0]["generated_text"]
    return result.strip()

sample_prompts = [
    "Ask me a Python question for a junior developer.",
    "Rate this answer: I used a dictionary to store key-value pairs.",
    "Give feedback on: I resolved a team conflict by listening to both sides."
]

demo = gr.Interface(
    fn=interview_assistant,
    inputs=gr.Dropdown(choices=sample_prompts, label="Choose a sample prompt or type your own"),
    outputs="text",
    title="🧠 Smart Interview Assistant",
    description="Powered by Mistral-7B. Practice interview questions or get feedback on your answers."
)

demo.launch()


