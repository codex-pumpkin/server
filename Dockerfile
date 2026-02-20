
FROM python:3.13-slim

RUN apt update && apt install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    gcc \
    ngspice \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN python -m pip install --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

EXPOSE 8000

CMD ["python", "-m", "src.main"]