# Enable the development environment
import os
DEBUG = True

# Define the application directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# FILEALCHEMY_DATA_DIR = os.path.join(BASE_DIR, 'data')

# Define the SQLite database file
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
# SQLALCHEMY_TRACK_MODIFICATIONS = False
DATABASE_CONNECT_OPTIONS = {}

# Threads per request
THREADS_PER_PAGE = 2

# Enable protection against *Cross-site Request Forgery (CSRF)*
# CSRF_ENABLED = True

# Secure, unique and absolutely secret key for signing the data.
CSRF_SESSION_KEY = "Gupt4Ch4bi@2023"

# Secret key for signing cookies
SECRET_KEY = "Gupt4Ch4bi@2023"

# Password Security Salt
SECURITY_PASSWORD_SALT = "Gupt4Ch4bi@2023"
SECURITY_TOKEN_AUTHENTICATION_HEADER = "Authentication-Token"
