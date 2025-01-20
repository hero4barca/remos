import os
import sys
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the "env" variable from the environment, default to "dev"
env_type = os.getenv('ENV_TYPE', 'dev').lower()

try:
    if env_type == 'staging':
        from .staging import *  # Import settings from staging.py
    elif env_type == 'production':
        from .production import *  # Import settings from production.py
    else:
        from .dev import *  # Default to dev.py
except ImportError as e:
    # If there's an import error, log it and fall back to dev.py
    sys.stderr.write(f"Error importing settings for '{env_type}': {e}\n")
    from .dev import *
