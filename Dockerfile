FROM ubuntu:18.04

# Development: where the actual coding takes place
# Staging: where the application is reviewed and tested
# Production: where the final version of the application is hosted

# Define Your Envs Config
ENV PYENV_ROOT=$HOME/.pyenv
ENV PATH=$PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH
ENV DEBIAN_FRONTEND=noninteractive


# Install Ubuntu Dependences
RUN apt-get update && apt-get upgrade -y

RUN apt-get install -y \
    curl \
    apt-transport-https \
    git-core \
    make \
    build-essential \
    libssl-dev \
    zlib1g-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    wget \
    llvm \
    libncurses5-dev \
    libncursesw5-dev \
    xz-utils \
    tk-dev \
    libffi-dev \
    liblzma-dev \
    unixodbc-dev

# Config Timezone America/Sao_Paulo
RUN ln -fs /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime && dpkg-reconfigure -f noninteractive tzdata

# Install Pyenv
RUN curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash

# Update Pyenv
RUN pyenv update

# Install Python 3.6.5
RUN pyenv install 3.6.5

# Set Python Global
RUN pyenv global 3.6.5
RUN pyenv rehash

# Upgrade PIP
RUN pip install --upgrade pip

# Install ODBC Driver
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/ubuntu/18.04/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN apt-get update
RUN ACCEPT_EULA=Y apt-get install msodbcsql17 mssql-tools -y
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bash_profile
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc

RUN echo "---> Cleaning up" \
    && apt-get autoremove -y \
    && apt-get autoclean -y \
    && apt-get clean -y \
    && rm -rf /tmp/*

RUN mkdir -p /var/labhacker/api_enquetes

WORKDIR /var/labhacker/api_enquetes --no-ca
ADD . /var/labhacker/api_enquetes/
RUN pip install -r requirements.txt

CMD [ "python3", "src/manage.py runserver 0.0.0.0:8000" ]