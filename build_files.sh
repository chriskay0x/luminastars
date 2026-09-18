#!/bin/bash
# Force install dependencies bypassing the Vercel env restriction
python -m pip install -r requirements.txt --break-system-packages

# Collect the static files
python manage.py collectstatic --noinput --clear