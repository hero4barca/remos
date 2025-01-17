import os
import sys

# Get the "env" variable from the environment, default to "dev"
env = os.getenv('env', 'dev').lower()

try:
    if env == 'staging':
        from .staging import *  # Import settings from staging.py
    elif env == 'production':
        from .production import *  # Import settings from production.py
    else:
        from .dev import *  # Default to dev.py
except ImportError as e:
    # If there's an import error, log it and fall back to dev.py
    sys.stderr.write(f"Error importing settings for '{env}': {e}\n")
    from .dev import *
