FROM python:3.6

EXPOSE 5000

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONBUFFERED=1

COPY requirements.txt .
RUN python -m pip install -r requirements

CMD ["python", 'wsgi.py']