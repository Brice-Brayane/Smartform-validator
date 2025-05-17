FROM python:3.11-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    chromium chromium-driver \
    fonts-liberation libappindicator3-1 libasound2 libatk1.0-0 libatk-bridge2.0-0 \
    libgtk-3-0 libxss1 libnss3 libx11-xcb1 libxcomposite1 libxdamage1 libxrandr2 \
    libgbm1 libxkbcommon0 ca-certificates \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY backend/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY backend ./backend
COPY frontend ./frontend
COPY tests ./tests

ENV FLASK_APP=backend/app.py
EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]
