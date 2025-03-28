# Katalog scripts

Miejsce na skrypty pomocnicze, takie jak:

- `download_data.sh` – skrypt pobierający dataset z zewnętrznego źródła.
- `convert_labels.py` – narzędzie do konwersji formatów anotacji (np. z Pascal VOC do YOLO).
- `check_augmentations.py` – szybki test augmentacji (generowanie obrazów podglądowych).
- `utils/` – ewentualne moduły współdzielone przez kilka skryptów.

**Przykładowe użycie**:

```bash
cd scripts
bash download_data.sh  # pobiera i rozpakowuje dane
python convert_labels.py --voc_folder data/voc --yolo_folder data/labels
```

> Trzymaj tu narzędzia, które nie pasują bezpośrednio do `src/` (gdzie jest główny kod YOLO), ale są przydatne do zarządzania projektem.

## Autor

add.ktiv
