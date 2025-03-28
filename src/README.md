# Katalog src

W tym folderze znajdują się pliki związane z implementacją modelu YOLO i jego trenowaniem.
Możesz tu przechowywać m.in.:

- `train.py` – główny skrypt uruchamiający proces treningu.
- `detect.py` – skrypt służący do przeprowadzania inferencji na pojedynczych obrazach lub wideo.
- `config/` – ewentualnie podfolder z plikami konfiguracyjnymi (np. .yaml dla YOLO).
- `utils/` – pliki pomocnicze (funkcje do wczytywania danych, wizualizacji wyników, itp.).

**Przykładowe pliki** (do zapełnienia):

- `train.py` – zawiera kod ładowania danych, inicjalizacji modelu YOLO, pętli treningowej.
- `val.py` – jeśli chcesz osobno obsłużyć walidację.
- `config/yolov5_znaki.yaml` – plik z definicją ścieżek do train/val, listy klas, anchor boxów.

**Uruchomienie przykładowe**:

```bash
cd src
python train.py --epochs 50 --batch-size 16 --cfg config/yolov5_znaki.yaml
```

> Upewnij się, że posiadasz odpowiednie zależności (PyTorch, opencv-python, itp.).

## Autor

add.ktiv
