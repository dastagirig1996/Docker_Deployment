# Stage 1:
FROM python:3.12.2-bullseye AS builder
WORKDIR /app
copy . /app
CMD ["python3","calculator.py"]

#Stage 2:
# FROM python:3.12.2-bullseye
# WORKDIR /app
# COPY --from=builder /app /app
# ENV PYTHONUNBUFFERED = 1
# CMD ["python3","calculator.py"]
