#!/bin/bash

# Migrate the database
python manage.py migrate

# Execute the main container command
exec "$@"
