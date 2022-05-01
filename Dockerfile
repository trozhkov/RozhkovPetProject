FROM ubuntu:latest
FROM reg.uptr.dev/public-projects/python-unprivileged:3.8

COPY requirements.txt .
RUN pip3 install --no-cache-dir --user -r requirements.txt
COPY . .