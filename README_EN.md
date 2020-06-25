![python3-badge](https://img.shields.io/badge/python-django-green.svg)
![enter image description here](https://img.shields.io/badge/license-GPLv3-blue.svg)

# API Enquetes
> It provides an API to query the participation of polls data through a REST architecture

# Installation

> There are two ways to install this project. The first is using Docker and the second is using Pipenv. Both ways the project will run on port 8005. Being accessible through the link:

- http://www.localhost:8005

## Docker

### Requirements

It's necessary to instal this softwares:

- [Docker](https://docs.docker.com/engine/install/ubuntu/)
- [Docker-Compose](https://docs.docker.com/compose/install/)
- Create a file with name **.env** on same folder file **settings.py** it is. You need to create the following environment variables.

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

1 - Open your terminal and clone this repository by typing

```sh
git clone https://github.com/labhackercd/api_enquetes.git
```

2 - Navigate to the root directory and enter

```sh
cd api_enquetes
docker-compose up
```

## Pipenv

1 - Open your terminal and clone this repository by typing

```
git clone https://github.com/labhackercd/api_enquetes.git
```

First of all, you need to install [pipenv](https://pipenv.readthedocs.io/en/latest/install/#installing-pipenv). After install these dependencie you can run the follow commands:

```
pipenv install
```

### Running

```
pipenv run src/manage.py runserver 0.0.0.0:8005
```

## Support

Fell free to create any issue on this repository and contact the team responsible to maintain this project here on GitHub (@erivanio, @thiagonf, @joaopaulonsoares and @teogenesmoura) or via email: labhacker@camara.leg.br.

## Contributing

1. Fork of this repository
2. Write your code
3. Create a Pull Request
4. Our team will review your PR and merge as soon as possible!

## License

This project is under GPLv3 License
