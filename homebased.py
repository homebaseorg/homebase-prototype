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
db_file = data_dir / "cache.db"


def main():
    check_existence()
    with open(config_file, "rb") as f:
        data = tomllib.load(f)
        content_by_tag = data["Tags"]

        all_feeds_with_tags = (
            (tag, feed_url)
            for tag, feed_urls in content_by_tag.items()
            for feed_url in feed_urls
        )

        for tag, feed_url in all_feeds_with_tags:
            tag_feed = handlers.handle_feed(tag, feed_url)

            for feed in tag_feed:
                db.add_feed(db_file, feed)


def check_existence():
    # check if config dir and file exists
    if not config_dir.exists():
        config_dir.mkdir()

    if not config_file.exists():
        copy(config_file_example, config_file)

    # check if data dir and database exists
    if not data_dir.exists():
        data_dir.mkdir()

    if not db_file.exists():
        db.create_table(db_file)


if __name__ == "__main__":
    main()
