FROM python:3.9

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/

COPY . /usr/src/app/

RUN pip install --user aiogram

CMD ["python", "app.py"]