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

#### 1. Clone the repository
```sh
git clone https://github.com/tomasz-jankowski/rkn
cd rkn
```

#### 2. Create .env file in root directory with below entries
```text
# Django
ENV=development                     # or production
ALLOWED_HOSTS=example.com,test.com  # allowed hosts (comma-delimited, production only)
PORT=8000                           # web app port
SECRET_KEY=secret-key               # Django secret key

# MinIO
MINIO_API_PORT=9000                 # MinIO API port
MINIO_CONSOLE_PORT=9001             # MinIO console port
MINIO_ACCESS_KEY=access_key         # MinIO user
MINIO_SECRET_KEY=secret_key         # MinIO password
MINIO_BUCKET=name                   # MinIO default bucket name

# Postgres
DB_NAME=postgres                    # database name
DB_HOST=postgres                    # database host
DB_USER=user                        # database user
DB_PASSWORD=password                # database password

# pgAdmin
PGADMIN_EMAIL=name@example.com      # pgAdmin user e-mail
PGADMIN_PASSWORD=password           # pgAdmin password
PGADMIN_PORT=8001                   # pgAdmin port
```

#### 3. Create .minio_access_key and .minio_secret_key files in root directory containing MINIO_ACCESS_KEY and MINIO_SECRET_KEY accordingly.

.env
```text
...
MINIO_ACCESS_KEY=access_key
MINIO_SECRET_KEY=secret_key
...
```

.minio_access_key
```text
access_key
```
.minio_secret_key
```text
secret_key
```

#### 4. Build image and run container
```sh
docker compose build
docker compose up -d
```
#### 5. Configure application

##### Create and apply migrations

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
````

##### Create Django admin user

```sh
root@8e70acf9c6d2:/app# python manage.py createsuperuser
Username (leave blank to use 'root'): admin
Email address: admin@example.com
Password: 
Password (again): 
Superuser created successfully.
```

##### Use static files from MinIO storage

```sh
root@539ea1091f76:/app# python manage.py collectstatic

You have requested to collect static files at the destination
location as specified in your settings.

This will overwrite existing files!
Are you sure you want to do this?

Type 'yes' to continue, or 'no' to cancel: yes

126 static files copied.
```

### Notes

#### Persistent storage
PostgreSQL and pgAdmin use persistent storage by defining Docker volumes in `docker-compose.yaml` files. If you want to e.g. change credentials you need to recreate the volumes.

```sh
docker compose down -v
```
