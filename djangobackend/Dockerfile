FROM python:3.10

RUN mkdir /app

WORKDIR /app

# set env var
# Prevents Python from writing pyc files to disk
#Prevents Python from buffering stdout and stderr
# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHONUNBUFFERED=1
# ENV DEBUG=1
# ENV DJANGO_ALLOWED_HOSTS="example.com,127.0.0.1"

RUN pip install --upgrade pip 

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

RUN rm ./djangobackend/settings.py
RUN mv ./djangobackend/settings_prod.py ./djangobackend/settings.py

# --- STATIC FILES CONFIGURATION ---
# Set the directory where static files will be collected
# If you're using a non-root user (recommended for production):
# USER appuser # Ensure collectstatic is run as the app user
# RUN chown -R appuser:appgroup ${DJANGO_STATIC_ROOT} # Ensure ownership

ENV DJANGO_STATIC_ROOT=/vol/web/static/
RUN mkdir -p ${DJANGO_STATIC_ROOT}

ENV DJANGO_SETTINGS_SKIP_REDIS_CONNECT=1

# Collect static files
# --noinput prevents prompts for confirmation
#RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000","--workers", "3", "--threads", "2", "djangobackend.wsgi:application"]