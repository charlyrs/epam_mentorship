FROM  python

WORKDIR /app

ENV DATA_DIRECTORY /data

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "code.py"]