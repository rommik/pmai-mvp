FROM python:3.9


RUN pip install poetry
# Install Make
RUN apt-get update && apt-get install -y make

WORKDIR /code

COPY . .
RUN ls -la
RUN make install

CMD ["make", "prod"]