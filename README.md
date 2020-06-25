![python3-badge](https://img.shields.io/badge/python-django-green.svg)
![enter image description here](https://img.shields.io/badge/license-GPLv3-blue.svg)

# API Enquetes
[Documentation in English](https://github.com/labhackercd/api_enquetes/blob/dev/README_EN.md)
> Este projeto provê uma API para consultas das participações das enquetes por meio de uma arquitetura REST.

# Instalação

> Existem duas formas de instalr este projeto. A primeira forma é utilizando o Docker e a segunda forma é utilizando o Pipenv. Em ambas a aplicação será executada na porta 8005, podendo ser acessada pelo link a seguir:

- http://www.localhost:8005

## Docker

### Requisitos

É necessário a instalação dos seguintes softwares:

- [Docker](https://docs.docker.com/engine/install/ubuntu/)
- [Docker-Compose](https://docs.docker.com/compose/install/)
- Criar um arquivo com o nome **.env** na pasta em que se encontra o arquivo **settings.py**. É necessário preencher todas as informações das variáveis de ambiente para que o projeto consiga ser inicializado.

```sh
SECRET_KEY=
DEBUG=
ALLOWED_HOSTS=
ENGINE= 
NAME=
HOST=
PORT=
USER_DB=
PASSWORD=
DRIVER=
```

1 - Abra o seu terminal e clone este repositório:

```sh
git clone https://github.com/labhackercd/api_enquetes.git
```

2 - Entre até a pasta raiz do projeto e execute o docker-compose:

```sh
cd api_enquetes
docker-compose up
```

3 - O projeto já está acessível na porta 5000 do localhost.

## Pipenv

### Requisitos

É necessário a instalação do seguinte software:

- [pipenv](https://pipenv.readthedocs.io/en/latest/install/#installing-pipenv)

1 - Abra o seu terminal e clone este repositório

```
git clone https://github.com/labhackercd/api_enquetes.git
```

```
pipenv install
```

### Execuntando

```
pipenv run src/manage.py runserver 0.0.0.0:8005
```

## Suporte

Contate os mantenedores do porojeto pelo GitHub (@erivanio, @thiagonf, @joaopaulonsoares and @teogenesmoura) ou por email: labhacker@camara.leg.br.

## Licença

Este projeto está sob a licença GPLv3
