FROM pwn.red/jail

COPY --from=ubuntu:jammy-20240227 / /srv

RUN mkdir -p /srv/app

COPY bin /srv/app/run

RUN chmod +x /srv/app/run

EXPOSE 5000
