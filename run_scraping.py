import os
import django

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'catalogo.settings')
django.setup()

# Importe a função de scraping após configurar o Django
from catalogo.commands.scrap import scraping_function

# Execute a função de scraping
scraping_function()
