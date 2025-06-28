import easyocr
import asyncio
from io import BytesIO
from PIL import Image

# Initialize EasyOCR with English ('en') and Hindi ('hi')
SUPPORTED_LANGUAGES = ['en', 'hi']
reader = easyocr.Reader(SUPPORTED_LANGUAGES)


async def extract_text_from_image(image_bytes: bytes) -> str:
    loop = asyncio.get_event_loop()

    # Pass raw bytes directly to EasyOCR
    result = await loop.run_in_executor(None, reader.readtext, image_bytes)

    extracted_text = " ".join([text[1] for text in result])
    return extracted_text


