import requests 
from flask import Flask, render_template, request
import os
from dotenv import load_dotenv
from werkzeug.utils import secure_filename

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def summarize_text(text):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {os.getenv('GROQ_API_KEY')}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama3-8b-8192",
        "messages": [
            {"role": "user", "content": text}
        ],
        "temperature": 0.5
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if a file was uploaded
        if 'file' not in request.files:
            return render_template('upload.html', error='No file selected')
        
        file = request.files['file']
        
        # Check if the file is empty
        if file.filename == '':
            return render_template('upload.html', error='No file selected')
        
        # Check if the file is a text file
        if not file.filename.endswith('.txt'):
            return render_template('upload.html', error='Please upload a .txt file')
        
        try:
            # Read the file content
            text = file.read().decode('utf-8')
            
            # Generate summary
            summary = summarize_text(text)
            
            return render_template('upload.html', 
                                 original_text=text,
                                 summary=summary,
                                 success='File uploaded and summarized successfully!')
        except Exception as e:
            return render_template('upload.html', error=f'Error processing file: {str(e)}')
    
    return render_template('upload.html')

if __name__ == "__main__":
    app.run(debug=True)
    