# Katalog data

Tutaj przechowujesz zbiór danych do trenowania i walidacji:
- Obrazy (np. w formacie JPG, PNG).
- Etykiety (np. pliki .txt w formacie YOLO), ewentualnie w podfolderach train/val/test.

**Struktura przykładowa**:
```
data/
  images/
    train/
    val/
    test/
  labels/
    train/
    val/
    test/
```

**Uwagi**:
- Jeśli dane są bardzo duże, rozważ użycie [Git LFS](https://git-lfs.github.com/) lub zewnętrznego magazynu.
- Plik `.gitignore` może zawierać wpis `data/` aby nie śmiecić historii w repo.
- W plikach etykiet (YOLO) każda linia ma postać:
  ```
  <class_index> <x_center> <y_center> <width> <height>
  ```
  gdzie współrzędne znormalizowane do 0–1.
  
## Autor

add.ktiv