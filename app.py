import gradio as gr
from transformers import pipeline
from diffusers import StableDiffusionPipeline
import torch

# Load GPT-Neo
print("Loading GPT-Neo...")
text_pipe = pipeline("text-generation", model="EleutherAI/gpt-neo-1.3B")

# Load Stable Diffusion
print("Loading Stable Diffusion...")
sd_pipe = StableDiffusionPipeline.from_pretrained(
    "CompVis/stable-diffusion-v1-4",
    torch_dtype=torch.float32
)
sd_pipe = sd_pipe.to("cpu")

def enhance_prompt(prompt):
    result = text_pipe(f"Enhance this prompt for image generation: {prompt}", max_new_tokens=50)
    return result[0]["generated_text"].split(":")[-1].strip()

def generate_image(user_prompt, enhance):
    final_prompt = enhance_prompt(user_prompt) if enhance else user_prompt
    image = sd_pipe(final_prompt).images[0]
    return image, final_prompt

with gr.Blocks() as demo:
    gr.Markdown("## 🤖 AI Image Generator (GPT-Neo + Stable Diffusion)")
    with gr.Row():
        prompt_input = gr.Textbox(label="Enter your prompt", placeholder="e.g. anime girl in cyber city")
        enhance_checkbox = gr.Checkbox(label="Use GPT-Neo to enhance prompt", value=True)
    generate_button = gr.Button("Generate")
    image_output = gr.Image()
    prompt_output = gr.Textbox(label="Final Prompt Used")

    generate_button.click(
        fn=generate_image,
        inputs=[prompt_input, enhance_checkbox],
        outputs=[image_output, prompt_output]
    )

demo.launch(server_name="0.0.0.0", server_port=7860)
