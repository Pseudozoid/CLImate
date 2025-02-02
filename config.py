import os
from dotenv import load_dotenv

ENV_FILE = '.env'

def get_api_key():
    # Load existing environment variables from .env
    load_dotenv()

    api_key = os.getenv('API_KEY')

    if not api_key:
        api_key = input("Enter your API key: ").strip()

        # Save it in .env
        with open(ENV_FILE, 'a') as f:
            f.write(f"API_KEY={api_key}\n")

        print("API key saved successfully.")

    return api_key

