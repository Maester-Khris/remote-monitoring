#!bin/bash

if [ -z "$VIRTUAL_ENV" ]; then
    echo "❌ No Python virtual environment is active. Please activate it first."
    exit 1
fi

if [ ! -f manage.py ]; then
    echo "Navigate to the root of the django project"
    exit 1
fi

python manage.py shell
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())