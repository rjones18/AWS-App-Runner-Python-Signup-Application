FROM python:3.7-slim
WORKDIR /myapp
COPY application.py /myapp/application.py
COPY app/ /myapp/app/
COPY requirements.txt /myapp/requirements.txt
RUN pip install -r requirements.txt
CMD ["python", "/myapp/application.py"]