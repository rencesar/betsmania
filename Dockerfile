FROM python:3.5

# Install PIP and Requiriments
  ENV PYTHONUNBUFFERED 1
  RUN mkdir /code
  WORKDIR /code
  ADD requirements/dev.txt /code
  RUN pip install -r requirements.txt
  ADD . /code/