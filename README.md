# SQLAlchemy - A Quick example
This projects sets up a classic sample database of employees and provides an example on how to get data from it using SQLAlchemy.

## Database diagram
![Employees Schema](./db/employees-schema.png?raw=true "Employees Schema")

## Requirements
- [docker](https://docs.docker.com/engine/install/ubuntu)
- [docker-compose](https://docs.docker.com/compose/install)

## Installation
```bash
# Setup the DB and the adminer service using docker
docker-compose up -d
docker logs mysql_db_1 -f

# Wait for all the demo data to be imported. IE. after you see this line:
# [Note] [Entrypoint]: /usr/local/bin/docker-entrypoint.sh: running /docker-entrypoint-initdb.d/I_load_salaries3.sql

# Create a venv, activate it and install the required libraries
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage
```bash
python main.py
```

## Access the DB management UI
- Open a web browser
- Navigate to http://localhost:8080 and use the following info to login:
  - System: MySQL
  - Server: db
  - Username: root
  - Password: password
  - Database: employees
