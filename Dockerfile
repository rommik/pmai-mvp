FROM python:3.9

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Install Make
RUN apt-get update && apt-get install -y make

WORKDIR /code

COPY . .

RUN make install

CMD ["make", "prod"]