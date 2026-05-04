from pathlib import Path
from typing import Any
import base64
import json
import os

import yaml
from box import ConfigBox
from box.exceptions import BoxValueError

try:
    from ensure import ensure_annotations
except ModuleNotFoundError:
    def ensure_annotations(func):
        return func

from cnnClassifier import logger


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)

        if content is None:
            raise BoxValueError("YAML file is empty")

        logger.info(f"YAML file: {path_to_yaml} loaded successfully")
        return ConfigBox(content)
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"JSON file saved at: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    with open(path, "r") as f:
        content = json.load(f)
    logger.info(f"JSON file loaded from: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    import joblib

    joblib.dump(value=data, filename=path)
    logger.info(f"Binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    import joblib

    data = joblib.load(path)
    logger.info(f"Binary loaded from: {path}")
    return data


load_bins = load_bin


@ensure_annotations
def get_size(path: Path) -> str:
    size_in_kb = os.path.getsize(path) / 1024
    return f"{size_in_kb:.2f} KB"


def decoderImage(imgstring, filename):
    imgdata = base64.b64decode(imgstring)
    with open(filename, "wb") as f:
        f.write(imgdata)


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())
