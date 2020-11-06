FROM python:3.8-alpine
WORKDIR /resourcesr_lite
ADD . /resourcesr_lite
RUN pip install -r requirements.txt
CMD ["python3","app.py"]
