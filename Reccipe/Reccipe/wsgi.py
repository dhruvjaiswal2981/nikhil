import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise
from pathlib import Path  # Import Path for defining BASE_DIR

# Define BASE_DIR
BASE_DIR = Path(__file__).resolve().parent.parent

# Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Reccipe.settings')

# Get the WSGI application
application = get_wsgi_application()

# Add WhiteNoise to serve static files
application = WhiteNoise(application, root=os.path.join(BASE_DIR, 'staticfiles'))
