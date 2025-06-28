 # Question Prism - Question Classifier 📚

A powerful Streamlit application that automatically classifies questions into predefined categories using AI agents and provides comprehensive explanations through web search. The app supports text input, image OCR, and batch processing via Excel files.

## Features ✨

- **Question Classification**: Automatically categorizes questions into 8 different types
- **OCR Support**: Extract and classify questions from images
- **Batch Processing**: Upload Excel files for bulk question classification
- **Web Search Integration**: Uses DuckDuckGo and Tavily for comprehensive answers
- **Streaming Responses**: Real-time response display with typing animation
- **Multi-language OCR**: Supports English and Hindi text extraction

## Question Categories 📝

The system classifies questions into these categories:

1. **Mathematical** - Calculations, equations, derivatives, integrals
2. **Definition** - Definitions, theory, explanations, conceptual meaning
3. **Formulation** - Deriving or expressing formulas, using principles
4. **Inferential** - Inference, interpretation, logical deduction
5. **Differentiation** - Compare or classify two or more items
6. **Analytical** - Sequences, logic puzzles, arithmetic, patterns
7. **Statistical** - Averages, charts, probability, standard deviation
8. **Inference** - Drawing conclusions from given information

## Prerequisites 🔧

- Python 3.8 or higher
- OpenAI API key
- Tavily API key
 q
## Installation 🚀

1. **Clone the repository**
```bash
git clone https://github.com/Priteshverma123/Question-classifies-Agno-Agent.git
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**

Create a `.env` file in the root directory:
```env
OPENAI_API_KEY=your_openai_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

## API Keys Setup 🔑

### OpenAI API Key
1. Visit [OpenAI Platform](https://platform.openai.com/)
2. Create an account or log in
3. Navigate to API Keys section
4. Create a new API key
5. Copy the key to your `.env` file

### Tavily API Key
1. Visit [Tavily](https://tavily.com/)
2. Sign up for an account
3. Get your API key from the dashboard
4. Add it to your `.env` file

## Usage 💻

1. **Start the application**
```bash
streamlit run main.py
```

2. **Access the app**
Open your browser and go to `http://localhost:8501`

## How to Use 📖

### Text Input
1. Enter your question in the text input field
2. Click "Classify Question"
3. View the classification and explanation

### Image Upload
1. Click "Upload an Image" in the sidebar
2. Select an image file (JPG, JPEG, PNG)
3. The app will extract text using OCR and classify it
4. View the extracted text and classification results

### Excel Batch Processing
1. Click "Upload Excel File" in the sidebar
2. Upload an Excel file (.xlsx) with questions
3. The file should have a 'question' column or questions in the first column
4. View the batch classification results in a table

## Project Structure 📁

```
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
```

## Dependencies 📦

- **streamlit**: Web app framework
- **agno**: AI agent framework
- **easyocr**: Optical Character Recognition
- **pandas**: Data manipulation for Excel processing
- **groq**: Alternative LLM provider
- **python-dotenv**: Environment variable management
- **duckduckgo-search**: Web search functionality
- **tavily-python**: Advanced web search API

## Configuration ⚙️

The application uses multiple AI agents:

- **Classifier Agent**: Categorizes questions using GPT-4
- **DuckDuckGo Searcher**: Performs web searches using DuckDuckGo
- **Tavily Searcher**: Performs advanced web searches using Tavily API
- **Orchestrator**: Coordinates all agents for comprehensive responses

## Troubleshooting 🔧

### Common Issues

1. **OCR not working**
   - Ensure the image contains clear, readable text
   - Check if EasyOCR downloaded the required models

2. **API errors**
   - Verify your API keys are correct in the `.env` file
   - Check your API usage limits

3. **Excel upload issues**
   - Ensure your Excel file has a 'question' column
   - Check that the file is in .xlsx format

4. **Installation problems**
   - Try upgrading pip: `pip install --upgrade pip`
   - Use specific package versions if conflicts occur

### Performance Tips

- For better OCR results, use high-quality, well-lit images
- Keep questions clear and concise for better classification
- Large Excel files may take longer to process

## License 📄

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing 🤝

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## Support 💬

For issues and questions:
- Check the troubleshooting section above
- Create an issue in the repository
- Ensure you have the latest versions of all dependencies

## Acknowledgments 🙏

- OpenAI for GPT-4 API
- Tavily for web search capabilities
- EasyOCR for optical character recognition
- Streamlit for the web framework