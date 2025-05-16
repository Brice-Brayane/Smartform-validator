# Dockerfile
# ---------------------------------------------------------------
# Basis-Image und Installation
# ---------------------------------------------------------------
FROM python:3.11-slim

WORKDIR /app

COPY backend/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "-m", "backend.app"]
