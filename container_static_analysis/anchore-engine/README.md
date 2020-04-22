# Anchore Engine

## Starting the Anchore-Engine Environment

> $ docker-compose up -d

## Installing the anchore-cli tool in a Python Virtual Environment

> $ python3 -m venv venv

> $ source venv/bin/activate

> $ pip install anchorecli

## Running the anchore-cli 

### Exporting some variables

> $ ANCHORE_CLI_URL=http://127.0.0.1:8228/v1

> $ export ANCHORE_CLI_URL

> $ ANCHORE_CLI_USER=admin

> $ export ANCHORE_CLI_USER

> $ ANCHORE_CLI_PASS=foobar
export ANCHORE_CLI_PASS

### Adding an Image
> $ anchore-cli image add debian:latest

### Visualizing the list
> $ anchore-cli image list

## Checking vulnerabilities

> $ anchore-cli image vuln debian:latest all

> $ anchore-cli --json image vuln debian:latest all