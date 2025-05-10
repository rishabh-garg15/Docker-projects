FROM golang:1.21-alpine

ARG APP_PORT=8081
ENV APP_PORT=${APP_PORT}

WORKDIR /app
COPY main.go .

RUN go build -o server main.go

EXPOSE ${APP_PORT}
CMD ["./server"]

