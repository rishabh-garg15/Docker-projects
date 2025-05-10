FROM python:3.12-alpine
ARG APP_PORT=8081
ENV APP_PORT=${APP_PORT}
WORKDIR /app
COPY main.py .
EXPOSE ${APP_PORT}
CMD ["python", "main.py"]
