## Overview 
This is a Flask web app that summarizes text from uploaded .txt files using Groq API. It displays both original and summarized text on the webpage.

## Core Functionalities
* Upload .txt file
* Summarize text with Groq 
* Display original and summarized text
* Error handling for invalid file types
* Responsive web interface

## Technical Stack 
* Programming Language: Python 3.8+
* Web framework: Flask
* Frontend: HTML, CSS, JavaScript
* API: Groq
* Version Control: Git and Github
* IDE: Cursor AI

## Project Structure
```
project/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── static/
│   │   ├── css/
│   │   └── js/
│   └── templates/
│       └── index.html
├── config.py
├── requirements.txt
├── .env
├── .gitignore
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
flask run
```

## API Integration
* The application uses Groq API for text summarization
* API key must be securely stored in environment variables
* Rate limiting and error handling implemented for API calls

## Security Considerations
* File upload validation
* API key protection
* Input sanitization
* Error handling for invalid inputs

## Future Enhancements
* Support for multiple file formats
* Customizable summary length
* User authentication
* Save and load previous summaries
* Multiple language support

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License
MIT License


