FROM python:3.9
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["gunicorn", "manage:app", "-b", "0.0.0.0:8000"]
