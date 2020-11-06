FROM python:3.8-alpine
WORKDIR /resourcesr_lite
RUN pip install -r requirements.txt
ADD . .
CMD ["python3","app.py"]
