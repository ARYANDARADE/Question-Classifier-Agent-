# from fastapi import FastAPI, UploadFile, File, Form
# from fastapi.responses import JSONResponse
# from pydantic import BaseModel
# import asyncio
# import json
# import pandas as pd
# from io import BytesIO
# import uvicorn
# from tools.ocr import extract_text_from_image
# from agno.agent import RunResponse
# from tools.tools import orchestrator, classifier


# app=FastAPI()

# class QuestionRequest(BaseModel):
#     question: str
    
# @app.post("/ask")
# async def ask_question(request: QuestionRequest):
#     """
#     Endpoint to classify a user question and retrieve an answer.
#     """
#     response: RunResponse  = orchestrator.run(request.question)
#     # Convert to JSON
#     response_json = json.dumps({"response": response}, indent=4)

#     return JSONResponse(content=json.loads(response_json))

# @app.post("/upload")
# async def upload_image(file: UploadFile = File(...)):
#     """
#     Endpoint to extract text from an image and classify the extracted text.
#     """
#     image_bytes = await file.read()
#     extracted_text = await extract_text_from_image(image_bytes)
    
#     if not extracted_text:
#         return {"error": "No text detected in the image."}
    
#     response: RunResponse = orchestrator.run(extracted_text)
#     # Convert to JSON
#     response_json = json.dumps({"response": response}, indent=4)

#     return JSONResponse(content=json.loads(response_json))

# @app.post("/classify-xlsx")
# async def classify_xlsx(file: UploadFile = File(...)):
#     """
#     Accept an Excel file (.xlsx) containing a list of questions, classify each using only the Classifier agent.
#     """
#     if not file.filename.endswith(".xlsx"):
#         return JSONResponse(content={"error": "Only .xlsx files are supported."}, status_code=400)
    
#     # Wrap bytes in BytesIO to avoid the FutureWarning
#     contents = await file.read()
#     df = pd.read_excel(BytesIO(contents))

#     # Ensure there's a column named 'question' or use the first column
#     if 'question' in df.columns:
#         questions = df['question'].dropna().tolist()
#     else:
#         questions = df.iloc[:, 0].dropna().tolist()

#     results = []
#     for q in questions:
#         result: RunResponse = classifier.run(str(q))
        
#         # Convert RunResponse to dict safely (adjust based on how it's implemented)
#         if hasattr(result, "dict"):
#             result_dict = result.dict()
#         elif hasattr(result, "__dict__"):
#             result_dict = result.__dict__
#         else:
#             result_dict = str(result)

#         results.append({"question": q, "classification": result_dict})

#     return JSONResponse(content={"results": results})

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)

# import streamlit as st
# import pandas as pd
# from io import BytesIO
# import json
# from tools.ocr import extract_text_from_image
# from agno.agent import RunResponse
# from tools.tools import orchestrator, classifier

# # Set up the Streamlit app layout
# st.set_page_config(page_title="Question Prism App", layout="wide")

# # Sidebar with app title and file upload options
# st.sidebar.title("Question Prism App")
# option = st.sidebar.radio("Choose an option:", ("Ask a Question", "Upload Image", "Upload .xlsx"))

# # Main content
# st.title("Welcome to Question Prism App")

# # Handle different options based on user input
# if option == "Ask a Question":
#     question = st.text_input("Type your question below:")

#     if question:
#         # Run the question through the orchestrator and display the response
#         response: RunResponse = orchestrator.run(question)
        
#         # Convert response to a serializable format
#         if hasattr(response, "dict"):
#             response_dict = response.dict()
#         elif hasattr(response, "__dict__"):
#             response_dict = response.__dict__
#         else:
#             response_dict = str(response)
        
#         st.write("**Answer:**")
#         st.json(response_dict)

# elif option == "Upload Image":
#     uploaded_file = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg"])

#     if uploaded_file is not None:
#         image_bytes = uploaded_file.read()
#         extracted_text = extract_text_from_image(image_bytes)
        
#         if extracted_text:
#             st.write("**Extracted Text:**")
#             st.write(extracted_text)
            
#             # Classify the extracted text
#             response: RunResponse = orchestrator.run(extracted_text)
            
#             # Convert response to a serializable format
#             if hasattr(response, "dict"):
#                 response_dict = response.dict()
#             elif hasattr(response, "__dict__"):
#                 response_dict = response.__dict__
#             else:
#                 response_dict = str(response)

#             st.write("**Classification Result:**")
#             st.json(response_dict)
#         else:
#             st.error("No text detected in the image.")

# elif option == "Upload .xlsx":
#     uploaded_file = st.file_uploader("Upload an Excel File", type=["xlsx"])

#     if uploaded_file is not None:
#         # Read the uploaded Excel file
#         contents = uploaded_file.read()
#         df = pd.read_excel(BytesIO(contents))

#         # Ensure there is a column 'question' or use the first column
#         if 'question' in df.columns:
#             questions = df['question'].dropna().tolist()
#         else:
#             questions = df.iloc[:, 0].dropna().tolist()

#         results = []
#         for q in questions:
#             result: RunResponse = classifier.run(str(q))
            
#             # Convert RunResponse to dict safely
#             if hasattr(result, "dict"):
#                 result_dict = result.dict()
#             elif hasattr(result, "__dict__"):
#                 result_dict = result.__dict__
#             else:
#                 result_dict = str(result)

#             results.append({"question": q, "classification": result_dict})

#         st.write("**Classification Results for all questions in the file:**")
#         st.json(results)

import streamlit as st
import pandas as pd
import re
import asyncio
from io import BytesIO
from tools.ocr import extract_text_from_image
from tools.tools import orchestrator, classifier
from agno.agent import RunResponse
import time

def stream_response(content_text, chunk_size=20, delay=0.05):
    """Synchronous generator to yield response in chunks"""
    for i in range(0, len(content_text), chunk_size):
        yield content_text[i:i + chunk_size]
        time.sleep(delay)  # Simulate typing

def display_response(response_obj, stream=False):
    try:
        content_text = response_obj.content if hasattr(response_obj, 'content') else str(response_obj)
        explanation_match = re.search(r"(?:Here's a comprehensive explanation|Here's the information.*?):\n\n(.*)", content_text, re.DOTALL)
        explanation = explanation_match.group(1).strip() if explanation_match else content_text

        st.markdown("### 📖 Explanation")
        if stream:
            placeholder = st.empty()
            displayed_text = ""
            for chunk in stream_response(explanation):
                displayed_text += chunk
                placeholder.success(displayed_text)
        else:
            st.success(explanation)
    except Exception as e:
        st.error(f"⚠️ Failed to parse and display the response: {e}")

# Page Config
st.set_page_config(page_title="Question Classifier", layout="wide")

# --- Sidebar ---
st.sidebar.markdown("## 💡 Question Classifier")
st.sidebar.markdown("Analyze typed or scanned questions to get the category and explanation.")
st.sidebar.markdown("---")

upload_image = st.sidebar.file_uploader("📤 Upload an Image", type=["jpg", "jpeg", "png"], key="img_upload")
upload_excel = st.sidebar.file_uploader("📥 Upload Excel File (.xlsx)", type=["xlsx"], key="xlsx_upload")

st.title("📚 Question Prism (Question Classifier)")

st.subheader("📝 Type a Question")
question_input = st.text_input("Enter your question below:")

if st.button("Classify Question"):
    if question_input.strip() == "":
        st.warning("Please enter a valid question.")
    else:
        with st.spinner("Classifying..."):
            response: RunResponse = orchestrator.run(question_input)
        st.success("✅ Classification Complete!")
        display_response(response, stream=True)

if upload_image is not None:
    st.subheader("🖼️ Image Classification Result")
    with st.spinner("Extracting text from image..."):
        image_bytes = upload_image.getvalue()
        extracted_text = asyncio.run(extract_text_from_image(image_bytes))

    if not extracted_text:
        st.error("❌ No text detected in the image.")
    else:
        st.success("✅ Text extracted successfully!")
        st.text_area("Extracted Text", extracted_text, height=150)

        with st.spinner("Classifying extracted text..."):
            response: RunResponse = orchestrator.run(extracted_text)
        st.success("✅ Classification Complete!")
        display_response(response, stream=True)

if upload_excel is not None:
    st.subheader("📊 Excel File Classification Result")
    contents = upload_excel.read()
    df = pd.read_excel(BytesIO(contents))

    if 'question' in df.columns:
        questions = df['question'].dropna().tolist()
    else:
        questions = df.iloc[:, 0].dropna().tolist()

    results = []
    for q in questions:
        result: RunResponse = classifier.run(str(q))
        if hasattr(result, "dict"):
            data = result.dict()
        elif hasattr(result, "__dict__"):
            data = result.__dict__
        else:
            data = {}
        answer = data.get("answer", data.get("content", "No answer found."))
        results.append({
            "Question": q,
            "Category": answer
        })

    st.success(f"✅ Classified {len(results)} questions successfully!")
    st.dataframe(pd.DataFrame(results))

