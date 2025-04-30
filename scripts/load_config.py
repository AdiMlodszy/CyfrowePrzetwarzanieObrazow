import os
import yaml
from dotenv import load_dotenv

###
# Load configuration from a YAML file and expand environment variables in the configuration file.
# This function reads a YAML configuration file, expands any environment
# variables found in the file, and returns the configuration as a Python dictionary.
# It also loads environment variables from a .env file if it exists.
# The function uses the `dotenv` library to load environment variables from a .env file
# and the `yaml` library to parse the YAML configuration file.
# The `os` library is used to expand environment variables in the configuration text.
# The function takes an optional argument `config_path` which specifies the path to the YAML configuration file.
# If not provided, it defaults to "config.yaml".
# The function returns a Python dictionary containing the configuration.
###
def load_config(config_path="config.yaml"):
    # Load environment variables from .env file
    load_dotenv()

    # Load the YAML configuration file
    with open(config_path, 'r') as f :
        raw_text = f.read()                        # 2. czytaj JAKO TEKST
        resolved  = os.path.expandvars(raw_text)   # 3. ${VAR} -> wartość z ENV
        cfg       = yaml.safe_load(resolved) 
    return cfg 