FROM python:3-alpine

WORKDIR /usr/src/app

COPY app app
COPY requirements.txt requirements.txt

RUN apk update \
	&& apk add --virtual build-deps gcc python3-dev musl-dev \
	&& apk add --no-cache gcc

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "app/main.py"]