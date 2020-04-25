import os
from dotenv import load_dotenv
from pathlib import Path

#  specify the path to .env
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# env vars
DB_CLIENT = os.getenv("DB_CLIENT")
