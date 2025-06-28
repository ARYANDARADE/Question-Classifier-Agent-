Question Prism - Question Classifier 📚
A powerful Streamlit application that automatically classifies questions into predefined categories using AI agents and provides comprehensive explanations through web search. The app supports text input, image OCR, and batch processing via Excel files.

Features ✨
Question Classification: Automatically categorizes questions into 8 different types
OCR Support: Extract and classify questions from images
Batch Processing: Upload Excel files for bulk question classification
Web Search Integration: Uses DuckDuckGo and Tavily for comprehensive answers
Streaming Responses: Real-time response display with typing animation
Multi-language OCR: Supports English and Hindi text extraction

Question Categories 📝
The system classifies questions into these categories:

Mathematical - Calculations, equations, derivatives, integrals
Definition - Definitions, theory, explanations, conceptual meaning
Formulation - Deriving or expressing formulas, using principles
Inferential - Inference, interpretation, logical deduction
Differentiation - Compare or classify two or more items
Analytical - Sequences, logic puzzles, arithmetic, patterns
Statistical - Averages, charts, probability, standard deviation
Inference - Drawing conclusions from given information

Prerequisites 🔧
Python 3.8 or higher
OpenAI API key
Tavily API key 

Installation 🚀
Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies
pip install -r requirements.txt
Set up environment variables
Create a .env file in the root directory:

OPENAI_API_KEY=your_openai_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
API Keys Setup 🔑
OpenAI API Key
Visit OpenAI Platform
Create an account or log in
Navigate to API Keys section
Create a new API key
Copy the key to your .env file
Tavily API Key
Visit Tavily
Sign up for an account
Get your API key from the dashboard
Add it to your .env file

Usage 💻
Start the application
streamlit run main.py
Access the app Open your browser and go to http://localhost:8501

How to Use 📖
Text Input
Enter your question in the text input field
Click "Classify Question"
View the classification and explanation
Image Upload
Click "Upload an Image" in the sidebar
Select an image file (JPG, JPEG, PNG)
The app will extract text using OCR and classify it
View the extracted text and classification results
Excel Batch Processing
Click "Upload Excel File" in the sidebar
Upload an Excel file (.xlsx) with questions
The file should have a 'question' column or questions in the first column
View the batch classification results in a table

Project Structure 📁
question-classifier/
├── main.py                 # Streamlit app main file
├── requirements.txt        # Python dependencies
├── .env                   # Environment variables (create this)
├── tools/
│   ├── ocr.py            # OCR functionality using EasyOCR
│   ├── tools.py          # Agent definitions and orchestrator
│   └── prompts.py        # Prompt templates for classification
└── utils/
    └── config.py         # Configuration utilities

Dependencies 📦
streamlit: Web app framework
agno: AI agent framework
easyocr: Optical Character Recognition
pandas: Data manipulation for Excel processing
groq: Alternative LLM provider
python-dotenv: Environment variable management
duckduckgo-search: Web search functionality
tavily-python: Advanced web search API


Configuration ⚙
The application uses multiple AI agents:
Classifier Agent: Categorizes questions using GPT-4
DuckDuckGo Searcher: Performs web searches using DuckDuckGo
Tavily Searcher: Performs advanced web searches using Tavily API
Orchestrator: Coordinates all agents for comprehensive responses

Troubleshooting 🔧
Common Issues
OCR not working
Ensure the image contains clear, readable text
Check if EasyOCR downloaded the required models
API errors
Verify your API keys are correct in the .env file
Check your API usage limits
Excel upload issues
Ensure your Excel file has a 'question' column
Check that the file is in .xlsx format
Installation problems

Try upgrading pip: pip install --upgrade pip
Use specific package versions if conflicts occur
Performance Tips
For better OCR results, use high-quality, well-lit images
Keep questions clear and concise for better classification
Large Excel files may take longer to process

License 📄
This project is licensed under the MIT License - see the LICENSE file for details.

Contributing 🤝
Fork the repository
Create a feature branch
Make your changes
Submit a pull request
Support 💬
For issues and questions:

Check the troubleshooting section above
Create an issue in the repository
Ensure you have the latest versions of all dependencies

Acknowledgments 🙏
OpenAI for GPT-4 API
Tavily for web search capabilities
EasyOCR for optical character recognition
Streamlit for the web framework
