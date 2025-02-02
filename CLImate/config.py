import os
from dotenv import load_dotenv

CONFIG_DIR = os.path.expanduser("~/.config/climate")
ENV_FILE = os.path.join(CONFIG_DIR, ".env")

def get_api_key():
    # Ensure the config directory exists
    os.makedirs(CONFIG_DIR, exist_ok=True)

    # Load existing environment variables from .env
    load_dotenv(ENV_FILE)

    api_key = os.getenv("API_KEY")

    if not api_key:
        api_key = input("Enter your API key: ").strip()

        # Save it in .env
        with open(ENV_FILE, "w") as f:
            f.write(f"API_KEY={api_key}\n")

        print("API key saved successfully.")

    return api_key

