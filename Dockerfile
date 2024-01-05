FROM python:3.12


RUN pip install poetry && export VIRTUAL_ENV_DISABLE_PROMPT=1
# Install Make
RUN apt-get update && apt-get install -y make

WORKDIR /code

COPY . .
RUN ls -la
RUN make install

CMD ["make", "prod"]