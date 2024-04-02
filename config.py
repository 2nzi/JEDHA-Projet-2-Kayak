from pathlib import Path
import yaml

def project_path(path: Path) -> str:
    """
    Load a YAML file from the given path and return the default save path.

    Args:
        path (Path): The path to the YAML file.

    Returns:
        str: The default save path.
    """

    with path.open("r") as f:
        config = yaml.safe_load(f)

    return config['path']['project_path']

def save_data_path(path: Path) -> str:
    """
    Load a YAML file from the given path and return the default save path.

    Args:
        path (Path): The path to the YAML file.

    Returns:
        str: The default save path.
    """

    with path.open("r") as f:
        config = yaml.safe_load(f)

    return config['path']['save_data_path']