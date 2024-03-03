<div align="center">
  <h3 align="center">RKNAdmin</h3>

  <p align="center">
    Web application allowing university scientific club members to easily manage their organization data and simplify formal matters between them and university authorities.
  </p>
</div>

## Getting Started

### Tech stack
* Django 5.0.2
* PostgreSQL 16.2
* pgAdmin 4 8.3

### Installation

1. Clone the repository
```sh
git clone https://github.com/tomasz-jankowski/rkn
cd rkn
```

2. Create .env file in root directory with below entries
```text
ENV=development                     # or production
ALLOWED_HOSTS=example.com,test.com  # allowed hosts (comma-delimited, production only)
PORT=8000                           # web app port
SECRET_KEY=secret-key               # Django secret key
DB_NAME=postgres                    # database name
DB_HOST=postgres                    # database host
DB_PORT=8001                        # pgAdmin port
DB_USER=user                        # database user
DB_EMAIL=name@example.com           # database user e-mail
DB_PASSWORD=password                # database password
```

3. Build image and run container
```sh
docker compose build
docker compose up -d
```

### Notes

#### Persistent storage
PostgreSQL and pgAdmin use persistent storage by defining Docker volumes in `docker-compose.yaml` files. If you want to e.g. change credentials you need to recreate the volumes.

```sh
docker compose down -v
```

#### Django admin credentials
To create your first Django admin user, you need to exec into running container bash.

First, get your container name.
```sh
❯ docker ps
CONTAINER ID   IMAGE                COMMAND                  CREATED         STATUS             PORTS                           NAMES
8e70acf9c6d2   rkn-web              "python manage.py ru…"   8 minutes ago   Up 8 minutes       0.0.0.0:8000->80/tcp            rkn-web-1
ceda2c3bad39   postgres:16.2        "docker-entrypoint.s…"   8 minutes ago   Up 8 minutes       5432/tcp                        rkn-postgres-1
128ada0e335b   dpage/pgadmin4:8.3   "/entrypoint.sh"         8 minutes ago   Up 8 minutes       443/tcp, 0.0.0.0:8001->80/tcp   rkn-pgadmin-1
```

Then, exec into container bash, run migrations and create a new user.
```sh
❯ docker exec -it rkn-web-1 bash
root@8e70acf9c6d2:/app# python manage.py makemigrations
root@8e70acf9c6d2:/app# python manage.py migrate
root@8e70acf9c6d2:/app# python manage.py createsuperuser
Username (leave blank to use 'root'): admin
Email address: admin@example.com
Password: 
Password (again): 
Superuser created successfully.

```