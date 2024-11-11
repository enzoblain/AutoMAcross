import os

from dotenv import load_dotenv

def getFromEnv(attr):
    load_dotenv()

    value = os.getenv(attr)

    if not value:
        raise ValueError(f"{attr} not found. Please set it in the .env file.")

    return value