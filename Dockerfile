FROM ubuntu:20.04
FROM python:3.8

RUN mkdir rozhkovPetProject
WORKDIR /rozhkovPetProject

COPY requirements.txt .
#RUN export PATH="/root/.local/bin:$PATH"
RUN pip install -r requirements.txt

COPY . .