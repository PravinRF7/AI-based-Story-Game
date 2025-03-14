from flask import Flask, request, jsonify, send_from_directory
import os
import time
from flask_cors import CORS
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from diffusers import StableDiffusionPipeline

app = Flask(__name__, static_url_path='/static')
CORS(app, resources={r"/*": {"origins": "*"}})  # Allow frontend access

# ✅ Ensure "static/images/" directory exists
os.makedirs("static/images", exist_ok=True)

# ✅ Initialize AI Models
print("Loading AI Models...")

# ✅ Use GPT-2 for lightweight text generation
model_name = "gpt2"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32)
text_generator = pipeline("text-generation", model=model, tokenizer=tokenizer, device=0 if torch.cuda.is_available() else -1)

# ✅ Load Image Generation Model with Optimized VRAM Usage
try:
    image_model = StableDiffusionPipeline.from_pretrained(
        "runwayml/stable-diffusion-v1-5", safety_checker=None
    )
    image_model.to("cuda" if torch.cuda.is_available() else "cpu")
except Exception as e:
    print("❌ Image model failed to load:", str(e))
    image_model = None  # Disable image generation if the model fails

@app.route("/")
def home():
    return jsonify({"message": "Flask backend is running!"})

# ✅ Generate AI-powered story text
@app.route("/generate_text", methods=["POST"])
def generate_text():
    data = request.json
    user_input = data.get("user_input", "")

    prompt = f"{user_input}"
    output = text_generator(prompt, max_length=150, num_return_sequences=1)

    return jsonify({"story": output[0]["generated_text"]})

# ✅ Generate AI-powered image
@app.route("/generate_image", methods=["POST"])
def generate_image():
    if image_model is None:
        return jsonify({"error": "Image generation is disabled due to model loading failure."}), 500

    data = request.json
    prompt = data.get("prompt", "")

    try:
        timestamp = int(time.time())
        image_filename = f"generated_{timestamp}.png"
        image_path = os.path.join("static/images", image_filename)

        # ✅ Generate Image
        image = image_model(prompt).images[0]
        image.save(image_path)

        return jsonify({"image_url": f"/static/images/{image_filename}"})

    except IndexError:
        return jsonify({"error": "Image generation failed. Try a different prompt."}), 500

# ✅ Route to Serve Images Manually (Ensures Flask serves static files correctly)
@app.route('/static/images/<path:filename>')
def serve_image(filename):
    return send_from_directory("static/images", filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
