#!/bin/bash

# Exit on any error
set -e

# Run migrations
echo "Running migrations..."
python manage.py migrate


# Create superuser if it doesn't exist (Remove for production)
echo "Creating superuser..."
python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin')
    print('Superuser created')
else:
    print('Superuser already exists')
"

# Start the Django development server
echo "Starting Django server..."
exec python manage.py runserver 0.0.0.0:8000