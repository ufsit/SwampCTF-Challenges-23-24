FROM pwn.red/jail

COPY --from=ubuntu:jammy-20240227 / /srv

RUN mkdir -p /srv/app

COPY evaluation.bash /srv/app/run

RUN chmod +x /srv/app/run

ENV JAIL_ENV_employee_john_score=19
ENV JAIL_ENV_employee_james_score=16
ENV JAIL_ENV_employee_cole_score=57
ENV JAIL_ENV_employee_adam_score=84
ENV JAIL_ENV_employee_wilson_score=61
ENV JAIL_ENV_employee_ethan_score=56
ENV JAIL_ENV_employee_omar_score=74
ENV JAIL_ENV_employee_vic_score=81
ENV JAIL_ENV_employee_alex_score=00
ENV JAIL_ENV_employee_scott_score=94
ENV JAIL_ENV_employee_ben_score=47
ENV JAIL_ENV_employee_phoenix_score=89
ENV JAIL_ENV_employee_daniel_score=48
ENV JAIL_ENV_employee_jon_score=41
ENV JAIL_ENV_employee_jack_score=80
ENV JAIL_ENV_____secret_never_reveal_pls_thx__=swampCTF{eva1_c4t_pr0c_3nvir0n_2942}

EXPOSE 5000
