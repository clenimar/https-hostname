FROM python:3.7-alpine

# NOTE! `key-u.pem` is unencrypted.
# using it for DEV purposes only!
COPY etc/key.pem /etc/app/key-u.pem
COPY etc/cert.pem /etc/app/cert.pem
COPY src /app

WORKDIR /app

EXPOSE 4443

ENTRYPOINT ["python3", "app.py"]
