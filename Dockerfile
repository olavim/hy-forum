FROM python:3-alpine

WORKDIR /usr/src/app

COPY run.py ./
COPY requirements.txt ./
COPY application ./application

RUN apk update \
	&& apk add --virtual build-deps gcc python3-dev musl-dev libffi-dev \
	&& apk add --no-cache gcc

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 80

CMD ["python", "run.py"]