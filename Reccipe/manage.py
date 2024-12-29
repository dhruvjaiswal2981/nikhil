#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Reccipe.settings')

    # Port Binding for Render or Dynamic Environment
    port = os.environ.get("PORT", "8000")
    try:
        from django.core.management import execute_from_command_line
        # Add dynamic port binding if running via `runserver`
        if sys.argv[1] == "runserver":
            sys.argv[2] = f"0.0.0.0:{port}"
    except (ImportError, IndexError):
        pass  # IndexError if no command is provided, it continues as usual.

    try:
        execute_from_command_line(sys.argv)
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc


if __name__ == '__main__':
    main()
