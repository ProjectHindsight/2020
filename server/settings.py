from dotenv import load_dotenv
from pathlib import Path

# Load .env file
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# Load .env-no-git
env_no_git_path = Path('.') / '.env-no-git'
load_dotenv(dotenv_path=env_no_git_path)