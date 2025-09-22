import gradio as gr
from core.model_loader import load_llm, load_embedding_model
from core.resume_parser import extract_text_from_file
from core.vector_store import build_faiss_index, retrieve_context
from core.prompt_builder import build_feedback_prompt
from core.assistant_logic import generate_response

# Load models
llm = load_llm()
embedding_model = load_embedding_model()
db = None  # FAISS index

# Handle resume upload
def handle_resume(file):
    global db
    try:
        text = extract_text_from_file(file)
        db = build_faiss_index(text, embedding_model)
        return "✅ Resume uploaded and indexed successfully!"
    except Exception as e:
        return f"❌ Error: {str(e)}"

# Handle query with RAG
def handle_query(query):
    if db is None:
        return "Please upload your resume first."
    context = retrieve_context(db, query)
    return generate_response(llm, query, context)

# Handle feedback scoring
def handle_feedback(answer):
    prompt = build_feedback_prompt(answer)
    return generate_response(llm, prompt)

# Gradio Blocks UI
with gr.Blocks() as demo:
    gr.Markdown("## 🧠 Smart Interview Assistant with Resume Upload + Feedback Scoring")

    with gr.Tab("Resume-Based Q&A"):
        resume_file = gr.File(label="Upload your resume (.txt or .pdf)")
        upload_btn = gr.Button("Upload and Index")
        upload_status = gr.Textbox(label="Status")

        query_input = gr.Textbox(lines=4, placeholder="Ask a question based on your resume...")
        query_btn = gr.Button("Ask")
        query_output = gr.Textbox(label="Response")

        upload_btn.click(handle_resume, inputs=resume_file, outputs=upload_status)
        query_btn.click(handle_query, inputs=query_input, outputs=query_output)

    with gr.Tab("Answer Feedback"):
        answer_input = gr.Textbox(lines=4, placeholder="Paste your interview answer here...")
        feedback_btn = gr.Button("Get Feedback")
        feedback_output = gr.Textbox(label="Feedback")

        feedback_btn.click(handle_feedback, inputs=answer_input, outputs=feedback_output)
