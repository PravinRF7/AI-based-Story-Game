# **AI-Powered Visual Novel Game **
The AI-Based Story Game is an interactive storytelling web application where users create their own adventure by entering prompts. The AI generates dynamic text-based narratives and real-time AI-generated images to visualize each scene. Powered by GPT-2 for text generation and Stable Diffusion for image creation, this immersive experience lets users shape their journey step by step. The game runs on a Flask backend and a React frontend, seamlessly integrated with Docker for easy deployment. Whether you seek mystery, fantasy, or sci-fi, the AI adapts to your imagination, making each playthrough unique! 🚀📖🎭

#**Setup & Execution Guide**
## ** Prerequisites**
Ensure you have the following installed:
- **Python 3.10+**
- **Node.js (v16+)**
- **pip & npm**
- **CUDA 11+ (For GPU Acceleration, Optional)**

### **1️ Install Required Dependencies**
```bash
pip install -r requirements.txt
npm install
```

### **2️ Setup Virtual Environment (Recommended)**
```bash
python -m venv game_env
source game_env/bin/activate  # Linux/Mac
./game_env/Scripts/activate  # Windows
```

### **3️ Install & Configure AI Models**
#### ** Install Transformers & Dependencies**
```bash
pip install torch torchvision torchaudio transformers diffusers bitsandbytes flask flask-cors
```

```

### **4️Run the Flask Backend**
```bash
python app.py
```
✔ The backend should now be running at **`http://127.0.0.1:5000/`**.

### **5️ Start the React Frontend**
```bash
npm start
```
✔ The frontend should be available at **`http://localhost:3000/`**.

---

## **How to Use the Game**
1. Open **`http://localhost:3000/`** in your browser.
2. Enter an opening story prompt.
3. AI generates a **story and an image** dynamically.
4. Continue playing by providing **new inputs**.

---


