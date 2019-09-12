FROM olavim/python-libsass:1.0.0

RUN apk update \
	&& apk add --no-cache postgresql-dev libffi-dev

WORKDIR /usr/src/app

COPY run.py ./
COPY requirements.txt ./
COPY application ./application

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 80

CMD ["python", "run.py"]