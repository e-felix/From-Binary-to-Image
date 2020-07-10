import os
from dotenv import load_dotenv


def read_env_vars():
    """ Get the S3 environment variables """
    load_dotenv()

    return {
        "DATABASE_NAME": os.getenv("DATABASE_NAME"),
        "DATABASE_HOST": os.getenv("DATABASE_HOST"),
        "DATABASE_PORT": os.getenv("DATABASE_PORT"),
        "DATABASE_USER": os.getenv("DATABASE_USER"),
        "DATABASE_PASSWORD": os.getenv("DATABASE_PASSWORD")
    }