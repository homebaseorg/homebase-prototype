import tomli as tomllib
from pathlib import Path
from shutil import copy
from xdg import xdg_config_home

config_dir = xdg_config_home() / "homebase"
config_file = config_dir / "config.toml"
config_file_example = Path("config.toml.example")


def main():
    if not config_dir.exists():
        config_dir.mkdir()

    if not config_file.exists():
        copy(config_file_example, config_file)

    with open(config_file, "rb") as f:
        data = tomllib.load(f)
        print(data)


if __name__ == "__main__":
    main()
