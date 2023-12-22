FROM tiangolo/uwsgi-nginx-flask:python3.11

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Dumb bullshit my favorite
COPY mime.types /etc/mime.types
COPY ./app /app
