FROM python:3.12


RUN pip install poetry
# Install Make
RUN apt-get update && apt-get install -y make

WORKDIR /code

COPY . .
RUN ls -la
RUN virtualenv -p python3.12 /code/.venv
RUN make install

CMD ["make", "prod"]