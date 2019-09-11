FROM python:3-alpine

WORKDIR /usr/src/app

COPY run.py ./
COPY requirements.txt ./
COPY application ./application

RUN apk update && \
		apk add --virtual build-base gcc g++ postgresql-dev python3-dev musl-dev libffi-dev

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 80

CMD ["python", "run.py"]