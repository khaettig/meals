You can see a demo [here](https://meals-demo.khaettig.eu) with the username "demo" and password "demo".

Example docker-compose set up:
```
# docker-compose.yaml
version: "3"

services:
  meals:
    image: khaettig/meals
    container_name: meals
    restart: unless-stopped
    environment:
      - DATABASE_TYPE=postgresql
      - DATABASE_HOST=postgresql-meals
      - DATABASE_PORT=5432
      - DATABASE_NAME=meals
      - DATABASE_USER=meals
      - USE_WHITENOISE=True
      - DEBUG=False
    env_file:
      - .env
    ports:
      - "80:8000"

  postgresql:
    image: postgres
    container_name: postgresql-meals
    restart: unless-stopped
    environment:
      - POSTGRES_DB=meals
      - POSTGRES_USER=meals
    env_file:
      - .env
    volumes:
      - /data/postgresql-meals:/var/lib/postgresql/data

# .env
DATABASE_PASSWORD=<generated db_password>
POSTGRES_PASSWORD=<generated db_password>
SECRET_KEY=<generated secret_key>
```
