FROM python:3.10.2


ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#create virtual env 

WORKDIR /code


COPY ./requirements.txt .
RUN pip install -r requirements.txt


COPY . .



