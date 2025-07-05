# ----------------------------------
# 6. gradio_ui.py (optional frontend)
# ----------------------------------
import gradio as gr
import os

with gr.Blocks(theme=gr.themes.Base(), css="""
body { background-color: black; color: rgb(8, 166, 212); }
.gr-textbox textarea::selection {
    background-color: rgb(8, 166, 212);
    color: white;
}
""") as demo:
    gr.Markdown("""# 🧠 Friday AI Assistant""", elem_id="title")
    chat = gr.Textbox(label="Type your command to Friday")
    out = gr.Textbox(label="Friday's Response")

    def fake_friday_response(txt):
        return f"You said: {txt} (Friday would process this via voice in production)"

    chat.submit(fn=fake_friday_response, inputs=chat, outputs=out)

if __name__ == "__main__":
    demo.launch()