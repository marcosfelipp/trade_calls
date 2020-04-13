FROM python:3.6

RUN apt-get update && apt-get install -y python3-dev build-essential

WORKDIR /apiserver

COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir --ignore-installed six -r requirements.txt

COPY api/api.py .
COPY app.py .

CMD [ "python", "./app.py" ]