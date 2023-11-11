import openai

from docx import Document
from pathlib import Path
from openai import OpenAI


# Load your API key
api_key_path = 'openaiapikey.txt'  # Path to your API key file
with open(api_key_path, 'r') as file:
    api_key = file.read().strip()
    

# Initialize the OpenAI client
client = openai.OpenAI(api_key=api_key)


def open_file(filepath):
    doc = Document(filepath)
    return " ".join([para.text for para in doc.paragraphs])

word1 = open_file('summary.docx')


speech_file_path = Path(__file__).parent / "speech.mp3"
response = client.audio.speech.create(
  model="tts-1",
  voice="onyx",
  input=word1
)

response.stream_to_file(speech_file_path)