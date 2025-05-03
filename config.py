from dotenv import load_dotenv
import os
import base64

load_dotenv()

RAW_KEY = os.getenv("SECRET_KEY")

missing_padding = len(RAW_KEY) % 4
if missing_padding:
    RAW_KEY += '=' * (4 - missing_padding)

ALGORITHM = "HS256"
SECRET_KEY = base64.b64decode(RAW_KEY)