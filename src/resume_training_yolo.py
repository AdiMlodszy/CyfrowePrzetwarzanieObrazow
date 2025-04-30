import os, tempfile, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scripts.load_config import load_config
from ultralytics import YOLO
from pathlib import Path

CONFIG_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'config.yaml'))

# 0.  tryb środowiska
mode     = os.getenv("ENV_MODE", "local")      # 'local' domyślnie

# 1.  config
cfg      = load_config(CONFIG_PATH)
paths    = cfg[f"{mode}_paths"]

# 2.  model

raw_yaml= Path(paths["dataset_yaml"]).read_text()
filled  = os.path.expandvars(raw_yaml)

tmp_yaml = Path(tempfile.gettempdir()) / "dataset.yaml"
tmp_yaml.write_text(filled)

# 3.  trening
model   = YOLO(paths["weights"])

model.train(
    data    = str(tmp_yaml),
    project = paths["output_dir"],
    **cfg["training"]
)
