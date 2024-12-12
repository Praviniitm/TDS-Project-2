import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv(dotenv_path="C:/Users/91963/OneDrive/Documents/TDS Project 2/Open_AI_secret_Key.env")



# Access the environment variable
open_ai_secret_key = os.getenv("Open_AI_secret_Key")

# Check if the variable exists
if open_ai_secret_key:
    print(f"OpenAI Secret Key: {open_ai_secret_key}")
else:
    print("Environment variable not found!")

