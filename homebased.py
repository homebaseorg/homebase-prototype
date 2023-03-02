import tomli as tomllib
from pathlib import Path
from shutil import copy
from xdg import xdg_config_home, xdg_data_home
import db
import handlers


config_dir = xdg_config_home() / "homebase"
data_dir = xdg_data_home() / "homebase"
config_file = config_dir / "config.toml"
config_file_example = Path("config.toml.example")
database_file = data_dir / "cache.db"


def main():
    check_existence()
    with open(config_file, "rb") as f:
        data = tomllib.load(f)
        content_by_tag = data["Tags"]
        # for tag in content_by_tag
        links = data["Tags"]["blogs"][0]
        entries = handlers.handle_rss(links)["entries"]

        title = entries[1]["title"]
        summary = entries[1]["content"]
        link = entries[1]["link"]
        date = entries[1]["date"]
        content = entries[1]["content"]
        print(f"Title: {title}")
        print(f"link: {link}")
        print(f"date: {date}")
        print(f"content: {content}")


def check_existence():
    # check if config dir and file exists
    if not config_dir.exists():
        config_dir.mkdir()

    if not config_file.exists():
        copy(config_file_example, config_file)

    # check if data dir and database exists
    if not data_dir.exists():
        data_dir.mkdir()

    if not database_file.exists():
        db.create_table(database_file)


if __name__ == "__main__":
    main()
