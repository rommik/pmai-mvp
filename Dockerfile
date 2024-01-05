FROM python:3.9

WORKDIR /code


RUN make install

COPY . .

CMD ["make", "prod"]