# Enabling the development environment
DEBUG = True

# Application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Database


# Application threads
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True
CSRF_SESSION_KEY = "secret"

# Secret key for signing cookies
SECRET_KEY = "secret"
