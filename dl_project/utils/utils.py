import os
from box.exceptions import BoxValueError
import yaml
from dl_project.base.logger import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64



def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a YAML file and returns its content wrapped in a ConfigBox.

    Args:
        path_to_yaml (Path): Path to the YAML file.

    Raises:
        FileNotFoundError: If the YAML file does not exist.
        ValueError: If YAML file is empty or has syntax errors.
        Exception: Any other unexpected errors.

    Returns:
        ConfigBox: Parsed YAML content wrapped in a ConfigBox for easier access.
    """
    try:
        # Ensure the input is a Path object
        path_to_yaml = Path(path_to_yaml)

        # Check if the file exists
        if not path_to_yaml.exists():
            raise FileNotFoundError(f"YAML file '{path_to_yaml}' does not exist.")

        # Read and parse the YAML file
        with open(path_to_yaml, "r", encoding="utf-8") as yaml_file:
            content = yaml.safe_load(yaml_file)

            # Check if the YAML file is empty
            if content is None:
                raise ValueError(f"YAML file '{path_to_yaml}' is empty.")

            logger.info(f"YAML file '{path_to_yaml}' loaded successfully")
            return ConfigBox(content)  # Wrap the dictionary in a ConfigBox

    except yaml.YAMLError as e:
        logger.error(f"YAML parsing error in file '{path_to_yaml}': {e}")
        raise ValueError(f"YAML parsing error in file '{path_to_yaml}': {e}")
    except Exception as e:
        logger.error(f"Unexpected error while reading YAML file '{path_to_yaml}': {e}")
        raise e




@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """save json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")




@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json files data

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded succesfully from: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary data

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"


def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())

