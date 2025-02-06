FROM pwn.red/jail

COPY --from=ubuntu:jammy-20240227 / /srv

RUN mkdir -p /srv/app

ARG BINARY_FILE
COPY ${BINARY_FILE} /srv/app/run

RUN chmod +x /srv/app/run

ARG FLAG_FILE
COPY ${FLAG_FILE} /srv/app/flag.txt

EXPOSE 5000
