#  Minimal Python Docker App

A lightweight Python-based web server container that returns basic JSON info about the project. Ideal for demos, testing, and DevOps experiments.

---

## Features

- Ultra-small image using `python:3.12-alpine`
- Simple HTTP server with project metadata
- Configurable port at **build-time**
- Defaults to port **8081** if not specified

---

##  Usage

###  Build and Run on Default Port (8081)

```bash
docker build -t python-app:01 .
docker run -p 8081:8081 -itd python-app:01

###   Build and Run on custom Port (8082)

# In the below mentioned command change 8082 to any desirable port which you want to run your application at

docker build --build-arg APP_PORT=8082 -t python-app:01 .
docker run -p 8082:8082 -itd python-app:01

