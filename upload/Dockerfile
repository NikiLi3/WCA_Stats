FROM python

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY upload_script.py ./

CMD python /upload_script.py