# Text Summarizer Application

## Overview
This is a Flask web application that summarizes text from uploaded .txt files using the Groq API. The application features a modern, responsive interface that displays both the original and summarized text side by side.

## Core Functionalities
* Upload .txt files with validation
* Real-time text summarization using Groq API
* Side-by-side display of original and summarized text
* Error handling for invalid file types and API failures
* Responsive web interface with modern design
* Welcome page with feature highlights
* File upload page with drag-and-drop support

## Technical Stack
* Programming Language: Python 3.8+
* Web Framework: Flask
* Frontend: HTML5, CSS3, JavaScript
* API: Groq
* Version Control: Git and GitHub
* IDE: Cursor AI

## Project Structure
```
project/
├── app.py
├── templates/
│   ├── index.html
│   └── upload.html
├── static/
│   ├── css/
│   └── js/
├── uploads/
├── requirements.txt
├── .env
└── README.md
```

## Setup Instructions
1. Clone the repository:
```bash
git clone <repository-url>
cd <project-directory>
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
   - Create a `.env` file in the root directory
   - Add your Groq API key:
   ```
   GROQ_API_KEY=your_api_key_here
   ```

5. Run the application:
```bash
python3 app.py
```

## API Integration
* The application uses Groq API for text summarization
* API key is securely stored in environment variables
* Rate limiting and error handling implemented for API calls
* Configurable summarization parameters

## Security Considerations
* File upload validation for .txt files only
* API key protection through environment variables
* Input sanitization
* Error handling for invalid inputs
* Secure file handling

## User Interface
* Welcome page with feature highlights
* Upload page with drag-and-drop support
* Side-by-side display of original and summarized text
* Responsive design for all devices
* Clear error and success messages
* Modern, clean aesthetic

## Future Enhancements
* Support for multiple file formats (PDF, DOCX, etc.)
* Customizable summary length
* User authentication and account management
* Save and load previous summaries
* Multiple language support
* Batch file processing
* Export summaries to different formats

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License
MIT License


