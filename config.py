from pathlib import Path
import yaml

def load_config(func):
    def wrapper(path: Path) -> str:
        with path.open("r") as f:
            config = yaml.safe_load(f)
        return func(config)
    return wrapper

@load_config
def project_path(config) -> str:
    return config['path']['project_path']

@load_config
def save_data_path(config) -> str:
    return config['path']['save_data_path']

@load_config
def scrapy_hotel_path(config) -> str:
    return config['path']['scrapy_hotel_path']


@load_config
def scrapy_url_path(config) -> str:
    return config['path']['scrapy_url_path']





# from pathlib import Path
# import yaml

# def project_path(path: Path) -> str:
#     """
#     Load a YAML file from the given path and return the default save path.

#     Args:
#         path (Path): The path to the YAML file.

#     Returns:
#         str: The default save path.
#     """

#     with path.open("r") as f:
#         config = yaml.safe_load(f)

#     return config['path']['project_path']

# def save_data_path(path: Path) -> str:
#     """
#     Load a YAML file from 

#     Args:
#         path (Path): The path to the YAML file.

#     Returns:
#         str:
#     """

#     with path.open("r") as f:
#         config = yaml.safe_load(f)

#     return config['path']['save_data_path']


# def save_data_path(path: Path) -> str:
#     """
#     Load a YAML file from 

#     Args:
#         path (Path): The path to the YAML file.

#     Returns:
#         str:
#     """

#     with path.open("r") as f:
#         config = yaml.safe_load(f)

#     return config['path']['save_data_path']