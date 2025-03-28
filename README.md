# Projekt – Detekcja 50 znaków drogowych przy użyciu YOLO

To repozytorium zawiera kod, dane oraz dokumentację projektu, który ma na celu wykrywanie 50 różnych znaków drogowych z materiału wideo lub obrazów, z wykorzystaniem sieci YOLO (You Only Look Once).

## Struktura repozytorium

- `src/` – kod źródłowy (skrypty do trenowania, inferencji, konfiguracje).
- `data/` – zbiór danych (obrazy, etykiety, pliki txt) – może być zarządzany przez Git LFS, jeśli duży.
- `notebooks/` – notatniki Jupyter, np. do wstępnej analizy, wizualizacji i prototypowania.
- `docs/` – dodatkowa dokumentacja (diagramy, pliki PDF, itp.).
- `scripts/` – skrypty pomocnicze, np. konwersja formatów etykiet, pobieranie danych.

## Dokumentacja sprintów

Wszystkie informacje o planie sprintów i harmonogramie znajdują się w Wiki repozytorium.

## Jak zacząć?

1. Sklonuj repozytorium:
   ```bash
   git clone https://github.com/<adimlodszy>/CyfrowePrzetwarzanieObrazu.git
   ```
2. Zainstaluj wymagane zależności (CUDA, PyTorch, YOLOv5 itd.).
3. Upewnij się, że zainstalowany jest Python 3.7+ (lub inny, zgodny z Twoim frameworkiem).
4. Przejrzyj folder `src/`, `scripts/` i pliki konfiguracyjne, aby uruchomić trening / inferencję.

## Lista zadań

- [ ] **Sprint 0**: Planowanie i przygotowanie środowiska.
- [ ] **Sprint 1**: Zebranie i etykietowanie danych.
- [ ] **Sprint 2**: Trening i podstawowa optymalizacja modelu.
- [ ] **Sprint 3**: Zaawansowane ulepszenia, testy końcowe i dokumentacja.

## Autor

add.ktiv