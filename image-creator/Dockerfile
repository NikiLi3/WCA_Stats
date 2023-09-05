FROM python:3-slim

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY create_images.py ./

CMD python /create_images.py