import os
import sys

# Defina a variável de ambiente DJANGO_SETTINGS_MODULE
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'catalogo.settings')

# Adicione o caminho do diretório pai ao sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

def main():
    """Django's command-line utility for administrative tasks."""
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
    

if __name__ == '__main__':
    main()
