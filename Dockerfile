FROM python:3.12

RUN useradd -ms /bin/bash admin

RUN pip install poetry
# Install Make
RUN apt-get update && apt-get install -y make

WORKDIR /code
RUN chown -R admin:admin /code
RUN chmod 755 /code
USER admin
COPY . .
RUN ls -la
RUN virtualenv -p python3.12 /code/.venv
RUN make install
EXPOSE 7860
CMD ["make", "prod"]