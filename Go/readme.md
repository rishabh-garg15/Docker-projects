#  Minimal Go Docker App

A simple Go-based web server container that returns JSON info about the project. Configurable via Docker build argument.

---

##  Build and Run

### Default Port (8081)

```bash
docker build -t go-app:01 .
docker run -p 8081:8081 -itd go-app:01

Custom Port (e.g., 8082)

docker build --build-arg APP_PORT=8082 -t go-app:01 .
docker run -p 8082:8082 -itd go-app:01

