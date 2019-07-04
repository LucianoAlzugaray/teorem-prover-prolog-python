FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt && \
    apt-get update  -y && \
    apt-get install -y software-properties-common python3-tk  && \
    apt-get install -y swi-prolog 

COPY . .

CMD ["python", "src/main.py"]

