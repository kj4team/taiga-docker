FROM taigaio/taiga-back:latest

# Insert custom configuration into the taiga configuration file
COPY config.append.py /taiga-back/settings
RUN cat /taiga-back/settings/config.append.py >> /taiga-back/settings/config.py && rm /taiga-back/settings/config.append.py

# Install git, because we need it to install the taiga-ldap-contrib-auth-ext package
RUN apt-get update \
    && apt-get install -y git \
    && rm -rf /var/lib/apt/lists/*

RUN pip install git+https://github.com/TuringTux/taiga-contrib-ldap-auth-ext-2.git

RUN apt-get purge -y git \
    && apt-get autoremove -y