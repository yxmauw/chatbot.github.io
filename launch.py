import gradio as gr
from gpt4all import GPT4All

model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf")

def generate_text(input_text):
    output = model.generate(input_text, max_tokens=50)
    generated_text = output["text"]
    return generated_text

input_text = gr.Textbox(lines=5, label="Input Text")
output_text = gr.Textbox(lines=5, label="Generated Text")

gr.Interface(fn=generate_text, inputs=input_text, outputs=output_text, title="GPT4All_experiment").launch()
