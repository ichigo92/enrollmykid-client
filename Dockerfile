FROM python:3.7-alpine
WORKDIR /myapp
COPY . /myapp
RUN pip install -r requirements.txt
EXPOSE 8081
CMD ["python", "app.py"]
