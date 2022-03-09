FROM python:3.9-alpine

RUN pip install gunicorn

RUN mkdir /workdir
WORKDIR /workdir
COPY test.py /workdir
CMD ["gunicorn", "test:simple_app", "--bind", "0.0.0.0:8000"]