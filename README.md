# Text Summarizer

A modern web application that uses AI to summarize text from uploaded files. Built with Flask and powered by the Groq API.

![Text Summarizer Screenshot](screenshot.png)

## Features

- 📤 Upload .txt files with drag-and-drop support
- 🤖 AI-powered text summarization using Groq API
- 📱 Responsive design for all devices
- 🔄 Side-by-side display of original and summarized text
- ⚡ Real-time processing
- 🛡️ Secure file handling and API key protection

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- A Groq API key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/text-summarizer.git
cd text-summarizer
```

2. Create and activate a virtual environment:
```bash
# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory and add your Groq API key:
```
GROQ_API_KEY=your_api_key_here
```

## Usage

1. Start the application:
```bash
python3 app.py
```

2. Open your web browser and navigate to:
```
http://127.0.0.1:5000
```

3. Use the application:
   - Click "Start Summarizing" on the welcome page
   - Upload a .txt file
   - View the original text and summary side by side

## Project Structure

```
text-summarizer/
├── app.py              # Main application file
├── templates/          # HTML templates
│   ├── index.html     # Welcome page
│   └── upload.html    # Upload page
├── static/            # Static files
│   ├── css/          # Stylesheets
│   └── js/           # JavaScript files
├── uploads/           # Temporary storage for uploaded files
├── requirements.txt   # Python dependencies
├── .env              # Environment variables
└── README.md         # This file
```

## API Integration

The application uses the Groq API for text summarization. The API key is securely stored in environment variables and never exposed in the code.

## Security

- File upload validation for .txt files only
- API key protection through environment variables
- Input sanitization
- Error handling for invalid inputs
- Secure file handling

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Future Enhancements

- Support for multiple file formats (PDF, DOCX, etc.)
- Customizable summary length
- User authentication and account management
- Save and load previous summaries
- Multiple language support
- Batch file processing
- Export summaries to different formats

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/) - Web framework
- [Groq API](https://groq.com/) - AI text summarization
- [Python](https://www.python.org/) - Programming language

