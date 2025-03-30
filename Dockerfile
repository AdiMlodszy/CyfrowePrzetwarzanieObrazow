# Ten plik służy do budowy obrazu Dockera dla aplikacji Python

# 1. Użyj obrazu bazowego Python 3.9 slim
FROM python:3.9-slim

# 2. Zainstaluj wymagane pakiety systemowe
#    - gcc: kompilator C, wymagany do budowy niektórych pakietów Pythona
#    - git: narzędzie do kontroli wersji, wymagane do klonowania repozytoriów

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# 3. Ustaw katalog roboczy w kontenerze

WORKDIR /app

# 4. Skopiuj i zainstaluj zależności z pliku requirements.txt

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# 5. Ustaw zmienną środowiskową PYTHONUNBUFFERED na 1, aby wyłączyć buforowanie Pythona
ENV PYTHONUNBUFFERED=1

# 6. Tymczasowa komenda, która po prostu odpali bash
CMD ["bash"]







