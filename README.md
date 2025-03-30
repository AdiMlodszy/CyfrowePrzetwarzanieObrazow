# Projekt – Detekcja 50 znaków drogowych przy użyciu YOLO

Ten projekt skupia się na wykrywaniu jednej kategorii – znaków drogowych – z materiału wideo lub obrazów, z wykorzystaniem sieci YOLO (You Only Look Once). Celem jest nauczenie modelu rozpoznawania znaków drogowych, które pojawiają się na wideo przez co najmniej 2 sekundy.

## Struktura repozytorium

- `src/` – kod źródłowy (skrypty do trenowania, inferencji, konfiguracje).
- `data/` – zbiór danych (obrazy, etykiety, pliki txt) – może być zarządzany przez Git LFS, jeśli duży.
- `notebooks/` – notatniki Jupyter, np. do wstępnej analizy, wizualizacji i prototypowania.
- `docs/` – dodatkowa dokumentacja (diagramy, pliki PDF, itp.).
- `scripts/` – skrypty pomocnicze, np. konwersja formatów etykiet, pobieranie danych.
- `Dockerfile` – konfiguracja środowiska Docker dla projektu.
- `requirements.txt` – lista bibliotek potrzebnych do uruchomienia projektu.

## Dokumentacja sprintów

Wszystkie informacje o planie sprintów i harmonogramie znajdują się w Wiki repozytorium.

## Jak zacząć?

### Użycie Dockera (zalecane)

1. **Sklonuj repozytorium:**

   ```bash
   git clone https://github.com/<adimlodszy>/CyfrowePrzetwarzanieObrazu.git
   ```

2. **Zbuduj obraz Docker:**

   ```bash
   docker build -t road-signs-detector .
   ```

3. **Uruchom kontener Docker:**

   ```bash
   docker run --rm -it --name road-signs-container road-signs-detector bash
   ```

4. **Sprawdź instalację:**

   ```bash
   python -c 'import torch, torchvision, ultralytics, cv2; print("Pakiety poprawnie zainstalowane!")'
   ```

### Lokalna instalacja (alternatywnie)

Jeśli nie korzystasz z Dockera:

1. Upewnij się, że zainstalowany jest Python 3.7+.
2. Zainstaluj wymagane zależności:

   ```bash
   pip install -r requirements.txt
   ```

3. Przejrzyj folder `src/`, `scripts/` i pliki konfiguracyjne, aby uruchomić trening lub inferencję.

## Lista zadań

- [ ] **Sprint 0**: Planowanie i przygotowanie środowiska.
- [ ] **Sprint 1**: Zebranie i etykietowanie danych.
- [ ] **Sprint 2**: Trening i podstawowa optymalizacja modelu.
- [ ] **Sprint 3**: Zaawansowane ulepszenia, testy końcowe i dokumentacja.

## Autor

add.ktiv
