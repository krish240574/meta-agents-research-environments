import os

# Ensure the API key is correctly set
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
if not OPENAI_API_KEY:
    raise ValueError('OPENAI_API_KEY is not set. Please check your environment variables.')

OPENAI_BASE_URL = os.getenv('OPENAI_BASE_URL')
if not OPENAI_BASE_URL:
    raise ValueError('OPENAI_BASE_URL is not set. Please check your environment variables.')