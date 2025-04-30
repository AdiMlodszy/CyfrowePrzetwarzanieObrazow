import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scripts.load_config import load_config

config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'config.yaml'))
cfg = load_config(config_path)


mode = os.getenv("ENV_MODE", "local")
paths = cfg[f"{mode}_paths"]

print("=== PATHS LOADED ===")
print(f"DATASET_YAML:    {paths['dataset_yaml']}")
print(f"LOCAL_WEIGHTS: {paths['weights']}")
print(f"LOCAL_OUTPUT_DIR: {paths['output_dir']}")

print("=== TRAINING CONFIGURATION ===")

for k, v in cfg["training"].items():
    print(f"{k}: {v}")