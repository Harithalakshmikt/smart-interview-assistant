import gradio as gr
from transformers import pipeline

# Load the public LLM (Gemma 2B Instruction-tuned)
generator = pipeline("text-generation", model="google/gemma-2b-it")

# Define the assistant logic
def interview_assistant(prompt):
    response = generator(prompt, max_length=200, do_sample=True)[0]["generated_text"]
    return response.strip()

# Build Gradio UI
demo = gr.Interface(
    fn=interview_assistant,
    inputs=gr.Textbox(lines=4, placeholder="Ask a technical question or paste your answer for feedback..."),
    outputs="text",
    title="🧠 Smart Interview Assistant",
    description="Powered by Gemma-2B. Ask mock interview questions or get feedback on your answers.",
    theme="default"
)

# Launch the app
if __name__ == "__main__":
    demo.launch()
