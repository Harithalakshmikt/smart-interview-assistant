import gradio as gr
from transformers import pipeline

# Load public LLM from Hugging Face
generator = pipeline("text-generation", model="mistralai/Mistral-7B-Instruct-v0.1")

# Define assistant logic
def interview_assistant(prompt):
    result = generator(prompt, max_length=200, do_sample=True)[0]["generated_text"]
    return result.strip()

# Build Gradio UI
demo = gr.Interface(
    fn=interview_assistant,
    inputs=gr.Textbox(lines=4, placeholder="Ask a technical question or paste your answer for feedback..."),
    outputs="text",
    title="🧠 Smart Interview Assistant",
    description="Powered by Mistral-7B. Ask mock interview questions or get feedback on your answers.",
    theme="default"
)

# Launch the app
if __name__ == "__main__":
    demo.launch()
